import pandas as pd
import requests

# Reading sample data into dataframe
df = pd.read_csv('test_data_sample.csv', sep=',')
df.head(10)

# AWS API endpoint
URL = 'https://yd68muw1l7.execute-api.us-east-2.amazonaws.com/ecom_prod/test'

for i in df.index:

    # convert every row into json
    export = df.loc[i].to_json()
    # print(export)
    # writing into api
    response = requests.post(URL, data=export)

    print(response)
