import os
import re

#writes the organized data in lists to 3 files terms.txt, dates.txt, and tweets.txt
def writeToFiles(termsList, datesList, tweetsList):
	file2 = open("dates.txt", 'a')
	for date in datesList:
		file2.write(date+"\n")
	file2.close()

	file3 = open("tweets.txt", 'a')
	for tweet in tweetsList:
		file3.write(tweet+"\n")
	file3.close()

def writeOne(fp, term):
	fp.writelines(term+"\n")

def parse(fp, line, prefix, charsId):
	terms = re.split('[^a-zA-Z0-9]', line)
	if '&#' in line and ';' in line:
		if line[line.index('#')+1:line.index(';')].isdigit():
			terms.remove(line[line.index('#')+1:line.index(';')])
	for term in terms:
		if len(term) > 2:
			writeOne(fp, prefix + term.lower() + ":" + charsId)

def main():
	termsList = []
	datesList = []
	tweetsList = []
	fname = input("File to open: ")
	file = open(fname, "r")
	if os.path.isfile("terms.txt"):
		os.remove("terms.txt")
	file1 = open("terms.txt", 'a')
	if os.path.isfile("terms.txt"):
		os.remove("dates.txt")
	file2 = open("dates.txt", 'a')
	if os.path.isfile("tweets.txt"):
		os.remove("tweets.txt")
	file3 = open("tweets.txt", 'a')
	for line in file:
		lineList = line.split()
		if (len(lineList) >= 4):
			charsId = lineList[1][4:13]
			#	def parse(fp, line, prefix, charsId):
			#create terms.txt file
			#add text terms to termsList
			for wordIndex in range(len(lineList)):
				if wordIndex > 2:
					if lineList[wordIndex][-7:] == "</text>":
						#addTerm(termsList, lineList[wordIndex][:-7], "t-", charsId, file1)
						parse(file1, lineList[wordIndex][:-7], "t-", charsId) 
						break

					if len(lineList[wordIndex]) > 2:
						if wordIndex == 3:
							#addTerm(termsList, lineList[wordIndex][6:], "t-", charsId, file1)
							parse(file1, lineList[wordIndex][6:], "t-", charsId) 
						else:
							#addTerm(termsList, lineList[wordIndex], "t-", charsId, file1)
							parse(file1, lineList[wordIndex], "t-", charsId) 

			#add name terms to termsList
			add = False
			for wordIndex in range(len(lineList)):
				if lineList[wordIndex][:6] == "<name>":
					add = True
					#addTerm(termsList, lineList[wordIndex][6:], "n-", charsId, file2)
					parse(file1, lineList[wordIndex][6:], "n-", charsId) 
				elif lineList[wordIndex][-7:] == "</name>":
					#addTerm(termsList, lineList[wordIndex][:-7], "n-", charsId, file2)
					parse(file1, lineList[wordIndex][:-7], "n-", charsId) 
					add = False
					break
				else:
					if add:
						#addTerm(termsList, lineList[wordIndex], "n-", charsId, file2)
						parse(file1, lineList[wordIndex], "n-", charsId) 

			#add location terms to termsList
			add = False
			for wordIndex in range(len(lineList)):
				if lineList[wordIndex][:10] == "<location>":
					add = True
					#addTerm(termsList, lineList[wordIndex][10:], "l-", charsId, file3)
					parse(file1, lineList[wordIndex][10:], "l-", charsId) 
				elif lineList[wordIndex][-11:] == "</location>":
					#addTerm(termsList, lineList[wordIndex][:-11], "l-", charsId, file3)
					parse(file1, lineList[wordIndex][:-11], "l-", charsId) 
					add = False
					break
				else:
					if add:
						#addTerm(termsList, lineList[wordIndex], "l-", charsId, file3)
						parse(file1, lineList[wordIndex], "l-", charsId) 

			#create dates.txt file
			charsDate = []
			for charIndex in range(len(lineList[2])):
				if charIndex > 11 and charIndex < 22:
					charsDate.append(lineList[2][charIndex])

			dateString = ""
			for char in charsDate:
				dateString = dateString+char
			dateString = dateString+":"+charsId
			datesList.append(dateString)


			#create tweets.txt file
			tweetString = charsId
			tweetString = tweetString + ":"
			tweetString = tweetString + line[:-1]
			tweetsList.append(tweetString)

	file.close()
	file1.close()
	file2.close()
	file3.close()
	writeToFiles(termsList, datesList, tweetsList)
		
main()
		
