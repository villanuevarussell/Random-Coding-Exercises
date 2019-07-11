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
		print(word1)
		print(word2)

		if not word1 and not word2:
			return True
		else:
			return False

if __name__ == "__main__":
	anagram = Solution()

	print(anagram.isAnagram('racecare', 'crrecare'))