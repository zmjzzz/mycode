import datetime
import pandas as pd
tupleA = (datetime.datetime(2018, 7, 18, 18, 30, 00, 00), )
dictA = {"name": ("AAA", "BBB"), "date": (datetime.datetime(2018, 7, 18, 18, 30, 00, 00), datetime.datetime(2018, 8, 18, 18, 30, 00, 00))}
pdA = pd.DataFrame(dictA)
dictB = {"name": ("AAA", "BBB"), "date": ("2018-07-18 18:30:00", "2018-07-28 18:30:00")}
pdB = pd.DataFrame(dictB)
pdB["date"] = pd.to_datetime(pdB["date"], format="%Y:%m:%d %H:%M:%S")



