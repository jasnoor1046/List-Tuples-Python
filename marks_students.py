
# Function to accept marks and sort them
def get_sorted_marks():
    # Create an empty list to store marks
    student_marks = []
    
    # Accept marks for 6 students
    for i in range(6):
        mark = int(input(f"Enter the marks for student {i+1}: "))
        student_marks.append(mark)
    
    # Sort the marks in ascending order
    sorted_marks = sorted(student_marks)
    
    return sorted_marks

# Get sorted marks and display them
sorted_marks = get_sorted_marks()
print("Marks in sorted manner:", sorted_marks)