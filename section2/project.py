print('Welcome to the Tip Calculator!')
bill = float(input('What was the total bill price? '))
tip = int(input('How much tip would you like to give? 10, 12, or 15? ')) / 100
num_people = int(input('How many people to split the bill?'))

total = bill + (bill * tip)
print(total)
price_per_person = total / num_people

print('Each person should pay: ${0:.2f}'.format(price_per_person))