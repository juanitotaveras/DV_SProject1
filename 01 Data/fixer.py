
def main():
#	inFile = open ("./Gallups_Most_Important_Problem.csv", "r")
#	outFile = open("./Gallups_test.csv", "w")
	inFile = open ("./Public_Laws.csv", "r")
	outFile = open ("./Public_Laws_reformatted.csv", "w")
	topics = {1:"Macroeconomics", 2:"Civil Rights", 3:"Health", 4:"Agriculture", 5:"Labor", 6:"Education", 7:"Environment", 8:"Energy", 9:"Immigration", 10:"Transportation", 12:"Crime", 13:"Social Welfare", 14:"Housing & Development", 15:"Domestic Commerce", 16:"Defense", 17:"Science & Technology", 18:"Foreign Trade", 19:"International Affairs", 20:"Government Operations", 21:"Public Lands", 25:"Don't Know/Other"}

	first = inFile.readline()
	line1 = first.split(",")
	m = 0
	check = False
	while check == False:
		if (line1[m] != "MajorTopic") and (m < len(line1)):
			m += 1
		else:
			check = True
	# m is now equal to the index of Major Topic
	outFile.write(first)

	for line in inFile:
		line2 = line.split(",")
		newline = ""	
		if int(line2[m]) in topics:
			top = topics[int(line2[m])]
			st = ""
			for i in range (0, (len(line2) - 1)):
				if i == m:
					st += top + ","
				else:
					st += line2[i] + ","
			st += line2[i + 1]
		else:	
			st = ""
			for i in range (0, (len(line2)-1)):	
				if i == m:
					st += "N/A" + ","
				else:
					st += line2[i] + ","
			st += line2[i + 1]
		newline = st			 
		outFile.write(newline) 
		print("old line: " + line)
		print ("new line: " + newline)

	inFile.close()
	outFile.close()
	
main()
