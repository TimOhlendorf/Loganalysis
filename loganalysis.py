#!/usr/bin/env python
import psycopg2
DBNAME = "news"


def get_top_three_articles():
    pg = psycopg2.connect(database=DBNAME)
    cursor = pg.cursor()
    query = """SELECT articles.title, subq.sum FROM articles,
               (SELECT log.path, count(*) as sum FROM log WHERE log.path != '/'
               GROUP BY log.path ORDER BY sum DESC limit 3) AS subq
               WHERE subq.path LIKE CONCAT('%',articles.slug)
               ORDER BY subq.sum DESC;"""
    cursor.execute(query)
    results = cursor.fetchall()
    return results
    pg.close()


def get_sumpageview_authors_per_article():
    pg = psycopg2.connect(database=DBNAME)
    cursor = pg.cursor()
    query = """SELECT authors.name, sum(subq2.sum) AS totalhits FROM authors,
               (SELECT authors.name, subq.path, articles.title, subq.sum
               FROM articles JOIN authors ON authors.id=articles.author,
               (SELECT log.path, count(*) AS sum FROM log WHERE log.path != '/'
               GROUP BY log.path
               ORDER BY sum DESC) AS subq
               WHERE subq.path LIKE CONCAT('%',articles.slug)
               ORDER BY subq.sum) AS subq2
               WHERE subq2.name = authors.name GROUP BY authors.name
               ORDER BY totalhits DESC;"""
    cursor.execute(query)
    results = cursor.fetchall()
    return results
    pg.close()


def get_days_avg_requests_error_over_one_percent():
    pg = psycopg2.connect(database=DBNAME)
    cursor = pg.cursor()
    query = """SELECT to_char(subqallrequestsperday.date2,'Month DD, YYYY')
               AS "date",
               to_char(subqerrorperday.totalerrorperday::float/
               subqallrequestsperday.totalaccessperday::float*100,
               '0.99 %') AS "% of requests lead to error"
               FROM (SELECT count(log.status) AS totalerrorperday,
               Date(log.time) AS date1
               FROM log WHERE status like '4%'
               GROUP BY date1) AS subqerrorperday
               INNER JOIN (SELECT count(log.status) AS totalaccessperday,
               Date(log.time) AS date2
               FROM log GROUP BY date2) AS subqallrequestsperday
               ON subqerrorperday.date1 = subqallrequestsperday.date2
               WHERE subqerrorperday.totalerrorperday::float/
               subqallrequestsperday.totalaccessperday::float > 0.01;"""
    cursor.execute(query)
    results = cursor.fetchall()
    return results
    pg.close()


print('The most popular articles of all time (title - views): ')
print(' views \n'.join([' - '
      .join(['{:}'.format(item) for item in row])
      for row in get_top_three_articles()])+' views')

print('Who are the most popular article authors of all time? (author - views)')
print(' views \n'.join([' - '
      .join(['{:}'.format(item) for item in row])
      for row in get_sumpageview_authors_per_article()])+' views')

print('On which days did more than 1% requests lead to errors?'
      '(date - % of req. lead to err.)')
print('\n'.join([' - '
      .join(['{:}'.format(item) for item in row])
      for row in get_days_avg_requests_error_over_one_percent()]))
