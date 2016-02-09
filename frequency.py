import sys
import json

def main():
	tweet_file = open("c:/DataSciencePython/output.txt")         #open(sys.argv[2])
    
	alllines_tweet = tweet_file.readlines()

	#create a dict of all words in the tweet in output.txt: {'word',[number of occurrence of that word in all tweets])
	allwordsintweet = {}
	#/////////////////////////////////////////////////////////////////////////////////////////
	
	for i in range(0, len(alllines_tweet)):
	
	#//////////// Identify each tweet	in output.txt //////////////	
		parsed_line = json.loads(alllines_tweet[i])    # here we convert ith line of output.txt to a dict
		#print parsed_line
		if "text" in parsed_line:
			thistweetnonunicode = parsed_line["text"]
			thistweet = thistweetnonunicode.encode('utf-8')
			
	#///////////////////////// Determine the frequency of words ////////////////////////////
						
			for thisword in thistweet.split():                    #for each word in tweet:
				thisword = thisword.lower()                       #convert to lower case
				thisword = "".join(c for c in thisword if c not in ('!','.',':',',','"'))	#remove some punctuations

				if thisword not in allwordsintweet:
					allwordsintweet[thisword] = 1
				else:
					allwordsintweet[thisword] += 1
				
	for thisword in sorted(allwordsintweet):                   #sort all words in all tweets, by alphabetical order 
		
		#if (thisword[:1] != "@") and (thisword[:1] != "#") and (thisword[:4] != "http"):
		#if thisword[:1] in list("azertyuiopqsdfghjklmwxcvbn"):
		occurrenceinalltweets = allwordsintweet[thisword]      # number of occurrences of the term in all tweets
		occurrenceofalltermsinalltweet = len(allwordsintweet)  # number of occurrences of all terms in all tweets
		frequency = round ( occurrenceinalltweets / float(occurrenceofalltermsinalltweet) , 4)
		#frequency = [# of occurrences of the term in all tweets]/[# of occurrences of all terms in all tweets]
		if frequency > (0.5 / 100) :                           #display all terms with a frequency > 0.5%
			print thisword, round ( occurrenceinalltweets / float(occurrenceofalltermsinalltweet) , 5)

	tweet_file.close()

if __name__ == '__main__':
	main()