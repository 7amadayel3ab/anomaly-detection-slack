# Sales Anomaly Detection with BigQuery ML & Slack Alerts

This project automatically detects anomalies in daily sales data using BigQuery ML's ARIMA model and sends alerts to Slack.

## Architecture

- **Data**: Synthetic daily sales data stored in BigQuery.
- **Model**: ARIMA_PLUS time‑series model trained with `CREATE MODEL`.
- **Detection**: Scheduled query using `ML.DETECT_ANOMALIES` to flag unusual values.
- **Alerting**: Cloud Function triggered by Cloud Scheduler sends Slack notifications.

## Setup

1. Create BigQuery dataset `anomaly_detection` and table `sample_sales`.
2. Train ARIMA model.
3. Deploy Cloud Function with Slack webhook URL.
4. Schedule daily runs with Cloud Scheduler.

## Results

![Slack Alert Example](slack-alert.png)

## Technologies

- Google BigQuery ML
- Cloud Functions (Python)
- Cloud Scheduler
- Slack API
