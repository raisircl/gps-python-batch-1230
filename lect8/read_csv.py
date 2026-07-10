with open("students.csv", "r") as file:
    header = file.readline()
    print(header.strip())
    for line in file:
        data = line.strip().split(",")
        student_id = data[0]
        name = data[1]
        attendance = data[2]
        marks = data[3]
        
        print(name, attendance, marks)
