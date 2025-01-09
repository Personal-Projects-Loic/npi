#!/usr/bin/env python3
import sys
import os
from dotenv import load_dotenv
import tweepy

oauth_consumer_key = os.getenv("API_KEY")
oauth_consumer_secret = os.getenv("API_KEY_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
bearer = os.getenv("BEARER")

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

def twitterOAuthV2() -> tweepy.Client:
    client = tweepy.Client(
        bearer_token=bearer,
        consumer_key=oauth_consumer_key,
        consumer_secret=oauth_consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
    )
    return client

def twitterOAuthV1() -> tweepy.API:
    auth = tweepy.OAuth1UserHandler(
        oauth_consumer_key, oauth_consumer_secret,
        access_token, access_token_secret
    )
    api = tweepy.API(auth)

def tweet(client, tweet_text):
    if len(tweet_text) > 280:
        print("Error: Tweet text exceeds 280 characters.")
        return
    
    try:
        response = client.create_tweet(text=tweet_text)
        if response.data:
            print(f"Tweet publié avec succès ! ID du tweet: {response.data['id']}")
        else:
            print("Erreur lors de l'envoi du tweet : pas de données dans la réponse.")
    except tweepy.TweepyException as e:
        print(f"Erreur lors de l'envoi du tweet: {e}")

def main():
    load_dotenv()

    if len(sys.argv) < 2 or sys.argv[1] == "-h":
        helper()
    elif sys.argv[1] == "-e" and len(sys.argv) == 3:
        ascii_value = letterToAscii(sys.argv[2])
        command_line = commandAppender(ascii_value)
        print(f"Encoded message: {command_line}")
        
        client = twitterOAuthV2()
        tweet(client, command_line)
    elif sys.argv[1] == "-d" and len(sys.argv) == 3:
        print(asciiToLetter(sys.argv[2]))
    else:
        print("Invalid arguments. Use -h for help.")

if __name__ == "__main__":
    main()
