# python-air-quality-dashboard

This project creates an interactive Air Quality dashboard using Dash.

This project was completed as part of the course Machine Learning for Data Science at University Paris Cité, France.

# Dashboard
<img width="957" alt="fulldashboard" src="https://github.com/user-attachments/assets/62ba2859-6397-4179-b45e-bae070bd5386" />

Description ...  including a bar chart of AQI values and a table of the processed data

# Repository Overview
This repository contains 2 Python scripts: [airQuality](airQuality.py) and [app](app.py).

**airQuality** fetches AQI data dynamically from the [WAQI API](https://aqicn.org/api/) for specified cities and stores it in MongoDB allowing the dashboard to be refreshed with real-time data.

**app** builds a locally run Dash web application to visualize the air quality dashboard.
