from nltk import FreqDist, classify, NaiveBayesClassifier
from nltk.corpus import twitter_samples, stopwords
from nltk.tag import pos_tag
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import re, string, random
import pandas as pd
import pickle


# on a bit of a time crunch here --> in practice would vectorize forloops and such: will implement later
# going to implement n-jobs in sklearn after done here
# dask also is an option here

# print(pos_tag(tweet_tokens[0]))

# lemmatizing because i want to deal with the  shorter versions
# if everything in the set is generalized from cats -> cat for example it make everything more full-proof
# have entered the data cleaning phase --> there is more I can do with extraction to make it 'better'
# but most of the 'showcasing' around extraction will be done when I am pulling data from twitter
def lemmatize_sentence(tokens):
    lemmatizer = WordNetLemmatizer()
    lemmatized_sentence = []
    for word, tag in pos_tag(tokens):
        if tag.startswith('NN'):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'
        lemmatized_sentence.append(lemmatizer.lemmatize(word, pos))
    return lemmatized_sentence


# regex here for similar reasons as lemmatization -->
# a lot of the data I am getting in does nothing for me
# I want the simplest version of word to train the model on
# not links, not numbers, etc
# does not have to be so high up, might move down later
# just nice to look at right now....


def rmv_noise(tweet_tokens, stop_wrds=()):
    cleaned_tokens = []

    for token, tag in pos_tag(tweet_tokens):
        token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|' \
                       '(?:%[0-9a-fA-F][0-9a-fA-F]))+','', token)
        token = re.sub("(@[A-Za-z0-9_]+)","", token)

        if tag.startswith("NN"):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'

        lemmatizer = WordNetLemmatizer()
        token = lemmatizer.lemmatize(token, pos)

        if len(token) > 0 and token not in string.punctuation and token.lower() not in stop_wrds:
            cleaned_tokens.append(token.lower())
    return cleaned_tokens


# using nltk here for word density stuff -->
# I need to get the actual information about the words before I do anything serious with the model here

def grab_all_words(cleaned_tokens_list):
    for tokens in cleaned_tokens_list:
        for token in tokens:
            yield token


def get_tweets(cleaned_tokens_list):
    for model_tokens in cleaned_tokens_list:
        yield dict([token, True] for token in model_tokens)


if __name__ == "__main__":

    # use former function to clean our sample words and  such
    positive_tweet_tokens = twitter_samples.tokenized('positive_tweets.json')
    negative_tweet_tokens = twitter_samples.tokenized('negative_tweets.json')
    stop_wrds = stopwords.words('english')

    # using nltk.tag for positve markings here
    # using averaged percepton tagger for token context within sentence

    positive_tweets = twitter_samples.strings('positive_tweets.json')
    negative_tweets = twitter_samples.strings('negative_tweets.json')
    text = twitter_samples.strings('tweets.20150430-223406.json')
    # grabing a little data at first, for the purpose of visualizing it.
    # Ultimatly training will happen in a larger context
    tweet_tokens = twitter_samples.tokenized('positive_tweets.json')[0:1]

    positive_cleaned_tokens_list = []
    negative_cleaned_tokens_list = []

    for tokens in positive_tweet_tokens:
        positive_cleaned_tokens_list.append(rmv_noise(tokens, stop_wrds))

    for tokens in negative_tweet_tokens:
        negative_cleaned_tokens_list.append(rmv_noise(tokens, stop_wrds))
    # using naive bayes classifier here because it is the one I am most familiar with

    # this will initalize the actual frequency of all words -->
    # unfortunately they are grabbed as a tuple here, not a dictionary
    # So, Naturally, I have to turn into a dictionary, which is more elegant and fast -->
    # better for models, too!
    pos_words_list = grab_all_words(positive_cleaned_tokens_list)
    neg_words_list = grab_all_words(negative_cleaned_tokens_list)
    freq_dist_pos = FreqDist(pos_words_list)
    freq_dist_neg = FreqDist(neg_words_list)

    positive_model = get_tweets(positive_cleaned_tokens_list)
    negative_model = get_tweets(negative_cleaned_tokens_list)

    positive_dataset = [(tweet_dict, "Positive")
                        for tweet_dict in positive_model]

    negative_dataset = [(tweet_dict, "Negative")
                        for tweet_dict in negative_model]

    dataset = positive_dataset + negative_dataset

    random.shuffle(dataset)

    # using a lot of input here, there are optimizations that I am going to push in later
    train_data = dataset[:10000]
    test_data = dataset[10000:]

    # actually going ahead and running it:
    classifier = NaiveBayesClassifier.train(train_data)

    save_classifier = open("naivebayes.pickle","wb")
    pickle.dump(classifier, save_classifier)
    save_classifier.close()





# need to make model static here
