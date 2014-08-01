import sys
import json

##def hw():
##    print 'Hello, world!'
##
##def lines(fp):
##    print str(len(fp.readlines()))

def txtToDict(sent_file):
    # afinnfile = open(sent_file)
    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    return scores

def computeScore(dictData, scores):
    result = 0
    if "text" in dictData.keys():
        tweetContent = dictData["text"]
        tweetWords = tweetContent.encode('ascii','ignore').split() # encode
        for word in tweetWords:
            if word in scores.keys():
                result = result + scores[word]
    return result

def jsonToDict(tweet_file, scores):
    results = []
    
    t = 0
    for line in tweet_file:
        #print line
        dictData = json.loads(line)
        #t = t + 1
        #if t == 3:
        #    break
        #print t
        results.append(computeScore(dictData, scores))
    return results

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    scores = {}
    scores = txtToDict(sent_file)
    # print scores.items() # Print every (term, score) pair in the dictionary
    result = jsonToDict(tweet_file, scores)
    #print(sys.argv[2])
    #print(result[0:9])
    ##  for r in result:
    ##      print r
    return result

if __name__ == '__main__':
    main()
