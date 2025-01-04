def find_duplicates(input_list):
    # create a list to store duplicate items
    duplicates= []

    # this loop iterates through the list and find duplicates
    for item in input_list:
        # this will count the number of elements being repeated, and will also check if the elemnts are present in
        # the duplicats list, if both of these conditions are true [duplicate] list will be appended by that element
         
        if input_list.count(item) > 1 and item not in duplicates:
            duplicates.append(item)
    return duplicates

# taking input from the user
num_elements= int(input("Enter the no. of elements in the list: "))

# initialized the list to store the elements enetered by the user
input_list= []

print("Enter the elements:")
for _ in range(num_elements):
    element= int(input())
    input_list.append(element)

# function calling to execute the above logic
duplicates= find_duplicates(input_list)
print("Duplicates in list are: ", duplicates)

