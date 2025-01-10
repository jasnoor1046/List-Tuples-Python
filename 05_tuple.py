# program to rotate the tuple elements.
# tup: it is the tuple to be rotated.
# n: no. of positions.
def rotate_tuple(tup, n):

    # this will handle the case that n must lie within the range of.
    n = n % len(tup)
    rotated_tup = tup[-n:] + tup[:-n]
    # tup[-n:] slice will return the last 'n' elements of the tuple.
    # tup[:-n] slice will return all the elements of the tuple except the last 'n' elements.
    return rotated_tup


user_input = input("Enter the elements of tuple: ")
user_tuple = tuple(map(int, user_input.split(",")))

# taking the input from the user
positions = int(input("Enter the number of positions to be rotated: "))

rotated_tuple = rotate_tuple(user_tuple, positions)
print("Rotated tuple: ", rotated_tuple)
