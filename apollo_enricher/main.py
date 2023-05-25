import pandas as pd
from ProspectsDomainSearch import ProspectsDomainSearch
from API.outreach_api import OutreachAPI

TITLES = ['Chief Executive Officer', 'CEO', 'Chief Technology Officer', 'CTO', 'Chief Operations Officer', 'COO', 'Chief Supply Chain Officer', 
          'Technical Director', 'Senior Vice President', 'Global Sourcing', 'Owner', 'Co-Founder', 'President', 'President', 'VP']
DF = pd.read_excel('contacts.xlsx')
DF = DF[['Name','Domain Name']]
SAVE_PATH = 'contacts_contacts.csv'
SAVE_FINAL_EXCEL = 'contacts_contacts_or_checked.xlsx'


def find_contacts_in_apollo(save_path):
    new_prospects = ProspectsDomainSearch(df=DF, domain_col='Domain Name', titles=TITLES).run()
    new_prospects.to_csv(save_path, index=False)   

def compare_or(check_path,save_excel_file):
    apollo = pd.read_csv(check_path)
    checked_prospects = OutreachAPI().outreach_emails_checker(df=apollo,column='email')
    checked_prospects.to_excel(save_excel_file, index=False)

def drop_duplicates(file):
    df = pd.read_csv(file)
    df.drop_duplicates(inplace=True)
    df.to_csv(file, index=False)

find_contacts_in_apollo(save_path=SAVE_PATH)
drop_duplicates(file=SAVE_PATH)
compare_or(check_path=SAVE_PATH, save_excel_file=SAVE_FINAL_EXCEL)
