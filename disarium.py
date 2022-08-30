n = input('Enter an integer number: ')
allDigits = sum(int(n[i])**(i+1) for i in range(len(n)))
if int(n) == allDigits: print(f'{n} is a disarium number.') 
else: print(f'{n} is not a disarium number.') 
