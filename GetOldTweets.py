import GetOldTweets3 as got

# python -m pip install GetOldTweets3 --user
# This is for printing top tweets by user barackobama

tweetCriteria = got.manager.TweetCriteria().setUsername("barackobama")\
                                           .setTopTweets(True)\
                                           .setMaxTweets(10)
tweet = got.manager.TweetManager.getTweets(tweetCriteria)
for x in range(len(tweet)):
    print (tweet[x].text),

