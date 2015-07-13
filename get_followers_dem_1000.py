from twython import Twython
import pandas as pd
import pprint

APP_KEY =  's5zNSchQABtfEe683ZL5bgSW8'
APP_SECRET = 'dyQBARmUVVudDD56banM6OaZyOkwylkq1YO2DvbL0XnoR62sQ5'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

D_Accounts = ('maddow','TheDemocrats','DWStweets','NancyPelosi','SenatorReid','ThePlumLineGS','dscc','dccc')

D_Twitter = pd.DataFrame({'id':00000}, index=[0])


for sn in (D_Accounts):
    followers = twitter.get_followers_ids(screen_name=sn, count=1000)
    followers_list = pd.DataFrame(followers['ids'])
    followers_list.columns = ['id']
    followers_list[sn] = True
    D_Twitter = pd.merge(D_Twitter, followers_list, on='id', how='outer')


D_Twitter_indexed = D_Twitter.set_index(['id'])
D_Twitter_indexed.to_csv('Dem_Twitter1000.csv')