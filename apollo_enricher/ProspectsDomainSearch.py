import pandas as pd
from API.apollo_api import PeopleSearch, PeopleEnrich
import logging

logging.basicConfig(level=logging.INFO)

class ProspectsDomainSearch:
    """
    Initializes the class with the input parameters.

    Parameters:
    - df (pandas DataFrame): The input dataframe
    - domain_col (str): The name of the column in the input dataframe that contains the domains to search
    - titles (list): The list of job titles to search for
    """
    def __init__(self,df,domain_col, titles) -> None:
        self.df = df
        self.domain_col = domain_col
        self.titles = titles
    
    def run(self):
        self._people_searcher()
        return self.new_contacts

    def _people_searcher(self):

        """
        Searches for people on Apollo.io for each domain in the input dataframe and concatenates the results.
        """

        self.new_contacts = pd.DataFrame()
        for index, row in self.df.iterrows():
            people = PeopleSearch(organization_domains=row[self.domain_col], person_titles=self.titles).run()

            for col in self.df.columns:
                people[f'original_{col}'] = row[col]
            self.new_contacts = pd.concat([self.new_contacts,people], ignore_index=True)
            logging.info(f'Seach finished for {row[self.domain_col]}')
        # return self.new_contacts

class ProspectsEnrichSearch:
    """
    Initializes the class with the input parameters.

    Parameters:
    - persons (pandas DataFrame): The input dataframe with Contacts from Apollo with columns 
    ["id", "first_name", "last_name", "email", "original_Name"]

    """
    def __init__(self, persons) -> None:
        self.df = persons
    
    def run(self):
        self._people_searcher()
        return self.new_contacts
    
    def _people_searcher(self):
        """
        Searches for people on Apollo.io for each domain in the input dataframe and concatenates the results.
        """
        self.new_contacts = pd.DataFrame()
        for index, row in self.df.iterrows():
            people = PeopleEnrich(persons=row).run()

            if isinstance(people, pd.DataFrame):
                self.new_contacts = pd.concat([self.new_contacts, people], ignore_index=True)
                logging.info(f'Search finished for {row}')
            else:
                logging.warning(f'PeopleEnrich did not return a DataFrame for {row}. Skipping concatenation.')



    

