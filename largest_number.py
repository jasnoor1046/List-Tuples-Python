# Function definitions
def find_largest_number(numbers):
    
    # initiallizing the largest one by zero.
    largest_number = numbers[0]

    # this loop will itterate over the elements in that list:
    for number in numbers:
    # if the current number in that list will be greater than the largest_number which is zero initially, then;
    # largest_number will be updated by that number and this loop will continue till it finds the largest one
        
        if number > largest_number:
            largest_number = number
    return largest_number

# Main function definition
def main():
    n = int(input("Enter the number of elements in the list: "))
    numbers = []
    for i in range(n):
        number = int(input(f"Enter number {i+1}: "))
        numbers.append(number)

    largest = find_largest_number(numbers)
    print("The largest number in the list is:", largest)

# Main function call
main()