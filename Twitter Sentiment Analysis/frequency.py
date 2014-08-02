import sys
import json

def txtToDict(sent_file):

    wordScores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        wordScores[term] = int(score)  # Convert the score to an integer.
    return wordScores

def splitTweet(dictData):
    tweetWords = []
    if "text" in dictData.keys():
        tweetContent = dictData["text"]
        tweetWords = tweetContent.encode('ascii','ignore').split() # encode
    return tweetWords

def jsonToDict(tweet_file):
    tweetData = []

    for line in tweet_file:
        dictData = json.loads(line)
        tweetData.append(splitTweet(dictData))
    return tweetData

def calcTermFrequency(tweetData):
    termDict = {}
    for eachTweet in tweetData:
        for word in eachTweet:
            if word in termDict.keys():
                termDict[word] = termDict[word] + 1
            else:
                termDict[word]= 1
    return termDict

def main():
    tweet_file = open(sys.argv[1])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    tweetData = jsonToDict(tweet_file)
    termDict = {}
    termDict = calcTermFrequency(tweetData)
    for key in termDict.keys():
        print key + " " + str(float(termDict[key])/float(sum(termDict.values())))
    
if __name__ == '__main__':
    main()
