'''
Takes in  string and prints out the longest word, punctuations is not included
'''
import string

def LongestWord(sen): 
	#creates a string of all punctions for comparison
	punctuations = "".join(string.punctuation)
	#new strong to remove punctuations
	newstring = ""


	#loop to first remove punctuations from string, if char is in puncations,
	#it skips, if it isn't it adds it to newstring
	for s in sen:
		if s in punctuations:
			pass
		else:
			newstring = newstring + s

	#splits string into a list
	newstring = newstring.split()
	
	#Makes first word in list the current longest word
	longword = newstring[0]

	#iterates through list 
	for word in newstring[1:]:
		#if the len of the current longest word is less than the current word being iterated it makes that the longest word
		if len(longword) < len(word):

			longword = word
	#returns longestword string
	return longword


#Test Cases
if __name__ == "__main__":
	print(LongestWord("Hello Friend"))#Expected Output = Friend
	print(LongestWord("fun#!*!( times"))#Expected Output = times
	print(LongestWord("hel!(!@(*@lo friend super!)!)#*(@#*(#@*@) supercagu@@@!)!)raglistic"))#Expected Output = supercaguraglistic

