### Apollo Enricher
Find new contacts for job titles keywords and domain names in Apollo. Also has an email verification class in Outreach.io.

**Before use the classes add configs for Apollo and Outreach to config.ini**

**Please look at main.py as example of using**

#### ProspectsDomainSearch.py:

#### ProspectsDomainSearch.ProspectsDomainSearch
Searches for people on Apollo.io for each domain in the input dataframe and concatenates the results. Use ProspectsDomainSearch(df,domain_col, titles).run()

Parameters:
- df: _DataFrame_. The input dataframe.
- domain_col: _string_, The name of the column in the input dataframe that contains the domains to search.
- titles: _list_ The list of job titles to search for.

#### ProspectsDomainSearch.ProspectsEnrichSearch
Searches for people on Apollo.io for each domain in the input dataframe and concatenates the results. Use ProspectsEnrichSearch(persons).run()

Parameters:
- persons: _DataFrame_. The input dataframe with Contacts from Apollo with columns ["id", "first_name", "last_name", "email", "original_Name"]

#### API.outreach_api.OutreachAPI().outreach_emails_checker
Searching for emails from dataframe in an Outreach database. Use OutreachAPI().outreach_emails_checker(df, column)

Parameters:
- df: _DataFrame_. Target dataframe
- column: _string_. a name of the column with emails in the dataframe

