import pandas as pd

#Below are some of the usefult command for PAndas
#print (data.head(4))
#print (data.values) //shows values of each row in array
#print (data.describe) #quick statistic summary
#print (data['Primary Type']) //displays the speciifc columns
#print (data.iloc[3:6,0:3]) #displays Rows 3-5 and column 0-2
#print(data.iloc[3]) //displays 3rd Row
#print (data.iloc[0,3]) //displays 0th Row, 3rd column
#data2 = data.cumsum()
#print (data2.plot())

bike_station = pd.read_csv("../data/bike_station.csv")
bike_trips = pd.read_csv("../data/bike_trips.csv")

bike_station_trip = pd.merge(bike_station, bike_trips, how='right', left_on=['station_id'], right_on=['start_station_id'])
bike_station_trip.to_csv("../data/result_data.csv")
