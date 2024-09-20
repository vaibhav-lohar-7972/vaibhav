# Function to check if a number is prime
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Input: taking a number from the user
num = int(input("Enter a number: "))

# Checking if the number is prime and displaying the result
if is_prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")
