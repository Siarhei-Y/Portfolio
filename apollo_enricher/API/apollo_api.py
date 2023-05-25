import pandas as pd
import requests
import json
import configparser
from time import sleep
import logging
config = configparser.ConfigParser()
config.read('config.ini')

API_KEY = config['API KEY']['key']

logging.basicConfig(level=logging.INFO)


class PeopleSearch:
    """Return dataframe with people found by search parameters"""
    
    def __init__(self, organization_domains, person_titles):
        self.organization_domains = organization_domains
        self.page = 1
        self.url = "https://api.apollo.io/v1/mixed_people/search"
        self.data = {
            "api_key": API_KEY,
            "q_organization_domains": organization_domains,
            "page": self.page,
            "person_titles": person_titles
        }
        self.headers = {
            'Cache-Control': 'no-cache',
            'Content-Type': 'application/json'
        }

    def run(self):
        try:
            logging.info(f'Search starts for {self.organization_domains}')    
            self._send_response()
            self.pages = self.response['pagination']['total_pages']
            self.df = pd.json_normalize(self.response['people'])
            for i in range(2,self.pages+1):
                self.page = i
                self._send_response()
                self.df2 = pd.json_normalize(self.response['people'])
                self.df = pd.concat([self.df, self.df2], ignore_index=True)
        except Exception as e:
            logging.error(f'Error in PeopleSearch: {e}')
            self.df = pd.DataFrame()
        finally:
            return self.df        

    def _send_response(self):
        sleep(0.4)
        try:
            self.response = requests.request("POST", self.url, headers=self.headers, json=self.data).json()
        except Exception as e:
            logging.error(f'Error in _send_response: {e}')
            raise Exception('Failed to send response') from e

class PeopleEnrich:
    """Enrich people from Apollo"""
    
    def __init__(self, persons):
        cols = ["id", "first_name", "last_name", "email", "original_Name"]
        person_data = persons[cols]
        self.url = "https://api.apollo.io/v1/people/match"
        self.person = person_data.to_dict()

        if pd.notna(person_data['email']):
            self.data = {
                "api_key": API_KEY,
                "email": self.person['email'],
                "id": self.person['id'],
                "first_name": self.person["first_name"],
                "last_name": self.person["last_name"],
                "original_Name": self.person["original_Name"],

            }
        else:
            self.data = {
                "api_key": API_KEY,
                "id": self.person['id'],
                "first_name": self.person["first_name"],
                "last_name": self.person["last_name"],
                "original_Name": self.person["original_Name"],
            }

        self.headers = {
            'Cache-Control': 'no-cache',
            'Content-Type': 'application/json'
        }

    def run(self):
        try:
            logging.info(f'Search starts for {self.data}')    
            self._send_response()
            self.df = pd.json_normalize(self.response['person'])
        except Exception as e:
            logging.error(f'Error in PeopleSearch: {e}')
            self.df = pd.DataFrame()
        finally:
            return self.df        

    def _send_response(self):
        sleep(0.4)
        try:
            self.response = requests.request("POST", self.url, headers=self.headers, json=self.data).json()
        except Exception as e:
            logging.error(f'Error in _send_response: {e}')
            raise Exception('Failed to send response') from e