num_students= int(input("Please Enter the number of the student:>>>>"))
i=1
while i <= num_students :#(i)will initialize for the loops (while loop is used for outer loop)
    total_grade = 0
    num_subjects = int(input(f"Enter the number of subjects for student {i}:>>"))
    
    for j in range(1, num_students +1):#for loop in a while loop {neested loop}
        grade = float(input(f"Enter subject {j} grade for student {i}:>>"))
        total_grade += grade

    average_grade = total_grade/ num_students
    print(f"Average grade for studenets {i}>>>:{average_grade:.2f}")#{2.f is for two decimal places for float!!!}\
    i += 1#(for the next student in the outer loop!!)