from flask import Flask, render_template, request
from flask import send_from_directory
from flask import json
from flask import Response
from main import main
from datetime import datetime
import pandas as pd
import numpy as np


app = Flask(__name__)

# Metric mapping
METRIC_MAP_GA4 = {
    'Revenue': 'totalRevenue',
    'Sessions': 'sessions',
    'Conversions': 'ecommercePurchases'
}

METRIC_MAP_UA = {
    'Revenue': 'ga:transactionRevenue',
    'Sessions': 'ga:sessions',
    'Conversions': 'ga:transactions'
}

@app.route('/', methods=['GET', 'POST'])
def index():
    forecast_df = None
    if request.method == 'POST':
        metric_display = request.form.get('metric')

        # Map display name to technical metric names
        metric_ga4 = METRIC_MAP_GA4[metric_display]
        metric_ua = METRIC_MAP_UA[metric_display]

        # Here, we process the selected metric.
        forecast_df = main(metric_ga4, metric_ua)

    current_year = datetime.now().year
    return render_template('index.html', forecast_df=forecast_df, metrics=METRIC_MAP_GA4.keys(), current_year=current_year)

@app.route('/export_csv', methods=['GET'])
def export_csv():
    metric = request.args.get('metric')
    metric_ga4 = METRIC_MAP_GA4[metric]
    metric_ua = METRIC_MAP_UA[metric]

    forecast_df = main(metric_ga4, metric_ua)
    
    # Converter DataFrame para CSV
    csv_data = forecast_df.to_csv(index=False)
    
    # Criar resposta com conteúdo CSV
    response = Response(csv_data, mimetype="text/csv")
    response.headers['Content-Disposition'] = f'attachment; filename=forecast_{metric}.csv'
    
    return response

@app.route('/<path:path>')
def static_file(path):
    return send_from_directory('static', path)

@app.route('/get_data', methods=['GET'])
def get_data():
    try:
        metric = request.args.get('metric')
        metric_ga4 = METRIC_MAP_GA4[metric]
        metric_ua = METRIC_MAP_UA[metric]

        forecast_df = main(metric_ga4, metric_ua)
        
        forecast_df.replace({np.nan: None}, inplace=True)

        data = {
            'table_data': forecast_df.to_dict(orient='records'),
            'dates': forecast_df['Date'].tolist(),
            'real_values': forecast_df['Real ' + metric].tolist(),
            'predicted_values': forecast_df['Predicted ' + metric].tolist(),
            'upper_bound': forecast_df['Upper Bound'].tolist(),
            'lower_bound': forecast_df['Lower Bound'].tolist()
        }
        
        return app.response_class(
            response=json.dumps(data, default=str),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        return str(e), 500  # Return the exception as a string for debugging

if __name__ == '__main__':
    app.run(debug=True)
