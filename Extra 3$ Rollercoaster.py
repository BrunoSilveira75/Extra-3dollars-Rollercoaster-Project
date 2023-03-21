height = 120
less12 = 5
price_12to18 = 7
price_above18 = 12

height_user = int(input("Type your height in cm: "))

if height_user <= 119:
    print("You are not allowed to ride because of your height")
else:
    age = int(input("Type your age: "))
    if age > 18:
        bill = 12
        print("Adults tickets are $12.")
    elif age >= 12 or age == 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 5
        print("Children tickets are $5.")

photo = input("\nDo you want a photo?\n 1- You want a photo.\n 2 - You don't want a photo. \nType here:  ")
photo = photo.upper()
if photo == "S":
    result = bill + 3
    print(f"You have to pay ${result} dollars")
else:
    print(f"You're total is ${bill}")
