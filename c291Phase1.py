file = open("10Records.xml", "r")
for line in file:
	lineList = line.split()
	if (len(lineList) >= 4):
		charsId = []
		for charIndex in range(len(lineList[1])):
			if charIndex > 3 and charIndex < 13:
				charsId.append(lineList[1][charIndex])

		#create terms.txt file
		termsList = []
		for wordIndex in range(len(lineList)):
			if wordIndex > 2:
				if lineList[wordIndex][-7:] == "</text>":
					termsList.append(lineList[wordIndex][:-7])
					break

				if len(lineList[wordIndex]) > 2:
					if wordIndex == 3:
						termsList.append(lineList[wordIndex][6:])
					else:
						termsList.append(lineList[wordIndex])
		
		for wordIndex in range(len(termsList)):
			termsList[wordIndex] = termsList[wordIndex]+":"
			for char in charsId:
				termsList[wordIndex] = termsList[wordIndex]+char

		for term in termsList:
			print(term)
		

		#create dates.txt file
		datesList = []
		charsDate = []
		for charIndex in range(len(lineList[2])):
			if charIndex > 11 and charIndex < 22:
				charsDate.append(lineList[2][charIndex])


		dateString = ""
		for char in charsDate:
			dateString = dateString+char
		dateString = dateString+":"
		for char in charsId:
			dateString = dateString+char
		datesList.append(dateString)
		#print(dateString)

		#create tweets.txt file
		tweetsList = []
		tweetString = ""
		for char in charsId:
			tweetString = tweetString+char
		tweetString = tweetString + ":"
		tweetString = tweetString + line
		tweetsList.append(tweetString)
		#print(tweetString)

file.close()
		

	
			
		
