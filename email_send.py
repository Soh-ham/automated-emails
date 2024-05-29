import yagmail
import os
import pandas as pd
from news import NewsFeed
import datetime

username = "*********3@gmail.com"
password = os.getenv("PASSWORD")

df = pd.read_excel('people.xlsx')

for index, row in df.iterrows():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    news_feed = NewsFeed(interest=row['interest'], from_date=yesterday, to_date=today)
    email = yagmail.SMTP(user=username, password=password)
    email.send(to=row['email'],
               subject=f"Your {row['interest']} news for today!",
               contents=f"Hi, {row['name']}\n See what`s on about {row['interest']} today!\n {news_feed.get()}Max.")