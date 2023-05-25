import pandas as pd
import Levenshtein
import openai
import json
# import credits


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


answer = GPT(promt='How are you?').run()