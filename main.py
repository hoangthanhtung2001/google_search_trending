# -*- coding: utf-8 -*-
"""Extracting-GoogleTrends-Data_PythonCodeTutorial.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lMX3VemgcfGpiGNlQJNPyivSXHAVYe6O
"""

# !pip install pytrends
import pandas as pd
from pytrends.request import TrendReq
import seaborn
# for styling
seaborn.set_style("darkgrid")

# initialize a new Google Trends Request Object
pt = TrendReq(hl="en-US", tz=360)

# # set the keyword & timeframe
# pt.build_payload(["Python", "Java"], timeframe="all")

# # get the interest over time
# iot = pt.interest_over_time()
# iot

# plot it
# iot.plot(figsize=(10, 6))

# get hourly historical interest
# data = pt.get_historical_interest(
#     ["data science"], 
#     cat=396, 
#     year_start=2022, month_start=1, day_start=1, hour_start=0,
#     year_end=2022, month_end=2, day_end=10, hour_end=23,
# )
# data

# # the keyword to extract data
# kw = "Top Trending tiktok"
# pt.build_payload([kw],geo="VN",timeframe="all")
# # get the interest by country
# ibr = pt.interest_by_region("REGION", inc_low_vol=True, inc_geo_code=True)

# # sort the countries by interest
# print("---------------------------------------------------")
# print("---------------------------------------------------")
# print("Xep hang tim kiem theo Khu vuc Viet Nam:")
# print(ibr[kw].sort_values(ascending=False)[:10])


# # get related topics of the keyword
# rt = pt.related_topics()
# print("---------------------------------------------------")
# print("---------------------------------------------------")
# print("Chu de lien quan:",rt[kw]["top"])

# # get related queries to previous keyword
# rq = pt.related_queries()
# print("Truy van lien quan:",rq[kw]["top"])


# # get suggested searches
# pt.suggestions("Tiktok")

# another example of suggested searches
# pt.suggestions("America")

# trending searches per region
ts = pt.trending_searches(pn="vietnam")
print("---------------------------------------------------")
print("---------------------------------------------------")
print("Top Search Trending in Viet Nam")
print(ts)

# real-time trending searches
print("---------------------------------------------------")
print("---------------------------------------------------")
print("Top Search Trending Hien tai")
trending_searches_df = pt.realtime_trending_searches(pn="VN",count=500)
print(trending_searches_df)