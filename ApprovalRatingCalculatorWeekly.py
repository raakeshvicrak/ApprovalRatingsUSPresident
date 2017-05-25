import MySQLdb as db;

con = db.connect('localhost', 'root', 'root', 'sys');

cursor = con.cursor();

date = 2;

while date <= 29:
	if date < 10:
		if (date+6) < 10:
			countallquery = "SELECT count(*) FROM tweetdataset77AffinCustom where statustime BETWEEN '2017-04-0"+ str(date) +" 00:00:00' AND '2017-04-0"+ str(date+6) +" 23:59:59';"
			positivecountquery = "SELECT count(*) FROM tweetdataset77AffinCustom where statustime BETWEEN '2017-04-0"+ str(date) +" 00:00:00' AND '2017-04-0"+ str(date+6) +" 23:59:59' and customplusaffin > 0;"
			positivecountqueryaffinonly = "SELECT count(*) FROM tweetdataset77AffinCustom where statustime BETWEEN '2017-04-0"+ str(date) +" 00:00:00' AND '2017-04-0"+ str(date+6) +" 23:59:59' and afinnScore > 0;"
		else:
			countallquery = "SELECT count(*) FROM tweetdataset77AffinCustom where statustime BETWEEN '2017-04-0"+ str(date) +" 00:00:00' AND '2017-04-"+ str(date+6) +" 23:59:59';"
			positivecountquery = "SELECT count(*) FROM tweetdataset77AffinCustom where statustime BETWEEN '2017-04-0"+ str(date) +" 00:00:00' AND '2017-04-"+ str(date+6) +" 23:59:59' and customplusaffin > 0;"
			positivecountqueryaffinonly = "SELECT count(*) FROM tweetdataset77AffinCustom where statustime BETWEEN '2017-04-0"+ str(date) +" 00:00:00' AND '2017-04-"+ str(date+6) +" 23:59:59' and afinnScore > 0;"
	else:
		countallquery = "SELECT count(*) FROM tweetdataset77AffinCustom where statustime BETWEEN '2017-04-"+ str(date) +" 00:00:00' AND '2017-04-"+ str(date+6) +" 23:59:59';"	
		positivecountquery = "SELECT count(*) FROM tweetdataset77AffinCustom where statustime BETWEEN '2017-04-"+ str(date) +" 00:00:00' AND '2017-04-"+ str(date+6) +" 23:59:59' and customplusaffin > 0;"
		positivecountqueryaffinonly = "SELECT count(*) FROM tweetdataset77AffinCustom where statustime BETWEEN '2017-04-"+ str(date) +" 00:00:00' AND '2017-04-"+ str(date+6) +" 23:59:59' and afinnScore > 0;"

	cursor.execute(countallquery);
	#print(countallquery);
	
	totalrows = 0;
	positiverows = 0;
	positiverowsaffinonly = 0;
	
	for row in cursor:
		totalrows = row[0];
	
	cursor.execute(positivecountquery);
	
	for row in cursor:
		positiverows = row[0];
	
	approvalrating = 0;
	if totalrows != 0:	
		approvalrating = (positiverows / totalrows) * 100;
	
	cursor.execute(positivecountqueryaffinonly);
	
	for row in cursor:
		positiverowsaffinonly = row[0];
	
	approvalratingaffinonly = 0;
	if totalrows != 0:
		approvalratingaffinonly = (positiverowsaffinonly / totalrows) * 100;
	
	if date < 10:
		if approvalrating > 0:
			print("The approval rating from 2017-04-0" + str(date)+" until 2017-04-"+ str(date+6) +" : " + str(approvalrating) + "%");
	else:
		if approvalrating > 0:
			print("The approval rating from 2017-04-" + str(date)+" until 2017-04-"+ str(date+6) +" : " + str(approvalrating) + "%");
	date = date + 7;