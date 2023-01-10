count = 0
sum = 0
full_name = input("Enter Full Name: ").title()
min_price = float(input("Enter Min Price: "))
price_list = [42.0, 69.6, 12.3, 77.7, 101.1, 99.9, 88.4]
for price in price_list:
    sum += price
    if price> min_price:
        count += 1
print("Hello, the minimum price is ", end="")
print(min_price)
print("There are ", end="" )
print(count, end=" ")
print("prices greater than the minimum price")

print("The total price is ", end=" ")
print(sum)