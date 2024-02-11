# movie price $20, discout: $10
# seniors>=65 youth<=10
# $0 baby<=2

age = int(input("Enter your age: "))
price = 20

if age >= 65 or age <= 10 and age > 2:
    price = 10
elif age <= 2:
    price = 0

print(f"Your ticket price is ${price}")