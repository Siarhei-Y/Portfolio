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

### ML_models
- Covid Classification. Based on a Kaggle dataset. The purpose of the model to maximaze recall and identify potential mortal cases. Estimator: SGDClassifier, Recall: 0.93
- Prediction of Wild Blueberry Yield. Based on a Kaggle dataset. Estimator: CatBoostRegressor, MAE: 348.79915.

### a/b_tests
- ab_test_new_page. T-test to determine whether the new page generates more conversions than the old page.
- ab_bootstrap. Bootstrap on exponential distribution, T-test, p-value of bootstrapped difference.

### ANOVA
- [ANOVA, varience test for crop_yield_farm dataset on Kaggle.]([../../wiki](https://www.kaggle.com/code/yagelosergey/crop-yield-farm-anova/notebook?scriptVersionId=135926243)https://www.kaggle.com/code/yagelosergey/crop-yield-farm-anova/notebook?scriptVersionId=135926243)

### product_metrics_analysis
- Growth, Retention, Churn, MAU, DAU, Top-10 products.
