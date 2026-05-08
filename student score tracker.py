students = {}

def load_data():
    file = open("students.txt", "r")
    content = file.read()
    file.close()

    if content != "":
        records = content.split(";")   
        for record in records:
            if record != "":
                name, score = record.split(",")
                students[name] = int(score)

def save_data():
    file = open("students.txt", "w")
    for name in students:
        file.write(name + "," + str(students[name]) + ";")
    file.close()


while True:
    print("")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Score")
    print("4. Delete Student")
    print("5. Statistics")
    print("6. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        score = int(input("Score: "))
        students[name] = score

    elif choice == "2":
        for name in students:
            print(name, ":", students[name])

    elif choice == "3":
        name = input("Enter name: ")
        if name in students:
            students[name] = int(input("New score: "))

    elif choice == "4":
        name = input("Enter name: ")
        if name in students:
            del students[name]

    elif choice == "5":
        if len(students) > 0:
            scores = list(students.values())
            print("Average:", sum(scores) / len(scores))
            print("Highest:", max(scores))
            print("Lowest:", min(scores))

    elif choice == "6":
        save_data()
        break
