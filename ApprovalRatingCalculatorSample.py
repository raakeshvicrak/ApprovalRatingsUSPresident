import nltk;
import pandas as pd;
from nltk import word_tokenize;
from random import randint
from afinn import Afinn
from nltk.tokenize import word_tokenize;

def caluclateRatings():
	dataframe = pd.read_csv("analysis.csv", index_col = None, sep=None, encoding="latin1");
	afinnScorePositiverows = 0;
	customplusafinnScorePositiverows = 0;
	totalrows = dataframe.shape[0];
	for counter in range(0,dataframe.shape[0]):
		afinnScore = dataframe['afinnScore'].iloc[counter];
		customplusafinnScore = dataframe['customplusaffin'].iloc[counter];
		if afinnScore > 0:
			afinnScorePositiverows = afinnScorePositiverows + 1;
		if customplusafinnScore > 0:
			customplusafinnScorePositiverows = customplusafinnScorePositiverows + 1;
	print("The overall approval rating is : "+str((customplusafinnScorePositiverows / totalrows) * 100)+"%");

filePath = input("Enter the file path: ");

dataframe = pd.read_csv(filePath, index_col = None, encoding="latin1");
resultdataframe = pd.DataFrame(columns=('tweetID', 'tweet', 'afinnScore', 'customlexiconscore', 'customplusaffin','userlocation', 'userid', 'statustime'))

positivewordlist = [];
negativewordlist = [];

file = open('positivelexicon.txt', "r");

for line in file:
	positivewordlist.append(line);

file = open('negativelexicon.txt', "r");

for line in file:
	negativewordlist.append(line);

tweetIDlist = [];
afinnScore = [];
tweetlist = [];
customlexiconscore = [];

afinn = Afinn();

for counter in range(0,dataframe.shape[0]):
	 subset = ((int)(counter / 100)) * 1000;
	 tweet = dataframe['tweet'].iloc[counter];
	 tweetID = dataframe['statusid'].iloc[counter];
	 userlocation = dataframe['userlocation'].iloc[counter];
	 userID = dataframe['userid'].iloc[counter];
	 statustime = dataframe['statustime'].iloc[counter];
	 
	 ascore = afinn.score(tweet);
	 
	 score = 0;
	 
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
	 
	 tweetIDlist.append(tweetID);
	 afinnScore.append(ascore);
	 tweetlist.append(tweet);
	 
	 resultdataframe.loc[counter] = [tweetID, tweet, ascore, score, (ascore+score), userlocation, userID, statustime];
	 
filename = 'analysis.csv';
resultdataframe.to_csv(filename, sep=',');

caluclateRatings();


