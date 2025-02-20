# Simple Python script to calculate age in 5 years

def main():
    # Ask for user input
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    # Calculate the age in 5 years
    future_age = age + 5

    # Print the result
    print(f"Hello {name}! In 5 years, you will be {future_age} years old.")

if __name__ == "__main__":
    main()
