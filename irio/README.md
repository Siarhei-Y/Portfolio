### Irio
Simple functions that help to clean and complete the data

#### RegionCreator
Assign an economic region for a country in a Dataset. Use RegionCreator(df, country_column, region_col_name).region()

Parameters: 
- df: _DataFrame_. Provide a target dataframe.        
- country_column: _string_. Provide a target column with country names.
- region_col_name: _string_. Give a name to a column with economic regions.

#### FuzzyComparator
Class constructor that initializes the FuzzyComparator object with two dataframes, the columns to compare, and a matching score. Use FuzzyComparator(df1, df2, col1, col2, score=0.8,tracking=False).compare()

Parameters:
- df1: _DataFrame_. First dataframe to compare.
- df2: _DataFrame_. Second dataframe to compare.
- col1: _string_. Column name in first dataframe to compare.
- col2: _string_. Column name in second dataframe to compare.
- score: _float_. Matching score threshold (default=0.8).
- tracking: _bool_. Set to True to print progress during comparison (default=False).

#### GPT
Initializes a new instance of the GPT class with a given prompt.

**Warning - Add your OpenAI Api Key to the class before use.**

Parameters:
- prompt: _string_. The text prompt to send to the OpenAI API
