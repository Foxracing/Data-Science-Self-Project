import sys
import json

##def hw():
##    print 'Hello, world!'
##
##def lines(fp):
##    print str(len(fp.readlines()))

def txtToDict(sent_file):
    # afinnfile = open(sent_file)
    wordScores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        wordScores[term] = int(score)  # Convert the score to an integer.
    return wordScores

def computeScore(dictData, wordScores):
    result = 0
    tweetWords = []
    if "text" in dictData.keys():
        tweetContent = dictData["text"]
        tweetWords = tweetContent.encode('ascii','ignore').split() # encode
        for word in tweetWords:
            if word in wordScores.keys():
                result = result + wordScores[word]
    return [result, tweetWords]

def jsonToDict(tweet_file, wordScores):
    tweetScores = []
    
    #t = 0
    for line in tweet_file:
        #print line
        dictData = json.loads(line)
        #t = t + 1
        #if t == 3:
        #    break
        #print t
        tweetScores.append(computeScore(dictData, wordScores))
    return tweetScores

def calcNewTerm(tweetScores):
    termDict = {}
    for eachTweet in tweetScores:
        for word in eachTweet[1]:
            if word in termDict.keys():
                termDict[word][0] = termDict[word][0] + eachTweet[0]
                termDict[word][1] = termDict[word][1] + 1
            else:
                termDict[word]= [eachTweet[0], 1]
    return termDict

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    wordScores = {}
    wordScores = txtToDict(sent_file)
    # print scores.items() # Print every (term, score) pair in the dictionary
    tweetScores = jsonToDict(tweet_file, wordScores)
    #print(sys.argv[2])
    #print(result[0:9])
    ##  for r in result:
    ##      print r
    #print tweetScores[0:5]
    termDict = {}
    termDict = calcNewTerm(tweetScores)
    #print "done...................."
    for key in termDict.keys():
        print key + " " + str(termDict[key][0]/termDict[key][1])
    
if __name__ == '__main__':
    main()
