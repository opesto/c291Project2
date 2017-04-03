#writes the organized data in lists to 3 files terms.txt, dates.txt, and tweets.txt
def writeToFiles(termsList, datesList, tweetsList):
	file1 = open("terms.txt", 'a')
	for term in termsList:
		file1.writelines(term+"\n")
	file1.close()

	file2 = open("dates.txt", 'a')
	for date in datesList:
		file2.write(date+"\n")
	file2.close()

	file3 = open("tweets.txt", 'a')
	for tweet in tweetsList:
		file3.write(tweet+"\n")
	file3.close()

def writeOne(fp, term):
	fp.write(term+"\n")

#recursively checks a string for certain illegal term characters such as:
#!@#$%^&*()+?/ and seperates the string into multiple strings at the index 
#of the illegal character. The string/strings are then added to termsList.
def addTerm(termsList, termgroup, prefix, charsId, fp): 
	
	if "&#" in termgroup and ";" in termgroup:
		if termgroup[termgroup.index("#")+1:termgroup.index(";")].isdigit():
			addTerm(termsList, termgroup[:termgroup.index("#")-1], prefix, charsId, fp)
			addTerm(termsList, termgroup[termgroup.index(";")+1:], prefix, charsId, fp)
		else:
			addTerm(termsList, termgroup, prefix, charsId, fp)
	elif "." in termgroup:
		index = termgroup.index(".")
		if index != 0:
			addTerm(termsList, termgroup[:index], prefix, charsId, fp)
		if index != len(termgroup) - 1:
			addTerm(termsList, termgroup[index+1:], prefix, charsId, fp)
	elif "," in termgroup:
		index = termgroup.index(",")
		if index != 0:
			addTerm(termsList, termgroup[:index], prefix, charsId, fp)
		if index != len(termgroup) - 1:
			addTerm(termsList, termgroup[index+1:], prefix, charsId, fp)
	elif "!" in termgroup:
		index = termgroup.index("!")
		if index != 0:
			addTerm(termsList, termgroup[:index], prefix, charsId, fp)
		if index != len(termgroup) - 1:
			addTerm(termsList, termgroup[index+1:], prefix, charsId, fp)
	elif "@" in termgroup:
		index = termgroup.index("@")
		if index != 0:
			addTerm(termsList, termgroup[:index], prefix, charsId, fp)
		if index != len(termgroup) - 1:
			addTerm(termsList, termgroup[index+1:], prefix, charsId, fp)
	elif "#" in termgroup:
		index = termgroup.index("#")
		if index != 0:
			addTerm(termsList, termgroup[:index], prefix, charsId, fp)
		if index != len(termgroup) - 1:
			addTerm(termsList, termgroup[index+1:], prefix, charsId, fp)
	elif "$" in termgroup:
		index = termgroup.index("$")
		if index != 0:
			addTerm(termsList, termgroup[:index], prefix, charsId, fp)
		if index != len(termgroup) - 1:
			addTerm(termsList, termgroup[index+1:], prefix, charsId, fp)
	elif "%" in termgroup:
		index = termgroup.index("%")
		if index != 0:
			addTerm(termsList, termgroup[:index], prefix, charsId, fp)
		if index != len(termgroup) - 1:
			addTerm(termsList, termgroup[index+1:], prefix, charsId, fp)
	elif "^" in termgroup:
		index = termgroup.index("^")
		if index != 0:
			addTerm(termsList, termgroup[:index], prefix, charsId, fp)
		if index != len(termgroup) - 1:
			addTerm(termsList, termgroup[index+1:], prefix, charsId, fp)
	elif "&" in termgroup:
		index = termgroup.index("&")
		if index != 0:
			addTerm(termsList, termgroup[:index], prefix, charsId, fp)
		if index != len(termgroup) - 1:
			addTerm(termsList, termgroup[index+1:], prefix, charsId, fp)
	elif "*" in termgroup:
		index = termgroup.index("*")
		if index != 0:
			addTerm(termsList, termgroup[:index], prefix, charsId, fp)
		if index != len(termgroup) - 1:
			addTerm(termsList, termgroup[index+1:], prefix, charsId, fp)
	elif "(" in termgroup:
		index = termgroup.index("(")
		if index != 0:
			addTerm(termsList, termgroup[:index], prefix, charsId, fp)
		if index != len(termgroup) - 1:
			addTerm(termsList, termgroup[index+1:], prefix, charsId, fp)
	elif ")" in termgroup:
		index = termgroup.index(")")
		if index != 0:
			addTerm(termsList, termgroup[:index], prefix, charsId, fp)
		if index != len(termgroup) - 1:
			addTerm(termsList, termgroup[index+1:], prefix, charsId, fp)
	elif "?" in termgroup:
		index = termgroup.index("?")
		if index != 0:
			addTerm(termsList, termgroup[:index], prefix, charsId, fp)
		if index != len(termgroup) - 1:
			addTerm(termsList, termgroup[index+1:], prefix, charsId, fp)
	elif "+" in termgroup:
		index = termgroup.index("+")
		if index != 0:
			addTerm(termsList, termgroup[:index], prefix, charsId, fp)
		if index != len(termgroup) - 1:
			addTerm(termsList, termgroup[index+1:], prefix, charsId, fp)
	elif "/" in termgroup:
		index = termgroup.index("/")
		if index != 0:
			addTerm(termsList, termgroup[:index], prefix, charsId, fp)
		if index != len(termgroup) - 1:
			addTerm(termsList, termgroup[index+1:], prefix, charsId, fp)
	elif ";" in termgroup:
		index = termgroup.index(";")
		if index != 0:
			addTerm(termsList, termgroup[:index], prefix, charsId, fp)
		if index != len(termgroup) - 1:
			addTerm(termsList, termgroup[index+1:], prefix, charsId, fp)
	elif "'" in termgroup:
		index = termgroup.index("'")
		if index != 0:
			addTerm(termsList, termgroup[:index], prefix, charsId, fp)
		if index != len(termgroup) - 1:
			addTerm(termsList, termgroup[index+1:], prefix, charsId, fp)
	elif ":" in termgroup:
		index = termgroup.index(":")
		if index != 0:
			addTerm(termsList, termgroup[:index], prefix, charsId, fp)
		if index != len(termgroup) - 1:
			addTerm(termsList, termgroup[index+1:], prefix, charsId, fp)
	else:
		if len(termgroup) > 2:
			#termsList.append(prefix+termgroup.lower()+":"+charsId)
			writeOne(fp, prefix + termgroup.lower() + ":" + charsId)
			
