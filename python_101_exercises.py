# Raymond Yang

# 1. Hello, you!

username1 = input("Enter your name: ")
print(f"Hello, {username1}!")

# 2. HELLO, YOU!

username2 = input("ENTER YOUR NAME: ").upper()
print(f"HELLO, {username2}! YOUR NAME HAS {len(username2)} LETTERS IN IT! RADICAL!")

# 3. Madlib

print("_(best sport)_ is the best sport in the world!  It's way better than _(worst sport)_!")
bestSport = input("The best sport is obviously: ")
worstSport = input("The worst sport is obviously: ")
print(f"{bestSport} is the best sport in the world!  It's way better than {worstSport}!")

# 4. Day of the Week

day = int(input(Enter the day of the week (0 to 6): ))

if day == 0:
    print("Today is Sunday.")
elif day == 1:
    print("Today is Monday.")
elif day == 2:
    print("Today is Tuesday.")
elif day == 3:
    print("Today is Wednesday.")
elif day == 4:
    print("Today is Thursday.")
elif day == 5:
    print("Today is Friday.")
elif day == 6:
    print("Today is Saturday.")
else:
    print("That's not a choice, you dingus.")

# 5. Work or Sleep In?

day = int(input(Enter the day of the week (0 to 6): ))

if 1 <= day <= 5:
    print("Go to work!")
elif day == 0 or day == 6:
    print("Sleep in.")

# 6. Celsius to Fahrenheit

Celsius = input("Enter the temperature in degrees Celsius: ")
Fahrenheit = Celsius * 1.8 + 32
print(f"The temperature in Fahrenheit is {Fahrenheit}.)

# 7. Tip Calculator

bill = input("Enter the total bill amount: ")
service = input("How was the level of service (good, fair or bad)? ")
if service == "good":
    print(f"Tip amount: {bill * 0.2} \nTotal amount: {bill + bill * 0.2}")
elif service == "fair":
    print(f"Tip amount: {bill * 0.15} \nTotal amount: {bill + bill * 0.15}")
elif service == "bad":
    print(f"Tip amount: {bill * 0.1} \nTotal amount: {bill + bill * 0.1}")