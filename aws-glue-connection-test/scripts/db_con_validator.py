## import libs 
import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql import SparkSession
import numpy as np
from pyspark.sql import functions as sf
from awsglue.utils import getResolvedOptions
from py4j.java_gateway import java_import
from awsglue.transforms import Map
from awsglue.dynamicframe import DynamicFrame, DynamicFrameReader
##

##Follow step by step:
# 1- Create the database connection in glue (save the name )
# 2- Create a glue job, adding the connection previusly created
# 3- Add to the job and IAM rol with permision over this connection
# 4- edit the variable "conn_type" with the number corresponding to the database
# 5- edit the variable "glue_connection_name" with the glue connection's name previusly created
# 6- ORACLE ONLY: edit the variable "JDBC_CONNECTION_URL" with the JDBC URL 
# 7- add database name in "conn_test_database"
# 8- add table name in "conn_test_table" (depend of database type sql server is not needed)

conn_type = 4 #Redshift= 1 Mysql= 2 SqlServer= 3 Oracle=4
glue_connection_name = "<connection name>" #connection name previusly created in glue
JDBC_CONNECTION_URL = "jdbc:oracle:thin:@//<endpoint>:1521/ORCL" #ORACLE database only
conn_test_database = "<database-name>" #database for test
conn_test_table= "<table-name>" #table name for test



def getConnections(glueContext,conn_type,glue_connection_name,conn_test_database,JDBC_CONNECTION_URL) :
    # selection of database engine drive
    if conn_type == 1: #redshift
        driver = "com.amazon.redshift.jdbc41.Driver"
    elif conn_type == 2: #mysql
        driver = "com.mysql.jdbc.Driver"
    elif conn_type == 3: #microsoft sql server
        driver = "com.microsoft.sqlserver.jdbc.SQLServerDriver"
    elif conn_type == 4: #oracle
        driver = "oracle.jdbc.driver.OracleDriver"


    if conn_type == 4: #oracle needs generate the connection in other way
        conn_test = glueContext.extract_jdbc_conf(glue_connection_name)
        conn_config = {
        "user": conn_test['user'], 
        "password": conn_test['password'], 
        "driver": driver, 
        "url": JDBC_CONNECTION_URL
        }
    else: #all other type of databases
        conn_test = glueContext.extract_jdbc_conf(glue_connection_name)
        conn_config = {
            "user": conn_test['user'], 
            "password": conn_test['password'], 
            "driver": driver, 
            "url": "{};database={}".format(conn_test['url'], conn_test_database) #you need the database name
        }
        

    return conn_config


# ------------------------------------------------------------------------------------------------------------------------- SETUP
print("setup")

print("glue context")
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session


print("java_import")
java_import(sc._gateway.jvm,"java.sql.Connection")
java_import(sc._gateway.jvm,"java.sql.DatabaseMetaData")
java_import(sc._gateway.jvm,"java.sql.DriverManager")
java_import(sc._gateway.jvm,"java.sql.SQLException")
java_import(sc._gateway.jvm,"java.sql.*")

# ------------------------------------------------------------------------------------------------------------------------- test connections
try:

    print("generate connection")
    conn = getConnections(glueContext,conn_type,glue_connection_name,conn_test_database,JDBC_CONNECTION_URL)


    print("try connection")
    if conn_type == 1: #redshift
        query = """(SELECT * FROM {schema}.{table} ) t""".format(schema=conn_test_database,table=conn_test_table)
    elif conn_type == 2: #mysql
        query = """(SELECT * FROM {schema}.{table} ) t""".format(schema=conn_test_database,table=conn_test_table)
    elif conn_type == 3: #microsoft sql server
        query = """(SELECT 1 as result ) t"""
    elif conn_type == 4: #oracle
        query = """(SELECT * FROM {schema}.{table} FETCH NEXT 1 ROWS ONLY ) t""".format(schema=conn_test_database,table=conn_test_table)


    df = spark.read.jdbc(conn['url'], query, properties=conn)
    df.printSchema()
    df.show()
    print("Connection CONFIRMED !!")


except Exception as err:
    print(f"Connection Error: {err}")
    raise err


