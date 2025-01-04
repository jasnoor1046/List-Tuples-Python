def filter_even_numbers(input_list):

    # num: The first num is the value to be included in the new list even_numbers
    # for num in input_list= This iterates over each num in input list
    even_numbers= [num for num in input_list if num%2==0]

    return even_numbers

num_elements= int(input("Enter the no. of elements: "))
# an empty list to store the input values
input_list= []

print("Enter elements: ")
for _ in range(num_elements):
  
  # lements will be enetered by the user
  element= int(input())

  # elements entered will be appended in the list
  input_list.append(element)

  even_numbers= filter_even_numbers(input_list)
  print("Even numbers in list: ", even_numbers)
