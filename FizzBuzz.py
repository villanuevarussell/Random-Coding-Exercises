'''
A script that prints niumbers from 1 to n with the following rules below
Rules:
1.Multiples of 3 prints "Fizz" instead of the number
2.Multples of 5 print Buzz instead of number
3.Multiples of both 3 and 5 print Fizz Buzz

'''

def FizzBuzz(n):
	for number in range(1,n+1):
		if number % 15 == 0:
			print('FizzBuzz')
		elif number % 3 == 0:
			print('Fizz')
		elif number % 5 == 0:
			print('Buzz')
		else:
			print(number)


#Test Cases
if __name__ == "__main__":
	FizzBuzz(100)
	FizzBuzz(200)
	FizzBuzz(50)