# this function will store the logic
def sort_and_display_marks():
    marks = []
    for i in range(6):
        mark = float(input(f"Enter marks for student {i + 1}: "))
        marks.append(mark)
    marks.sort()
    print("Sorted marks:", marks)

#function calling
sort_and_display_marks()
