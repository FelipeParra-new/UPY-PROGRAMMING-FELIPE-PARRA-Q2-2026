# Required Structures
users = {
    'jperez':	{
        'password': '1234',
        'rol': 'student',
        'name': 'Juan Pérez'
    },
    'dromo':	{
        'password': '1234',
        'rol': 'student',
        'name': 'Daniela Romo'
    },
    'mjuarez':	{
        'password': '1234',
        'rol': 'student',
        'name': 'Mauricio Juárez'
    },
    'mlopez':	{
        'password': '1234',
        'rol': 'student',
        'name': 'María López'
    },
    'euc':	{
        'password': '1234',
        'rol': 'student',
        'name': 'Ernesto Uc'
    },
    'cbalam':	{
        'password': '1234',
        'rol': 'student',
        'name': 'Carlos Balam'
    },
    'jpedrozo':	{
        'password': '1234',
        'rol': 'professor',
        'name': 'Jorge Pedrozo'
    },
    'dgamboa':	{
        'password': '1234',
        'rol': 'coordinator',
        'name': 'Didier Gamboa'
    }
}
 
subjects = (
    "Discrete Mathematics",
    "Programming",
    "English II",
    "Differential Calculus",
    "Probability and Statistics",
    "Computer and Server Architecture",
    "Socio-Emotional Skills and Conflict Management"
)
 
notes = {
    'jperez': {
        'Discrete Mathematics': 8.5,
        'Programming': 9.2,
        'English II': 9.0,
        'Differential Calculus': 7.8,
        'Probability and Statistics': 8.3,
        'Computer and Server Architecture': 6.8,
        'Socio-Emotional Skills and Conflict Management': 9.5
    },
    'dromo': {
        'Discrete Mathematics': 9.0,
        'Programming': 6.7,
        'English II': 9.4,
        'Differential Calculus': 6.2,
        'Probability and Statistics': 9.1,
        'Computer and Server Architecture': 6.5,
        'Socio-Emotional Skills and Conflict Management': 9.8
    },
    'mjuarez': {
        'Discrete Mathematics': 7.5,
        'Programming': 8.0,
        'English II': 8.5,
        'Differential Calculus': 7.0,
        'Probability and Statistics': 7.8,
        'Computer and Server Architecture': 6.2,
        'Socio-Emotional Skills and Conflict Management': 8.9
    },
    'mlopez': {
        'Discrete Mathematics': 9.5,
        'Programming': 9.8,
        'English II': 9.2,
        'Differential Calculus': 9.0,
        'Probability and Statistics': 9.6,
        'Computer and Server Architecture': 9.4,
        'Socio-Emotional Skills and Conflict Management': 10.0
    },
    'euc': {
        'Discrete Mathematics': 8.2,
        'Programming': 6.9,
        'English II': 8.8,
        'Differential Calculus': 6.0,
        'Probability and Statistics': 6.4,
        'Computer and Server Architecture': 8.1,
        'Socio-Emotional Skills and Conflict Management': 9.0
    },
    'cbalam': {
        'Discrete Mathematics': 8.8,
        'Programming': 9.0,
        'English II': 8.5,
        'Differential Calculus': 6.6,
        'Probability and Statistics': 8.9,
        'Computer and Server Architecture': 8.7,
        'Socio-Emotional Skills and Conflict Management': 9.2
    }
}

while True:
    username=input("Write the username: ")
    password=input("Write the password: ")
    if username in users and users[username]["password"]==password:
        user_info = users[username]
        rol = user_info["rol"]
        nombre = user_info["name"]
        
        print(f"Welcome!, {nombre} ({rol})")
        break
    else:
        print("Incorrect Username/Password, try again ")

if rol=="student":
    print("_________________________________")
    print("School report")
    print("_________________________________")
    
    approved=set()
    pending=set()
    
    for subject, grade in notes[username].items():
        if grade >= 7.0:
            approved.add(subject)
            print(f"{subject:<35} : {grade}")
        else:
            pending.add(subject)
    print(f"Approved: {approved}")
    print(f"Pending : {pending}")
    
#Teacher´s point of view
elif rol == "professor":
    print(" Students")
    print("___________________________")
    # Filt and print only the user with student´s rol
    for u, data in users.items():
        if data["rol"] == "student":
            print(f"User: {u:<10} | Student: {data["name"]}")
            
    print()
    while True:
        student_user = input("Student to grade (username): ")
        if student_user not in notes:
            break
        
        print(" Subjects")
        print("_____________________________")
        for subject in subjects:
            print(subject)
        
        print()
        subject_to_grade=input("Write the subject to grade: ")
        # Valid if the subject exist
        if subject_to_grade in notes[student_user]:
            new_grade = float(input("New grade: "))
            old_grade = notes[student_user][subject_to_grade]
            
            print("Do you confirm (yes/no)?")
            print(f"{subject_to_grade}: {old_grade} ==> {new_grade}")
            confirm = input().strip().lower()
            
            if confirm == "yes":
                notes[student_user][subject_to_grade] = new_grade
                print("Grade updated!")
                print(notes[student_user])
            else:
                print("Update cancelled.")
        else:
            print("Subject not found.")
            
        print("Write other thing to exit")
#Coordinator´s Point of view
elif rol == "coordinator":
    print(" Professors")
    print("___________________________")
    for u, data in users.items():
        if data["rol"] == "professor":
            print(f"User: {u:<10} | Professor: {data["name"]}")
            
    print("________________________________________")
    print(" Students")
    print("________________________________________")
    
    # Auxiliary list to store the exact order of the table columns 
    student_users = []
    for u, data in users.items():
        if data["rol"] == "student":
            print(f"User: {u:<10} | Student: {data["name"]}")
            student_users.append(u)
            
    print("________________________________________")
    print(" Records")
    print("________________________________________")
    
    # #Build the header
    header = f"{'SUBJECTS':<15}"
    for su in student_users:
        header += f" | {su:<7}"
    print(header)
    print("-" * len(header))
    
    # Cross-checking data by rows (subjects) and columns (students)
    for subject in subjects:
        row_str = f"{subject[:13]:<15}"
        for su in student_users:
            grade = notes[su][subject]
            row_str += f" | {grade:<7.1f}"
        print(row_str)   
    

    