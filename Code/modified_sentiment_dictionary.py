"""
@package sentiment
Twitter sentiment analysis.

This code performs sentiment analysis on Tweets.

A custom feature extractor looks for key words and emoticons.  These are fed in
to a naive Bayes classifier to assign a label of 'positive', 'negative', or
'neutral'.  Optionally, a principle components transform (PCT) is used to lessen
the influence of covariant features.

"""
import csv, random
import nltk
import tweet_features, tweet_pca
import sys

spam_words_file = "J:\PDM\SpamWords.txt"

def get_email_spam(args):
    # read emails
    fp = open(sys.argv[1], 'rb')
    email = fp.readlines()
    spam_file = open(spam_words_file, 'rb')
    spam = spam_file.readlines()
    spam_count = 0
    
    for s in xrange(len(spam)):
        spam[s] = spam[s].strip()

    for token in email:
        trim_token = token.strip()
        #print "trim_token = ", trim_token
        if(trim_token in spam):
            print "email contains spam ", trim_token
            spam_count = spam_count + 1
    
    print spam_count
        

get_email_spam(sys.argv[1:])