# readme loganalysis.py 
# author: Tim Ohlendorf 
# date: 29.08.2018
#
# environment
# python version 2.7.12
# psql version 9.5.13 
#
# run program: python loganalysis.py 
#
# program contains 3 functions which connect using library psycopg2 with the news sql-database 
# 
# get_top_three_articles() returns array [article-title, views] - with the three most viewed articles of all time 
# get_sumpageview_authors_per_article() returns array [author, views] - with the name of the author and the sum 
# of all of his articles views
# get_days_avg_requests_error_over_one_percent() - returns array [date, float] - checks every date (sum requests by date of timestamp) for # requests that lead to errors, if more than 1% of requests lead to error (HTTP STATUS 4XX), 
# it is added to the array 