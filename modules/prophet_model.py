"""
Prophet Forecasting Module

Description:
This module utilizes Facebook's Prophet to forecast time series data. It takes data fetched from Google Analytics 4, processes it to fit the requirements of Prophet, and then runs a forecast. The results are structured into a pandas DataFrame, which contains the actual data alongside the forecasted values, and the upper and lower bounds of the forecast.

Dependencies:
- prophet: The main library used for time series forecasting.
- pandas: Used for data manipulation and analysis.
- numpy: Used for numerical operations.

Main Functions:
- run_prophet_forecasting(df): Takes a DataFrame of GA4 data and runs a time series forecast using Prophet. The function returns a DataFrame with the real sales, predicted sales, and the upper and lower bounds of the forecast.
"""

from prophet import Prophet
import numpy as np
import pandas as pd

def run_prophet_forecasting(df):
    """Forecast time series data using Facebook's Prophet."""
    df['ds'] = pd.DatetimeIndex(df['date'])
    df['y'] = df['totalRevenue'].astype(float)
    df = df[['ds', 'y']]

    m = Prophet(interval_width=0.95, daily_seasonality=True, yearly_seasonality=True)
    m.fit(df)
    future = m.make_future_dataframe(periods=90)
    forecast = m.predict(future)

    df_f = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].copy()
    df_f = df_f.merge(df, on='ds', how='left')

    df_f['Date'] = df_f['Date'].dt.strftime('%Y/%m/%d')
    df_f['Real Sales'] = df_f['Real Sales'].round(2)
    df_f['Predicted Sales'] = df_f['Predicted Sales'].round(2)
    df_f['Lower Bound'] = df_f['Lower Bound'].round(2)
    df_f['Upper Bound'] = df_f['Upper Bound'].round(2)

    return df_f