import nltk
from nltk.corpus import twitter_samples
from nltk.tag import pos_tag
from nltk.stem.wordnet import WordNetLemmatizer

# using nltk.tag for positve markings here
# using averaged percepton tagger for token context within sentence

positive_tweets = twitter_samples.strings('positive_tweets.json')
negative_tweets = twitter_samples.strings('negative_tweets.json')
text = twitter_samples.strings('tweets.20150430-223406.json')
# grabing a little data at first, for the purpose of visualizing it.
# Ultimatly training will happen in a larger context
tweet_tokens = twitter_samples.tokenized('positive_tweets.json')[0:1]

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

print(lemmatize_sentence(tweet_tokens[0]))


# regex here for similar reasons as lemmatization -->
# a lot of the data I am getting in does nothing for me
# I want the simplest version of word to train the model on
# not links, not numbers, etc
