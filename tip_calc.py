# 7. Tip Calculator

bill = input("Enter the total bill amount: ")
service = input("How was the level of service (good, fair or bad)? ")
if service == "good":
    print(f"Tip amount: {bill * 0.2} \nTotal amount: {bill + bill * 0.2}")
elif service == "fair":
    print(f"Tip amount: {bill * 0.15} \nTotal amount: {bill + bill * 0.15}")
elif service == "bad":
    print(f"Tip amount: {bill * 0.1} \nTotal amount: {bill + bill * 0.1}")