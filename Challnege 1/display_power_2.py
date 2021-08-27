# Display the powers of 2 using anonymous function

# Uncomment code below to take input form the user
terms = int(input("How many terms? "))

# use anonymous function
result = list(map(lambda x: 2 ** x, range(terms)))

print("The total terms are:",terms)
for i in range(terms):
    print("2 rasied to power ", i, " is", result[i])
