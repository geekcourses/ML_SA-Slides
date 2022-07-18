student_scores = {
    "Ivan": 5.00,
    "Alex": 3.50,
    "Maria": 5.50,
    "Georgy": 5.00,
}


# create best_students_scores dictionary with "students:scores" pairs, where scores>4.0:
best_students_scores = {}
for student, score in student_scores.items():
    if( score > 4.00):
      best_students_scores[student] = score

#print result
for student, score in best_students_scores.items():
  print("{:<8s} - {:<.2f}".format(student,score))

