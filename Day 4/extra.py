import random
students = ['Ali', 'Ahmed', 'Usman', 'Hassan', 'Ayesha', 'Fatima', 'Zain', 'Sara', 'Hamza', 'Noor']
print("Students list:", students)
print("Number of students:", len(students))
winner = random.choice(students)
print(f"🎉 Winner is: {winner}")

students.remove(winner)
print("Remaining students:", students)
print("Number of students:", len(students))