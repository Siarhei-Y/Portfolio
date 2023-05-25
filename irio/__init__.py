import pandas as pd
import Levenshtein
import openai
import json
from irio import credits



class RegionCreator:
    """
    Assign an economic region for a country in a Dataset
    
    use inspectorio.Region(df, country_column).assign_regin()
    """
    def __init__(self, df, country_column, region_col_name='Region'):
        self.df=df
        self.country_column = country_column
        self.region_col_name='region_col_name'
        
        self.regions = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vRmy7Nl3uNIrffyP0MZ2Myzet0x8xrHgPhWWPlD-Bk2K01dAu1Ua1iaGWpbsN6qrA/pub?output=csv")
        self.regions_ = ['EMEA', 'LATAM', 'North America', 'APAC', "CHINA"]

    def region(self):
        self.df[self.country_column] = self.df[self.country_column].str.strip()
        for r in self.regions_:
            self.df.loc[self.df[self.country_column].isin(self.regions[self.regions.Region == r].Country), self.region_col_name] = r
            self.df.loc[self.df[self.country_column].isin(self.regions[self.regions.Region == r].Code), self.region_col_name] = r
        return self.df
    

class FuzzyComparator:
    def __init__(self, df1, df2, col1, col2, score=0.8,tracking=False):
        self.df1 = df1
        self.df2 = df2
        self.col1 = col1
        self.col2 = col2
        self.score = score
        self.tracking = tracking
    def compare(self):
        n = 0
        matches = []
        for index1, row1 in self.df1.iterrows():
            for index2, row2 in self.df2.iterrows():
                company1 = str(row1[self.col1])
                company2 = str(row2[self.col2])
                dist = Levenshtein.distance(company1.lower(), company2.lower())
                match_score = 1 - (dist / max(len(company1), len(company2)))
                n+=1
                if match_score >= self.score:
                    matches.append({'company1': company1, 'company2': company2, 'match_score': match_score})
                if self.tracking:
                    print(f'{n / (len(self.df1) * len(self.df2)) * 100:.2f}%')
        result_df = pd.DataFrame(matches)
        return result_df
        
class GPT:
    def __init__(self, promt):
        self.promt = promt

    def run(self):
    # Set up your OpenAI API credentials
        openai.api_key = credits.gpt_api_key

        # Define the prompt to send to the API
        prompt = self.promt
    
        # Define the parameters for the API request
        params = {
            "model": "text-davinci-002",
            "prompt": prompt,
            "temperature": 0.5,
            "max_tokens": 1024,
            "n": 1,
            "stop": ""
        }
    
        # Send the request to the OpenAI API
        response = openai.Completion.create(**params)
        # Parse the response to extract the generated text
        generated_text = response.choices[0].text.strip()
        return generated_text
            
        
    