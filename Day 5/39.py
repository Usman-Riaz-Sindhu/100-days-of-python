marks = [12, 43, 43, 54, 24, 83, 93, 23, 45, 67, 89, 90, 100]
total = sum(marks)
print(total)

sum = 0
for m in marks:
    sum += m
    
print(sum)

max_mark = 0
for m in marks:
    if m > max_mark:
        max_mark = m
print(max_mark)