def sum_nested_tuples(t):
    total_sum = 0
    for element in t:
        if isinstance(
            element, tuple
        ):  # this checks if the current element is present in the tuple
            # if it is a tuple the function is called recursively with this nested tuple as the argument.
            # the result is added to total_sum.
            total_sum += sum_nested_tuples(element)
        else:
            total_sum += element
    return total_sum


# Take tuple input from the user
user_input = input("Enter the elements of the tuple: ")

# eval: it evaluates the input string as python expression allows us to interpret the nested tuples correctly
user_tuple = eval(user_input)

print("Sum of all elements:", sum_nested_tuples(user_tuple))
