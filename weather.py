import requests
import sqlite3 as lite
import datetime

cities = { "Pittsburgh": '40.4406, 79.9959',
            "Austin": '30.303936,-97.754355',
            "Boston": '42.331960,-71.020173',
            "Chicago": '41.837551,-87.681844',
            "Cleveland": '41.478462,-81.679435'
        }

# api key is from  https://darksky.net/dev/
api_key = "79cc0385b63239c41d1742a5ec1b7164"

# Note the URL pattern for the API call:   https://api.forecast.io/forecast/APIKEY/LATITUDE,LONGITUDE,TIME
url = "https://api.darksky.net/forecast/79cc0385b63239c41d1742a5ec1b7164"

# create the necessary datetime objects to iterate through the exercise
start_date = datetime.datetime.now() - datetime.timedelta(days=30)
end_date = datetime.datetime.now()

# establish the connection to the database
con = lite.connect('weather.db')
cur = con.cursor()

# create the table
cities.keys()
with con:
    cur.execute('CREATE TABLE IF NOT EXISTS daily_temp ( day_of_reading INT, city1 REAL, city2 REAL, city3 REAL, city4 REAL, city5 REAL);') #use your own city names instead of city1..



for k,v in cities.items():
    query_date = end_date - datetime.timedelta(days=30) #set value each time through the loop of cities
    while query_date < end_date:
        #query for the value
        print (query_date)
        r = requests.get(url + v + ',' +  query_date.strftime('%Y-%m-%dT12:00:00'))

        with con:
            #insert the temperature max to the database
            cur.execute('UPDATE daily_temp SET ' + k + ' = ' + str(r.json()['daily']['data'][0]['temperatureMax']) + ' WHERE day_of_reading = ' + query_date.strftime('%s'))

 #increment query_date to the next day for next operation of loop
        query_date += datetime.timedelta(days=1) #increment query_date to the next day


con.close() # a good practice to close connection to database













