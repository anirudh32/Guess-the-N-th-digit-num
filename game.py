import random

t=int(input("how many digit number do you want to guess: "))
num = random.randrange(int('1'+(t-1)*'0'), int('1'+t*'0'))

n = int(input("Guess the "+str(t)+" digit number:"))
while(len(str(n))!=t):
        print("the entered digit isn't a",t,"digit number")
        n=int(input("Guess the "+str(t)+" digit number:"))
if (n == num):
	print("Great! You guessed the number in just 1 try! You're a amazing!")
else:
	ctr = 0

	while (n != num):
		
		ctr += 1

		count = 0


		n = str(n)
		num = str(num)

		
		correct = ['X']*t

		
		for i in range(t):

			
			if (n[i] == num[i]):
				
				count += 1
				
				correct[i] = n[i]
			else:
				continue

		if (count < t) and (count != 0):
			print("Not quite the number. But you did get ", count, " digit(s) correct!")
			print("Also these numbers in your input were correct.")
			for k in correct:
				print(k, end=' ')
			print('\n')
			print('\n')
			n = int(input("Enter your next choice of numbers: "))
			while(len(str(n))!=t):
			    print("the entered digit isn't a",t,"digit number")
			    n = int(input("Enter your next choice of numbers: "))
                

		
		elif (count == 0):
			print("None of the numbers in your input match.")
			n = int(input("Enter your next choice of numbers: "))
			while(len(str(n))!=t):
			    print("the entered digit isn't a",t,"digit number")
			    n = int(input("Enter your next choice of numbers: "))
	if n == num:
		if ctr<10:
		    print("Great! You guessed the number in just",ctr,"tries")
		else:
		    print("Great! But You guessed the number in",ctr,"tries")

