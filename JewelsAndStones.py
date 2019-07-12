'''
This program tells you how many jewels are in a string of stones.
The first parameter are the characters that are jewels
The second parameter is list of stones.
The program compares each stone if it is a Jewel and returns the number of jewels in the string
'''

def JewelsAndStones(j,s):
	'''
	#Using a Hash Map
	#Different types of stones
	Jewels = {}
	jewelcount = 0

	#splits into a list
	j = list(j)
	#puts each jewel into a table
	for jewel in j:
		Jewels[jewel] = jewel

	for stones in s:
		if stones in Jewels:
			jewelcount += 1

	return jewelcount

	'''

	#Quicker way to do this
	jewelcount = 0

	for stones in s:
		if stones in j:
			jewelcount += 1


	return jewelcount
	
	

#Test Cases
if __name__ == "__main__":
	print(JewelsAndStones("aA","aAAbbbb"))#Output = 3
	print(JewelsAndStones("z","ZZ"))#Output = 0
	print(JewelsAndStones("ABCDE","aAAbbbaAbAAAbBcdEEC"))#Output = 10

