import os
from google.cloud import bigquery
import requests

SLACK_WEBHOOK_URL = os.environ.get('SLACK_WEBHOOK_URL')

def detect_anomalies(request):
    client = bigquery.Client()
    query = """
    SELECT
      date,
      sales,
      is_anomaly,
      anomaly_probability
    FROM
      ML.DETECT_ANOMALIES(
        MODEL `epicfuely777.anomaly_detection.sales_arima_model`,
        STRUCT(0.95 AS anomaly_prob_threshold),
        (SELECT date, sales FROM `epicfuely777.anomaly_detection.sample_sales` WHERE date >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY))
      )
    WHERE is_anomaly = TRUE
    """
    query_job = client.query(query)
    results = query_job.result()
    anomalies = [dict(row) for row in results]

    if anomalies and SLACK_WEBHOOK_URL:
        message = f"*⚠️ Anomaly Detected!*\nDate: {anomalies[0]['date']}\nSales: {anomalies[0]['sales']}\nProbability: {anomalies[0]['anomaly_probability']:.2f}"
        requests.post(SLACK_WEBHOOK_URL, json={'text': message})
        return f"Alert sent for {anomalies[0]['date']}", 200
    elif anomalies:
        return "Anomalies found but no Slack webhook configured.", 200
    else:
        return "No anomalies detected.", 200
