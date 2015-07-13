from twython import Twython, TwythonError
import pandas as pd
import pprint
import time

APP_KEY =  's5zNSchQABtfEe683ZL5bgSW8'
APP_SECRET = 'dyQBARmUVVudDD56banM6OaZyOkwylkq1YO2DvbL0XnoR62sQ5'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

ids_df = pd.read_csv('Dem_Twitter1000.csv')
#print ids_df[0:5]
new_df = pd.DataFrame(columns=['id','screen_name','name','description','location'], index=[0])

print "read csv. beginning iteration"
for idx, row in ids_df.iterrows():
    try:
    	print "processing", idx, row
    	# the row is actually a Series, which means we need to get
    	# the values array out of it. here it only has one column,
    	# so we get the first value out of the array
    	user_id = str(row.iloc[0])
    	user_id = user_id[:-2]
    	#print user_id, type(user_id)
        info  = twitter.show_user(user_id=user_id)
        info_df = pd.DataFrame(info, columns=['id','screen_name','name','description','location'], index = [0])
        #print info_df
        new_df = new_df.append(info_df)
        #print new_df
        print " -- complete, now sleeping"
        time.sleep(6)
    except TwythonError:
        pass
        time.sleep(6)
    except:
        print "this is where it breaks"

print "complete. writing csv"

D_Twitter_indexed = new_df.set_index(['id'])
D_Twitter_indexed = pd.merge(D_Twitter_indexed, ids_df, left_index=True, right_on='id', how='outer')
D_Twitter_indexed.to_csv('Dem_Twitter_info1000.csv', sep='\t', encoding='utf-8')