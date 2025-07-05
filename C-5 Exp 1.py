print("Name : Abhijith Mohanan ")
print("Admission No: A24MCA001")
print("Experiment No: 15")


with open("file.txt", "r") as file:
    lines = [line.strip() for line in file]
    print("lines are:", lines)
