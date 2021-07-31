from pandas_datareader import data
import datetime

start = datetime.datetime(2021,3,1)
end = datetime.datetime(2021,3,10)

df = data.DataReader(name="AAPL", data_source="yahoo", start=start, end=end)

print(df)