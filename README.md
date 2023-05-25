## Siarhei Yahela's Portfolio

### irio
Simple functions that help to clean and complete the data
- RegionCreator: Assign an economic region for a country in a Dataset. Use RegionCreator(df, country_column, region_col_name).region()
- FuzzyComparator: Class constructor that initializes the FuzzyComparator object with two dataframes, the columns to compare, and a matching score. Use FuzzyComparator(df1, df2, col1, col2, score=0.8,tracking=False).compare()
- GPT: Initializes a new instance of the GPT class with a given prompt.

### apollo_enricher
Find new contacts for job titles keywords and domain names in Apollo. Also has an email verification class in Outreach.io.
- ProspectsDomainSearch.ProspectsDomainSearch. Searches for people on Apollo.io for each domain in the input dataframe and concatenates the results. Use ProspectsDomainSearch(df,domain_col, titles).run()
- ProspectsDomainSearch.ProspectsEnrichSearch. Searches for people on Apollo.io for each domain in the input dataframe and concatenates the results. Use ProspectsEnrichSearch(persons).run()
- API.outreach_api.OutreachAPI().outreach_emails_checker. Searching for emails from dataframe in an Outreach database. Use OutreachAPI().outreach_emails_checker(df, column)

### webscrapers
- fundoodata Selenium Web Scraper. Scrape www.fundoodata.com list of companies
