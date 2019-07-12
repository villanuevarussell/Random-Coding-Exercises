'''
This script takes in list of numbers and checks to see if there are any duplicates within them.
If there are duplicates in the list it saves it to duplicate dictionary
After looping through entire array, it outputs a list of the values of the dictionary


Space Complexity: O(n)
Time Complexity: O(n)

'''

def duplicate(arr):
	hashtable = {}
	duplicates = {}
	#loops through array
	for i in arr:
		#if i in hashtable it adds it to duplicates dictionary
		if i in hashtable:
			print(f"{i} is the duplicate!")
			duplicates[i] = i
		#else it adds it to hash table for comparison
		else:
			hashtable[i]= i
	#if duplicate is empty prints no duplicates found and the empty dictionary
	if not duplicates:
		print("No Duplicates Found!")
		return list(duplicates.values())
	#return a list of duplicate values
	else:
		return list(duplicates.values())



#Test Cases
if __name__ == "__main__":
	arr = [1,3,4,2,2,4,3,10,8,17,4,2]
	print(duplicate(arr))#expected output 2,4,3
	arr = [10,10,10,2,2,2,4,4,4,10,8,18,109,109]
	print(duplicate(arr))#expected output 10,2,4,109	
	arr = [1,2,3,4,5,6,7]
	print(duplicate(arr))#expected output Empty