"""
Prophet Time Series Forecasting Module
--------------------------------------
Utilizes Facebook's Prophet library to predict time series data, specifically focusing on revenue trends. The results are formatted into a pandas DataFrame, presenting actual and forecasted values, including the prediction confidence intervals.

Description:
    The core functionality of this module revolves around the Prophet library. It takes historical data as input and produces forecasts,
    encompassing both point predictions and uncertainty intervals. The main aim is to provide insights into future revenue trends based on past data.

Dependencies:
    - prophet: Time series forecasting tool.
    - pandas: Data manipulation and analysis.
    - numpy: Mathematical operations.

Main Functions:
    - run_prophet_forecasting(df): Forecasts time series data, returning a DataFrame that consists of actual sales, predicted sales, and the confidence interval.
"""

from prophet import Prophet
import numpy as np
import pandas as pd

def run_prophet_forecasting(df):
    """Forecast time series data using Facebook's Prophet."""
    m = Prophet(interval_width=0.95, daily_seasonality=True, yearly_seasonality=True)
    m.fit(df)
    future = m.make_future_dataframe(periods=90)
    forecast = m.predict(future)

    df_f = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].copy()
    df_f = df_f.merge(df, on='ds', how='left')
    df_f.columns = ['Date', 'Predicted Sales', 'Lower Bound', 'Upper Bound', 'Real Sales']

    df_f['Date'] = df_f['Date'].dt.strftime('%Y/%m/%d')
    df_f['Real Sales'] = df_f['Real Sales'].round(2)
    df_f['Predicted Sales'] = df_f['Predicted Sales'].round(2)
    df_f['Lower Bound'] = df_f['Lower Bound'].round(2)
    df_f['Upper Bound'] = df_f['Upper Bound'].round(2)

    return df_f