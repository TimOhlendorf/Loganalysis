## Titel:  Readme loganalysis.py 
## Description:
###### The program contains three functions which connect using library psycopg2 with the news sql-database:
+ get_top_three_articles() returns array [article-title, views] - with the three most viewed articles of all time 
+ get_sumpageview_authors_per_article() returns array [author, views] - with the name of the author and the sum  of all of his articles views
+ get_days_avg_requests_error_over_one_percent() - returns array [date, float] - checks every date (sum requests by date of timestamp) for # requests that lead to errors, if more than 1% of requests lead to error (HTTP STATUS 4XX),  it is added to the array 


## Installation 
+ download loganalysis.py 
+ download news sql-database https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
  You will need to unzip this file after downloading it. The file inside is called newsdata.sql. Put this file into the vagrant   
  directory, which is shared with your virtual machine.

  To build the reporting tool, you'll need to load the site's data into your local database. Review how to use the psql command in this   lesson: (FSND version)

  To load the data, cd into the vagrant directory and use the command psql -d news -f newsdata.sql.
  Here's what this command does:

  psql — the PostgreSQL command line program
  -d news — connect to the database named news which has been set up for you
  -f newsdata.sql — run the SQL statements in the file newsdata.sql
  Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating   
  tables and populating them with data.
  
+ install psycopg2 library
+ install python 2.7.12

# environment
python version 2.7.12
psql version 9.5.13 

## Usage
run program in console: python loganalysis.py 

## further information 
author: Tim Ohlendorf 
date: 29.08.2018
