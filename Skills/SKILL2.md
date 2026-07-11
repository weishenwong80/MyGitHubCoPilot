#This is a skill name: Data analysis

description: Connect to employee database to perform an analysis based on user prompts

body:
Rule: Only allow "Select" statements when performing any actions on the database tables.
Step 1: Always establish a successful database connection first to my Azure SQL using the Visual Studio Code's SQL extension and the connection parameters that can be found in my Scripts folder named "config.yml". If connection fails, retry another 2 more times. If all 3 attempts fail, inform me and allow me to terminate the session. Do not use any other methods of connecting to the database.
Step 2: Inform me when a successful database connection has been established.
Step 3: Analyze the database schema and all database relationships before performing the data analysis.
Step 4: Return the results of the analysis in a summary table of not more than 500 words.
Step 5: Prompt me for any further questions. If there are no further questions, close the database connection. 
