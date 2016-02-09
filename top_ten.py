import sys
import json

def main():
	tweet_file = open("c:/DataSciencePython/output.txt")         #open(sys.argv[2])
    
	alllines_tweet = tweet_file.readlines()

	#create a dict of all hashtags in the tweet in output.txt: {'word',[number of occurrence of that word in all tweets])
	allhashtags = {}
	#/////////////////////////////////////////////////////////////////////////////////////////
	
	for i in range(0, len(alllines_tweet)):
	
	#//////////////////////////Identify hashtags for each tweet in output.txt //////////////	
		parsed_line = json.loads(alllines_tweet[i])    # here we convert ith line of output.txt to a dict
		
		if ("entities" in parsed_line) and (parsed_line["lang"].encode('utf-8') == 'en'):  #filter only english tweets with non null content
			listofindicetext = parsed_line["entities"]["hashtags"]
			
			if listofindicetext:                                      #get all hashtags of a given tweet
				for i in range(0, len(listofindicetext)):
					thishashtag = listofindicetext[i]["text"]
					thishashtag = thishashtag.encode('utf-8')
					thishashtag = thishashtag.lower()
				
	#////////////////////////////// Count hashtags ////////////////////////////					
				if thishashtag not in allhashtags:
					allhashtags[thishashtag] = [0,0]                   #the key is the hashtag
					allhashtags[thishashtag][0] = 1                    #1st item is the number of occurrences of this hashtag in all tweets
					allhashtags[thishashtag][1] = 0                    #2nd item is the frequency of this hashtag
				else:
					allhashtags[thishashtag][0] += 1
	
	#////////////////////////////// Determine the frequency of hashtags ////////////////////////////
	for thishashtag in sorted(allhashtags):                     #sort all hashtags by alphabetical order and do loop
		occurrenceinalltweets = allhashtags[thishashtag][0]     # number of occurrences of the hashtag in all tweets
		occurrenceofallhashtagsinalltweet = len(allhashtags)    # number of occurrences of all hashtags in all tweets
		frequency = round( occurrenceinalltweets / float(occurrenceofallhashtagsinalltweet) , 4)
		allhashtags[thishashtag][1] = frequency                 #update the frequency in the dict
		#frequency = [# of occurrences of the hashtag in all tweets]/[# of occurrences of all hashtags in all tweets]
		#print thishashtag, frequency
	
	#///////////////////////////// Display the 10 most frequent hashtags//////////////////////////
	tenmostfrequenthashtags = sorted(allhashtags, key=allhashtags.get, reverse=True)[:10]
	for thishashtag in tenmostfrequenthashtags:
		print thishashtag, allhashtags[thishashtag][1] 
	

	tweet_file.close()

if __name__ == '__main__':
	main()