"""
UA (Universal Analytics) Data Fetching Module
---------------------------------------------
Retrieves revenue data from Universal Analytics (UA) using the Google Analytics Reporting API v4 and structures it into a pandas DataFrame.

Description:
    This module is tailored to manage data extraction from UA. It defines the process for data retrieval, processes the API responses, 
    and organizes the data in a structured manner suitable for further analytical operations.

Dependencies:
    - googleapiclient.discovery: Google's interface for the Google Analytics Reporting API v4.
    - pandas: Data manipulation and analysis.
    - dotenv: Management of environment variables from the .env file.
    - oauth2client.service_account: Authentication using service account.

Main Functions:
    - initialize_analyticsreporting(): Prepares the Google Analytics Reporting API v4 client.
    - get_report(analytics): Fetches UA data with specified configurations.
    - fetch_ua_data(): Central function that oversees the data retrieval process.
"""

import os
import pandas as pd
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configurations
Key = os.environ.get('GOOGLE_SERVICE_KEY_PATH')
View = os.environ.get('UA_VIEW_ID')

Scope = [
    'https://www.googleapis.com/auth/analytics.readonly',
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

def initialize_analyticsreporting():
    credentials = ServiceAccountCredentials.from_json_keyfile_name(Key, Scope)
    analytics = build('analyticsreporting', 'v4', credentials=credentials)
    return analytics

def get_report(analytics, metric="ga:transactionRevenue"):
    return analytics.reports().batchGet(
        body={
            'reportRequests': [
                {
                    'viewId': View,
                    'dateRanges': [{'startDate': '2005-01-01', 'endDate': '2023-07-31'}],
                    'dimensions': [{'name': 'ga:date'}],
                    'metrics': [{'expression': metric}],
                    "orderBys": [
                        {"fieldName": "ga:date", "sortOrder": "ASCENDING"}
                    ]
                }
            ]
        }
    ).execute()

def fetch_ua_data(metric="ga:transactionRevenue"):
    try:
        analytics = initialize_analyticsreporting()
        response = get_report(analytics, metric)
        finalRows = []
        for row in response.get('reports', [{}])[0].get('data', {}).get('rows', []):
            date = row['dimensions'][0]
            value = float(row['metrics'][0]['values'][0])
            finalRows.append({'ds': date, 'y': value})
        return pd.DataFrame(finalRows)
    except Exception as e:
        print(f"Error fetching data from UA: {e}")
        return None

