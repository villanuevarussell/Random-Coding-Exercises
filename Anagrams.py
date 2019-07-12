'''
This Solution class has a function that takes two strings and returns 
'True' or 'False' based on if it is an anagram or not


big O:
Time:
O(n^2)
Space:
O(n)

'''

class Solution:
	def isAnagram(self, s: str, t: str) -> bool:
		#splits words into 2
		word1 = list(s)
		word2 = list(t)

		#if length of words not equal, it isn't an anagram
		if not len(s) == len(t):
			return False

		#loops through all combinations and from both if they exist 
		for x in word1[:]:
			deleteflag = False
			for y in word2[:]:
				if x == y:
					word2.remove(y)#deletes from y matching characters
					deleteflag = True#triggers delete flag for x
					break
			if deleteflag == True:#removes from x because x also contains that char
				word1.remove(x)

		#if word 1 and word 2 is empty returns True if not empty return false
		if not word1 and not word2:
			return True
		else:
			return False

#Test cases
if __name__ == "__main__":
	anagram = Solution()

	print(anagram.isAnagram('racecare', 'crrecare'))#expected Output False
	print(anagram.isAnagram('racecare', 'carecare'))#expected Output True
	print(anagram.isAnagram('racecare', 'hello'))#expected Output False since word is not same length
	print(anagram.isAnagram('anagram', 'gramana'))#expected Output True