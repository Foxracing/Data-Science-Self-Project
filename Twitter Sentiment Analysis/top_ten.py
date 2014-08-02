import sys
import json
import heapq

def findHashtag(dictData):
    newHashtag = ""
    if "entities" in dictData.keys():
        if dictData["entities"] is not None:
            if len(dictData["entities"]["hashtags"]) > 0:
                #print dictData["entities"]["hashtags"][0]
                if dictData["entities"]["hashtags"][0]["text"] is not None:
                    #print dictData["entities"]["hashtags"][0]["text"].encode('ascii','ignore')
                    newHashtag = dictData["entities"]["hashtags"][0]["text"].encode('ascii','ignore').strip()
                    #print newHashtag
    return newHashtag

def jsonToDict(tweet_file):
    hashtagDict = {}

    for line in tweet_file:
        dictData = json.loads(line)
        newHashtag = findHashtag(dictData)
        #print len(newHashtag)
    
        if newHashtag in hashtagDict.keys():
            #print "check2"
            hashtagDict[newHashtag] = hashtagDict[newHashtag] + 1
        elif newHashtag != "":
            #print "check1"
            hashtagDict[newHashtag] = 1
    return hashtagDict

def main():
    tweet_file = open(sys.argv[1])
    hashtagDict = {}
    hashtagDict = jsonToDict(tweet_file)
    
    #for key in termDict.keys():
    #    print key + " " + str(float(termDict[key])/float(sum(termDict.values())))
    k = 10
    k_keys_sorted = heapq.nlargest(k, hashtagDict, key=hashtagDict.__getitem__)
    #print k_keys_sorted
    
    for key in k_keys_sorted:
        print key + " " + str(hashtagDict[key])
    
if __name__ == '__main__':
    main()
