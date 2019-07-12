'''
This program takes in a list of numbers and finds the max difference all the numbers in the list and outputs that integer.
example: Input: [2,3,10,6,4,8,1], Output: 9
'''

def MaxDifference(numbers):
#creates a copy of the array
	numberscopy = numbers.copy()
	absolute = 0
#this nested loop is to go through all possible combinations by comparing list of numbers to the copy we made
	for x in numbers:
		for y in numberscopy:
#if absolute is greater it becomes the new absolute
			if abs(x-y) > absolute:
				absolute = abs(x-y)
				
	return absolute



#Test Cases
if __name__ == "__main__":
	numbers = [2,3,10,6,4,8,1]
	print(MaxDifference(numbers))