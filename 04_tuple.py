# program to find the pairs of elements that add upto specific sum.
def find_pairs(tup, target):
    pairs = []

    # iterates over each element in the tuple using index i.
    for i in range(len(tup)):

        # starts from i+1 to avoid comparing an elememnt with itself and ensure unique pairs.
        for j in range(i + 1, len(tup)):

            if tup[i] + tup[j] == target:
                pairs.append((tup[i], tup[j]))
    return pairs


user_input = input("enter the elements of tuple: ")

# tuple(map(int,user_input)): It applies the int function to each substring to an integer.
# e.g: map(int,['1','2','3']) will produce an iterator of integers [1,2,3]
# whereas tuple() converts this iterator into a tuple.

user_tuple = tuple(map(int, user_input.split(",")))
target_sum = int(input("Enter the target sum: "))

result = find_pairs(user_tuple, target_sum)

print("pairs that add upto", target_sum, ":", result)
