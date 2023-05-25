import pandas as pd
import configparser
import requests
import logging
from time import sleep

logging.basicConfig(level=logging.INFO)

class OutreachAPI():
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

        self.data = {
        'client_id': self.config['OUTREACH']['client_id'],
        'client_secret': self.config['OUTREACH']['secret'],
        'redirect_uri': self.config['OUTREACH']['redirect_uri'],
        'refresh_token': self.config['OUTREACH']['refresh_token'],
        'grant_type': 'refresh_token'
    }

        self._auth()
        response = requests.get(url='https://api.outreach.io/api/v2/prospects?page[size]=1000&count=false', headers=self.headers)
        print(response.status_code)
    
    def _auth(self):
        response = requests.post('https://api.outreach.io/oauth/token', data=self.data)
        response_json = response.json()
        
        access_token = response_json['access_token']
        refresh_token = response_json['refresh_token']
        
        self.config.set('OUTREACH', 'refresh_token', refresh_token)

        self.headers = {
            'Authorization': f'Bearer {access_token}'
        }
        self._save_token()

    def _save_token(self):
        try:
           with open('config.ini', 'w') as configfile:
               self.config.write(configfile)
        except Exception as e:
            logging.error(e)


    def __check_emails_in_outreach(self,emails_list):
        email_status_dict = {}

        for email in emails_list:
            url = f"https://api.outreach.io/api/v2/prospects/?filter[emails]={email}"
            sleep(0.1)
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                data = response.json().get("data")
                if data:
                    email_status_dict[email] = True
                else:
                    email_status_dict[email] = False
            else:
                email_status_dict[email] = None
            logging.info(f"{email} checked")

        return email_status_dict

    def outreach_emails_checker(self, df, column):
        emails_list = df[column].tolist()
        email_status_dict = self.__check_emails_in_outreach(emails_list=emails_list)
        df['in_outreach'] = df['email'].apply(lambda email: email_status_dict[email])
        self.or_checked_emails = df.copy()
        return self.or_checked_emails