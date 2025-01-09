#!/usr/bin/env python3
import sys
import os
from dotenv import load_dotenv
import tweepy

def helper():
    print("Usage :")
    print("\t./npi.py -e \"sentence to encode\"")
    print("\t./npi.py -d \"number to decode\"")

def letterToAscii(input_str):
    rev_str = input_str[::-1]
    res = 0

    for char in rev_str:
        res = res * 256 + ord(char)
    return res

def asciiToLetter(num):
    result = []
    num = int(num)

    while num > 0:
        result.append(chr(num % 256))
        num //= 256
    return ''.join(result[::1])

def commandAppender(ascii):
    prefix = "echo '[q]sa[ln0=aln256%Pln256/snlbx]sb"
    suffix = "snlbxq'|dc"
    res = prefix + str(ascii) + suffix

    return res

def twitterOAuth():
    oauth_consumer_key = os.getenv("API_KEY")
    oauth_consumer_secret = os.getenv("API_KEY_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuthHandler(oauth_consumer_key, oauth_consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    
    try:
        api.verify_credentials()
        print("Authentication OK")
        return api
    except tweepy.TweepyException as e:
        print(f"Error during authentication: {e}")
        sys.exit(1)

def tweet(api, tweet_text):
    if len(tweet_text) > 280:
        print("Error: Tweet text exceeds 280 characters.")
        return
    api.update_status(tweet_text)


def main():
    load_dotenv()

    api = twitterOAuth()
    if len(sys.argv) < 2 or sys.argv[1] == "-h":
        helper()
    elif sys.argv[1] == "-e" and len(sys.argv) == 3:
        ascii_value = letterToAscii(sys.argv[2])
        tweet_text = f"Encoded message: {ascii_value}"
        tweet(api, tweet_text)
    elif sys.argv[1] == "-d" and len(sys.argv) == 3:
        print(asciiToLetter(sys.argv[2]))
    else:
        print("Invalid arguments. Use -h for help.")

if __name__ == "__main__":
    main()
