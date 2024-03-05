from textblob import TextBlob
import math

# name 1: Meghan
# name 2: Tyler
# name 3:


class sentenceQuality():
    def __init__(self):
        # do some initialization, optional
        pass

    def calculateScores(self, tweet):
        # please implement this function
        # input: any tweet text
        # output: a list of scores for the tweet, it must include: score for length, score for Polarity, score for Subjectivity, and at least one score of the following:
        # https://en.wikipedia.org/wiki/Automated_readability_index
        # https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests
        # https://en.wikipedia.org/wiki/Gunning_fog_index
        # https://en.wikipedia.org/wiki/SMOG
        # https://en.wikipedia.org/wiki/Fry_readability_formula
        # https://en.wikipedia.org/wiki/Coleman%E2%80%93Liau_index
        # You should implement at least one score

        tweet = TextBlob(tweet)

        # Length
        # come back to this
        wordLength = len(tweet.words)
        length = 0.5
        if wordLength > 30 | wordLength < 3:
            length = 0.0
        elif wordLength > 11 & wordLength < 16:
            length = 1.0

        # Polarity
        polarity = tweet.sentiment.polarity

        # Subjectivity
        subjectivity = tweet.sentiment.subjectivity

        # Readability - we are using the Automated Readability Index
        minScore = 1
        maxDiff = 13
        numWords = len(tweet.words) - 1
        numChars = sum(1 for char in tweet if char.isalnum())
        numSentences = len(tweet.sentences)
        readability = math.ceil((4.71 * (numChars / numWords)) + (0.5 * (numWords / numSentences)) - 21.43)
        readability = round((readability - minScore) / maxDiff, 2) # calculated from a method to normalize scores


        return [length, polarity, subjectivity, readability]
        pass

    def calculateQuality(self, scores):
        # please implement this function to calculate a final quality score between 0 and 1
        # Input: a list of scores, which is the output of calculateScores
        # output: 0 means low quality, 1 mean high quality
        sum = 0
        for num in scores:
            sum = sum + num
        score = round(sum / len(scores), 3)
        return score
        pass


# this is for testing only
obj = sentenceQuality()
s = "DATA 233 is an excellent, challenging, and very exciting class!"

print("The scores for your input is " + str(obj.calculateScores(s)))

print("The final quality for your input is " + str(obj.calculateQuality(obj.calculateScores(s))))
