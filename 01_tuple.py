def second_largest(t):
    if len(t) < 2:
        return None

    first, second = float("-inf"), float("-inf")
    for num in t:

        if num > first:
            first, second = num, first

        elif first > num > second:
            second = num
    return second


user_input = input("Enter the elements of the tuple: ")
user_input = tuple(map(int, user_input.split(",")))

print("second largest element: ", second_largest(user_input))
