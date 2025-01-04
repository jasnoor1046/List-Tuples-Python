def bubble_sort(lst):
    n = len(lst)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


num_elements = int(input("Enter the no. of elements in the list: "))

user_list = []
for i in range(num_elements):
    element = int(input(f"Enter element {i+1}: "))
    user_list.append(element)

    sorted_list = bubble_sort(user_list)
    print("Sorted list: ", sorted_list)
