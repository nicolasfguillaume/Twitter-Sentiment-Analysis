import sys
import json

def countscoreoftweet(t):
	scoreoftweet = 0
	listofwordintweet = t.split()                            #split each word of the tweet t to a list of word
	for thisword in listofwordintweet:
		if thisword.lower() in scores:                          #for a given tweet, display each word that are also in sent_file
			scoreofthisword = int(scores[str(thisword.lower())])
			scoreoftweet += scoreofthisword
	return scoreoftweet
	
def lines(fp):
	print str(len(fp.readlines()))

def main():
	sent_file = open("c:/DataSciencePython/AFINN-111.txt")       #open(sys.argv[1])
	tweet_file = open("c:/DataSciencePython/output.txt")         #open(sys.argv[2])
    
	alllines_tweet = tweet_file.readlines()
	alllines_sent = sent_file.readlines()
	
	#//////////// 1st step: Create dictionaries ////////////////////////////////////////////
	# Create dict of term w/ score from AFINN-111.txt ////////////////// 
	global scores                                      #global variable across all functions
	scores = {}                                        #initialize a new dict
	for i in range(0, len(alllines_sent)):
		term, score = alllines_sent[i].split("\t")
		scores[term] = int(score)                      #each element of the dict is a term and its score
	
	#create a dict of new words: {'new word',[number of occurrence in positive context, number of occurrence in negative context, total number of tweet in which the new word appears]}
	newwordsentiment = {}
	#/////////////////////////////////////////////////////////////////////////////////////////
	
	for i in range(0, len(alllines_tweet)):
	
	#//////////// 2nd step: Identify each tweet	in output.txt //////////////	
		parsed_line = json.loads(alllines_tweet[i])    # here we convert ith line of output.txt to a dict
		#print parsed_line
		if "text" in parsed_line:
			thistweetnonunicode = parsed_line["text"]
			thistweet = thistweetnonunicode.encode('utf-8')
			
	#//////////// 3rd step: Determine the score of each tweet //////////////
			#print countscoreoftweet(thistweet)   #display the score of the current tweet

	#//////////// 4th step : determine the sentiment of new words ////////////////////////////
	
			#for each word in tweet but not in sent_file:				
			for thisword in thistweet.split():
				thisword = thisword.lower()                       #convert to lower case
				thisword = "".join(c for c in thisword if c not in ('!','.',':',','))	#remove some punctuations

				if thisword not in scores: 
				
					if countscoreoftweet(thistweet) > 0:          #case of a positive tweet
					
						if thisword not in newwordsentiment:      # initialize the list for each new word
							newwordsentiment[thisword] = [0,0,0]
						
						newwordsentiment[thisword][0] += 1     #increment number of occurrence in positive context
						#newwordsentiment[thisword][1] = 0     #number of occurrence in negative context
						newwordsentiment[thisword][2] += 1     #increment total number of tweet in which the new word appears
			
					if countscoreoftweet(thistweet) < 0:           #case of a negative tweet	
					
						if thisword not in newwordsentiment:      # initialize the list for each new word
							newwordsentiment[thisword] = [0,0,0]

						#newwordsentiment[thisword][0] = 0     #number of occurrence in positive context
						newwordsentiment[thisword][1] += 1     #increment number of occurrence in negative context
						newwordsentiment[thisword][2] += 1     #increment total number of tweet in which the new word appears

	for newword in sorted(newwordsentiment):                   #sort the new words by alphabetical order
	
		if newwordsentiment[newword][2] != 0:
			#sentiment = (number of occurrence in positive context - number of occurrence in negative context) / (total number of tweet in which the new word appears)
			sentiment = ( newwordsentiment[newword][0] - newwordsentiment[newword][1] ) / float( newwordsentiment[newword][2] )
			
			if (sentiment != 0) and (sentiment != 1) and (sentiment != -1):
				print newword, round (sentiment, 2) * 10   #, newwordsentiment[newword]
	
	#//////////////////////////////////////////////////////////////////////////////////////////
		
	sent_file.close()
	tweet_file.close()

if __name__ == '__main__':
	main()