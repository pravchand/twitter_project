"""
Twikit testing script
"""

# import asyncio

from twitter_search.config_utils.config import EMAIL, PASSWORD, USERNAME
from twikit import Client


client = Client("en-US")


async def main():
    # Asynchronous client methods are coroutines and
    # must be called using `await`.
    await client.login(
        auth_info_1=USERNAME, auth_info_2=EMAIL, password=PASSWORD
    )

    ###########################################

    # Search Latest Tweets
    tweets = await client.search_tweet("New York AND Pollution", "Latest")
    for tweet in tweets:
        print(tweet)

    # # Search more tweets
    # more_tweets = await tweets.next()
