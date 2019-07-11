
def duplicate(arr):
	hashtable = {}

	for i in range(0,len(arr)):
		if arr[i] in hashtable:
			print(f"{arr[i]} is the duplicate!")
			return arr[i]
		else:
			hashtable[arr[i]] = arr[i]
			

	print("No Duplicates Found!")






if __name__ == "__main__":
	arr = [1,3,4,2,2]
	duplicate(arr)