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

	#//////////// Create a dictionary of term w/ score from AFINN-111.txt ////////////////// 
	global scores                                      #global variable across all functions
	scores = {}                                        #initialize a new dict
	for i in range(0, len(alllines_sent)):
		term, score = alllines_sent[i].split("\t")
		scores[term] = int(score)                      #each element of the dict is a term and its score

		
	for i in range(0, len(alllines_tweet)):
		parsed_line = json.loads(alllines_tweet[i])    # here we convert ith line of output.txt to a dict
		#print parsed_line
		if "text" in parsed_line:
			getatweet = parsed_line["text"]
			getatweetunicode = getatweet.encode('utf-8')
			#print getatweetunicode
			print countscoreoftweet(getatweetunicode)   #display the score of the current tweet

			
    #lines(sent_file)
    #lines(tweet_file)
	sent_file.close()
	tweet_file.close()

if __name__ == '__main__':
	main()