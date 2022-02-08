# ETL - JDBC Connector Validator

Tool to test jdbc connections without broke anything, if you have the jdbc connection miss configure the cloudwatch log guide you.

## Pre-requirements 📋

Install in your pc:

* AWS CLI
* Nodejs
* Serverless
* Python 3x

## Deploy 📦

* Create an aws credential with the name: aws-test-con
* Update credential information
* Edit python file in /scritps folder following the steps inside
* In the command line positioned in the project folder execute the following statement:

```bash
npm run deploy
```

## Builded with  🛠️

* [Serverless🛰️](https://www.serverless.com/)
* [Python🐍](https://www.python.org/)
* [Pyspark](https://spark.apache.org/docs/latest/api/python/)
* [Numpy](https://numpy.org/doc/stable/)
* [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.copy)
* [AWS GLUE](https://aws.amazon.com/es/glue/)
* [AWS S3](https://aws.amazon.com/es/s3/)

## JDBC Connections Supported.

:heavy_check_mark: Microsoft SQL Server
:heavy_check_mark: Oracle
:heavy_check_mark: MySql
:heavy_check_mark: Redshift
:recycle: Others in development mode

## Authors & Contributors ✒️

* Alvaro Garcia - Data Engineer
* Fabian Almanzan - DevOps Manager
