#import tvDatafeed
from tvDatafeed import TvDatafeed, Interval

#tv = TvDatafeed()
tv = TvDatafeed(username='richard.genet@gmail.com', password='116richardgenet')
#data = tv.get_hist(symbol='ES1!', exchange='CME', interval=Interval.in_1_hour, n_bars=10)
#print(data)

#df = tv.get_hist(symbol='AAPL', exchange='NASDAQ', interval='1d', n_bars=10)
df = tv.get_hist(symbol='AAPL', exchange='NASDAQ', interval=Interval.in_daily, n_bars=10)
print(df)