def main():
	termsList = []
	datesList = []
	tweetsList = []
	fname = input("File to open: ")
	file = open(fname, "r")
	file1 = open("terms.txt", 'a')
	file2 = open("dates.txt", 'a')
	file3 = open("tweets.txt", 'a')
	for line in file:
		lineList = line.split()
		if (len(lineList) >= 4):
			charsId = lineList[1][4:13]

			#create terms.txt file
			#add text terms to termsList
			for wordIndex in range(len(lineList)):
				if wordIndex > 2:
					if lineList[wordIndex][-7:] == "</text>":
						addTerm(termsList, lineList[wordIndex][:-7], "t-", charsId, file1)
						break

					if len(lineList[wordIndex]) > 2:
						if wordIndex == 3:
							addTerm(termsList, lineList[wordIndex][6:], "t-", charsId, file1)
						else:
							addTerm(termsList, lineList[wordIndex], "t-", charsId, file1)

			#add name terms to termsList
			add = False
			for wordIndex in range(len(lineList)):
				if lineList[wordIndex][:6] == "<name>":
					add = True
					addTerm(termsList, lineList[wordIndex][6:], "n-", charsId, file2)
				elif lineList[wordIndex][-7:] == "</name>":
					addTerm(termsList, lineList[wordIndex][:-7], "n-", charsId, file2)
					add = False
					break
				else:
					if add:
						addTerm(termsList, lineList[wordIndex], "n-", charsId, file2)

			#add location terms to termsList
			add = False
			for wordIndex in range(len(lineList)):
				if lineList[wordIndex][:10] == "<location>":
					add = True
					addTerm(termsList, lineList[wordIndex][10:], "l-", charsId, file3)
				elif lineList[wordIndex][-11:] == "</location>":
					addTerm(termsList, lineList[wordIndex][:-11], "l-", charsId, file3)
					add = False
					break
				else:
					if add:
						addTerm(termsList, lineList[wordIndex], "l-", charsId, file3)

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
		
main()
		
