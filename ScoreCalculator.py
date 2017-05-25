import nltk;
import pandas as pd;
from nltk import word_tokenize;
from random import randint
from afinn import Afinn
from nltk.tokenize import word_tokenize;

#resultcustomlexicondataframe = pd.DataFrame(data= customlexicondataframe, columns=('customlexiconword', 'lexiconwordscore'));

dataframe = pd.read_csv("/Users/raakeshpremkumar/Documents/Social_Media_Mining/Final_project/Final_Code/updatedTrumpDataset.csv", index_col = None, encoding="latin1");
resultdataframe = pd.DataFrame(columns=('tweetID', 'tweet', 'afinnScore', 'customlexiconscore', 'customplusaffin','userlocation', 'userid', 'statustime'))

positivewordlist = [];
negativewordlist = [];

file = open('/Users/raakeshpremkumar/Documents/positivelexicon.txt', "r");

for line in file:
	positivewordlist.append(line);

file = open('/Users/raakeshpremkumar/Documents/negativelexicon.txt', "r");

for line in file:
	negativewordlist.append(line);

tweetIDlist = [];
afinnScore = [];
tweetlist = [];
customlexiconscore = [];

afinn = Afinn();

print(dataframe['userid'].iloc[0]);

for counter in range(1300000,1350000):
	 subset = ((int)(counter / 100)) * 1000;
	 #randomNum = randint(subset - 1000,subset);
	 tweet = dataframe['tweet'].iloc[counter];
	 tweetID = dataframe['statusid'].iloc[counter];
	 userlocation = dataframe['userlocation'].iloc[counter];
	 userID = dataframe['userid'].iloc[counter];
	 statustime = dataframe['statustime'].iloc[counter];
	 
	 #while tweetID in tweetIDlist:
	 #	counter = randint(subset - 1000,subset);
	 #	tweet = dataframe['tweet'].iloc[counter];
	 #	tweetID = dataframe['statusid'].iloc[counter];
	 
	 ascore = afinn.score(tweet);
	 
	 score = 0;
	 
	 if (counter % 1000) == 0:
	 	print(counter);
	 
	 for positiveword in positivewordlist:
	 	positiveword = positiveword.replace("\n","");
	 	if positiveword != "":
	 		if positiveword.upper() in tweet.upper():
	 			score = score + 1;
	 			
	 for negativeword in negativewordlist:
	 	negativeword = negativeword.replace("\n" , "");
	 	if negativeword != "":
	 		if negativeword.upper() in tweet.upper():
	 			score = score - 1;
	 
	 """tokenize_tweet = word_tokenize(tweet);
	 for tokenize_word in tokenize_tweet:
	 	#print(tokenize_word);
	 	if len(tokenize_word) > 2:
	 		for negativeword in negativewordlist:
		 		if ((tokenize_word in negativeword) and (abs(len(tokenize_word) - len(negativeword)) < 3)):
	 				#print("tokenize " + tokenize_word + " " + negativeword);
	 				score = score - 1;
	 				break;
		 	for positiveword in positivewordlist:
			 	if ((tokenize_word in positiveword) and (abs(len(tokenize_word) - len(positiveword)) < 3)):
	 				score = score + 1;
	 				break;"""
	 
	 tweetIDlist.append(tweetID);
	 afinnScore.append(ascore);
	 tweetlist.append(tweet);
	 
	 resultdataframe.loc[counter] = [tweetID, tweet, ascore, score, (ascore+score), userlocation, userID, statustime];
	 
print(resultdataframe);
filename = '/Users/raakeshpremkumar/Documents/Social_Media_Mining/Final_project/Final_Code/parts_of_analysis/part27.csv';
resultdataframe.to_csv(filename, sep=',');


