import sys
import json

def countscoreoftweet(t):
	scoreoftweet = 0
	listofwordintweet = t.split()                            #split each word of the tweet t to a list of word
	for thisword in listofwordintweet:
		if thisword.lower() in scores:                          #for a given tweet, display each word that are also in sent_file
			scoreofthisword = int(scores[str(thisword.lower())])
			#print thisword, scoreofthisword                    #print the word that matches and its corresponding score
			scoreoftweet = scoreoftweet + scoreofthisword
	return scoreoftweet
	
def lines(fp):
	print str(len(fp.readlines()))

def main():
	sent_file = open("c:/DataSciencePython/AFINN-111.txt")       #open(sys.argv[1])
	tweet_file = open("c:/DataSciencePython/output.txt")         #open(sys.argv[2])
    
	alllines_tweet = tweet_file.readlines()
	alllines_sent = sent_file.readlines()
	
	statesscore = {}
	
	states = {
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
	
	for thiskey in states:
		statesscore[thiskey.lower()] = [ states[thiskey].lower(), 0, 0, 0 ] #create the same dict in lower case
	                                                                        #and add a score to the state name, by creating a list [state name, sum score, total tweet in state, average]
	
	#//////////// Create a dictionary of term w/ score from AFINN-111.txt ////////////////// 
	global scores                                      #global variable across all functions
	scores = {}                                        #initialize a new dict
	for i in range(0, len(alllines_sent)):
		term, score = alllines_sent[i].split("\t")
		scores[term] = int(score)                                 #each element of the dict is a term and its score
	#///////////////////////////////////////////////////////////////////////////////////////
		
	for i in range(0, len(alllines_tweet)):
		parsed_line = json.loads(alllines_tweet[i])               # here we convert ith line of output.txt to a dict
		state1 = state2 = state = ""
		
		if "text" in parsed_line:
			getatweet = parsed_line["text"]
			getatweetunicode = getatweet.encode('utf-8')
			scoretweet = countscoreoftweet(getatweetunicode)
			
			if scoretweet > 1:            #select only positive tweets
			
				#if parsed_line["lang"].encode('utf-8') == 'en':
					
				if parsed_line["user"]["location"] is not None:  
					location = parsed_line["user"]["location"]
					locationunicode = location.encode('utf-8')
					if (',' in list(locationunicode)) and (len(locationunicode.split(', ')) > 1):
						state1 = locationunicode.split(', ')[1]
						state1 = state1.lower()
						#print "location: ", locationunicode
						#print "state1: ", state1
					else:
						state1 = ""
				
				if parsed_line["place"] is not None:                         #equivalent to bool(parsed_line["place"])
					place = parsed_line["place"]["full_name"]
					placeunicode = place.encode('utf-8')
					if ',' in list(placeunicode):
						state2 = placeunicode.split(', ')[1]
						state2 = state2.lower()
						#print "place: ", placeunicode
						#print "state2: ", state2
					else:
						state2 = ""
						
				if (state2 != ""):                        #use state2 if available, otherwise use state1
					state = state2
				else:
					state = state1
				
				if (state != ""):  
					print "state:", state
					print "score: ", scoretweet
					print "-" * 10				
				
				if state in statesscore:						
					statesscore[state][1] += scoretweet           #add scores of every positive tweet, per state
					statesscore[state][2] += 1                    #keep track of number of every positive tweet, per state
					statesscore[state][3] = statesscore[state][1] / float( statesscore[state][2] ) #update the average
				                                                  #calculate here the average of score per state
	
	print statesscore
	#print sorted(statesscore.items(), key=lambda x:x[1][3], reverse=True)
	print "Happiest state: ", max(statesscore, key=lambda i: statesscore[i][3])    #sort the dict per value of average, and return the corresponding key
																				  #compare each item in statesscore by the value of "statesscore[i]" at index 3
	sent_file.close()
	tweet_file.close()

if __name__ == '__main__':
	main()