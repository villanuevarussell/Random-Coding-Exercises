'''This code takes in a string and follows the rules of goat latin and outputs the string
Rules:
1.If a vowel appears as the first letter of the word, add ma to the end of the word
2.If a consonant appears as the first letter of the word, move the first letter of the word to the end then add ma
3.Add a letter 'a' to the end of each word per it's index. example: helloa howaa areaaa youaaaa doingaaaa
'''

import string
def toGoatLatin(string):
	#splits the string into separate words
	string = string.split()
	#a list that will hold the new words
	goatLatin = []
	#list of vowels
	vowels = "aAeEiIoOuU"
	#count which will be used to increase the number of 'a's for each word that it loops through
	count = 'a'
	#if it is a vowel it adds ma plus the extra a, then adds another 'a' to count
	for word in string:
		if word[0] in vowels:
			goatLatin.append(word+'ma'+count)
			count = count + 'a'

#if not a vowel moves first letter to front of word, adds ma and count, and adds another 'a' to count
		else:
			frontofword = word[1:]
			endofword = f"{word[0].lower()}ma"
			goatLatin.append(frontofword+endofword[0]+count)
			count = count + 'a'
#joins list and returns string
	return " ".join(goatLatin)

	



#Test Cases
if __name__ == "__main__":
	print(toGoatLatin('Hello Friend How are you doing today'))
	print(toGoatLatin('The cow jumped over the moon'))
	print(toGoatLatin('Coding exercises are fun'))




