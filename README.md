# sensor_data_aws_integration
Integration of AWS services (S3, Glue, Athena) on the creation of a pipeline for analysis of simulated temperature sensor data. Using a Python script to simulate data including temperature, humidity, pressure, vibration and power.

This data is loaded into a S3 bucket, a Glue crawler is created to extract it and Athena is used to query the data. Some examples are on this repository, and can be used to compute averages, identify trends and anomalies within the data.

Built as a learning project.
