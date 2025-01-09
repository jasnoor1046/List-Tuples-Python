# the program to find the frequency of elements in a tuple.
def count_frequency(t):

    frequency_list = []
    for item in t:

        # enumerate: generates the index for each item here.
        # this nested loop here iterates through ech element(elem,count) in frequency_list with its index idx.
        for idx, (elem, count) in enumerate(frequency_list):

            # checks if the current element matches th item from the tuple
            # if the match is found, update the count of the existing element in frequency_list by incrementing the count.
            if elem == item:
                frequency_list[idx] = (elem, count + 1)
                break
        else:
            frequency_list.append((item, 1))
    return frequency_list


user_input = input("Enter the elements of the tuple: ")
user_tuple = tuple(user_input.split(","))

print("Frequency of elements: ", count_frequency(user_tuple))
