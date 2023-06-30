# EcomFlow: Building Efficient Ecommerce Data Pipelines for Streamlined Analysis

Introduction
This project focuses on building data pipelines to analyze ecommerce data efficiently. The main objectives of this project are to establish data pipelines on AWS, enabling the analysis of ecommerce data using various business analytics tools. These pipelines will cover both streaming and batch processing of the data. Python3 will be utilized in AWS Lambda functions for data processing.

Dataset
The project utilizes ecommerce data from the UCI machine learning repository. The dataset comprises 8 columns and 541,909 rows in CSV format.

Tools
AWS API Gateway: Utilized for data ingestion (POST) and querying DynamoDB (GET).
AWS Kinesis Data Streams: Used for buffering the incoming data.
AWS Kinesis Firehose: Facilitates delivery of data to storage.
AWS Lambda Functions: Written in Python3 to process the data.
AWS Glue: Enables data catalog creation in the streaming process and ETL between S3 and Redshift in the batch process.
Storage
S3: Stores parquet data.
Redshift: Stores data and connects to Tableau or Power BI.
DynamoDB: Stores data with two tables (Customer & Invoice tables).
Streaming Process
Constantly pulls raw CSV data into the data pipelines. Transformed data is stored in S3, Redshift, and DynamoDB. BI analytics tools like Tableau, Athena, and Jupyter notebook can connect to the data in storage. Customers can query transaction data in DynamoDB using the API and primary keys (InvoiceNO & StockCode).

Sub-processes
Data Ingestion: Ingests CSV data into AWS Kinesis through the API gateway.
Data Cleaning: Cleans and performs necessary data type changes.
Data Processing & Storage: Moves data from Kinesis to storage (S3 or Redshift) and processes it.
BI Analytics: Establishes connections to BI tools like Tableau and Athena, and allows sending queries to DynamoDB.
Batch Process
Imports large volumes of raw data into the data pipelines. Transformed data is stored in S3 and Redshift. BI analytics tools like Power BI and Jupyter notebook can connect to the data in storage.

Sub-processes
Data Ingestion to S3: Ingests data into the S3 bucket.
Data Ingestion to Redshift: Ingests data into Redshift.
BI Analytics: Establishes connections to BI tools like Power BI and Jupyter notebook.
AWS Cognito
AWS Cognito is utilized for secure access to the API gateway with authentication tokens in the streaming process.

Conclusion
The established data pipelines enable efficient ETL processes and facilitate insightful data analysis. However, some improvements are needed, including implementing email notifications (AWS SNS) to monitor storage updates. Additionally, simplifying the setup of AWS Cognito for a larger number of users will be addressed in the future.
