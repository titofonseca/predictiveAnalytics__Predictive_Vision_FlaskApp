"""
GA4 Data Fetching Module

Description:
This module is responsible for fetching data from Google Analytics 4 (GA4) using the Google Analytics Data API v1beta. It retrieves the total revenue for a specified period and structures the data into a pandas DataFrame for further analysis.

Dependencies:
- google.analytics.data_v1beta: Google's library for GA4 Data API.
- pandas: Used for data manipulation and analysis.
- dotenv: For loading environment variables from the .env file.
- json: For handling JSON data.

Main Functions:
- initialize_analyticsreporting() : Initializes the Google Analytics Data API v1beta client using the service account information.
- get_report(client)              : Makes the API request to fetch data from GA4 based on the provided configurations.
- fetch_ga4_data()                : Orchestrates the data fetching process, processes the API response, and returns a DataFrame.
"""

import os
import pandas as pd
import json
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange, Dimension, Metric, RunReportRequest
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configurations
Key = os.environ.get('GOOGLE_SERVICE_KEY_PATH')
Property = os.environ.get('GA4_PROPERTY_ID')

def initialize_analyticsreporting():
    """Initialize the GA4 Data API v1beta client using the service account."""
    with open(Key, 'r') as file:
        service_account_info = json.load(file)
    client = BetaAnalyticsDataClient.from_service_account_info(service_account_info)
    return client

def get_report(client):
    """Fetch data from GA4 based on the provided configurations."""
    request = RunReportRequest(
        property=f"properties/{Property}",
        date_ranges=[DateRange(start_date="791daysAgo", end_date="yesterday")],
        dimensions=[Dimension(name="date")],
        metrics=[Metric(name="totalRevenue")],
        keep_empty_rows=True
    )
    return client.run_report(request)

def fetch_ga4_data():
    """Orchestrate the data fetching process and process the API response into a DataFrame."""
    try:
        client = initialize_analyticsreporting()
        response = get_report(client)
        
        dimensionHeaders = [dim.name for dim in response.dimension_headers]
        metricHeaders = [metric.name for metric in response.metric_headers]
        finalRows = []

        for row in response.rows:
            rowObject = {}
            dimensions = row.dimension_values
            metrics = row.metric_values
            
            for header, dimension in zip(dimensionHeaders, dimensions):
                rowObject[header] = dimension.value
                
            for metricHeader, metric in zip(metricHeaders, metrics):
                rowObject[metricHeader] = metric.value

            finalRows.append(rowObject)

        return pd.DataFrame(finalRows)
    
    except Exception as e:
        print(f"Error fetching data from GA4: {e}")
        return None