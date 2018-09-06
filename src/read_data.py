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

crime_list = pd.read_csv("../data/DS2.csv")
crime_list = crime_list.set_index('Case Number')
assault_list = pd.read_csv("../data/DS1.csv")
crime_assault = assault_list.join(crime_list, on=['Case Number'])
print (crime_assault)
