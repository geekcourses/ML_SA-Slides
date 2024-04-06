students = {
    "Ivan": 5.00,
    "Alex": 3.50,
    "Maria": 5.50,
    "Georgy": 5.00,
}

# Print out the names of the students, which scores > 4.00
names = list(students.keys())
scores = list(students.values())

max_score = max(scores)
max_score_index = scores.index(max_score)

min_score = min(scores)
min_score_index = scores.index(min_score)

print("{} - {}".format(names[max_score_index], max_score))
print("{} - {}".format(names[min_score_index], min_score))
