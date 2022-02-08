##Follow step by step:

* 1- Create the database connection in glue (save the name)
* 2- Create a glue job, adding the connection previusly created (only if you import the .py direcly without serverless)
* 3- Add to the job and IAM rol with permision over this connection (only if you import the .py direcly without serverless)
* 4- edit the variable "conn_type" with the number corresponding to the database
* 5- edit the variable "glue_connection_name" with the glue connection's name previusly created
* 6- ORACLE ONLY: edit the variable "JDBC_CONNECTION_URL" with the JDBC URL 
* 7- add database name in "conn_test_database"
* 8- add table name in "conn_test_table" (depend of database type sql server is not needed)