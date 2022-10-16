#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6

#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

total_bill = input("""welcome to the tip calculator!
what was the total bill? $""")
tip = input("""how much tip would you like to give? 10, 12, or 15? """)
people = input("""how many people to split the bill? """)
split = float(total_bill) / int(people)
tips = int(tip) / 100 + 1
split_tips = float(tips) * float(split)
pre_result = round(split_tips, 2)
result = print(f"Each person should pay: $" + str(pre_result))
