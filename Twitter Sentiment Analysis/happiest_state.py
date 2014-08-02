import sys
import json

def txtToDict(sent_file):
    # afinnfile = open(sent_file)
    wordScores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        wordScores[term] = int(score)  # Convert the score to an integer.
    return wordScores

def computeScore(dictData, wordScores):
    tweetScore = 0
    if "text" in dictData.keys():
        tweetContent = dictData["text"]
        tweetWords = tweetContent.encode('ascii','ignore').split() # encode
        for word in tweetWords:
            if word in wordScores.keys():
                tweetScore = tweetScore + wordScores[word]
    return tweetScore

def identifyState(dictData):

    statesForm = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
    }

    stateDict = {}
    stateName = ""
    if "place" in dictData.keys():
        if dictData["place"] is not None:
            if  "US" == dictData["place"]["country_code"]:
                stateName = dictData["place"]["full_name"].encode('ascii','ignore')[-2:] # state (first step)
                return stateName
        
    if "user" in dictData.keys():
        if dictData["user"] is not None:
            #print dictData["user"]["location"].encode('ascii','ignore').strip()
            #if "USA "== dictData["user"]["location"].encode('ascii','ignore').strip()[-3:]:
            #    print "Good"
            tempLocation = dictData["user"]["location"].encode('ascii','ignore').strip()
            for stateAbb in statesForm.keys():
                if tempLocation.find(stateAbb) >= 0:
                    stateName = stateAbb
                    return stateName
    return stateName
            
def jsonToDict(tweet_file, wordScores):
    tweetScores = []
    stateDict = {}
    
    for line in tweet_file:
        #print line
        dictData = json.loads(line)

        tweetScore = computeScore(dictData, wordScores)
        tweetScores.append(tweetScore)
        
        stateName = identifyState(dictData)
        if stateName in stateDict.keys():
            stateDict[stateName] = stateDict[stateName] + tweetScore
        elif stateName != "":
            stateDict[stateName] = tweetScore
    return stateDict

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    wordScores = {}
    wordScores = txtToDict(sent_file)

    stateDict = {}
    stateDict = jsonToDict(tweet_file, wordScores)
    #print(sys.argv[2])
    #print(tweetScore[0:9])
    #for r in tweetScores:
    #    print r
    #print stateDict
    print max(stateDict, key=stateDict.get)
    


if __name__ == '__main__':
    main()
