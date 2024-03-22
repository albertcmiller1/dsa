# https://stackoverflow.com/questions/18296755/python-max-function-using-key-and-lambda-expression

students = {
    'Theodore': 19,
    'Roxanne': 22,
    'Albert': 22,
    'Mathew': 21,
    'Betty': 20
}


print(max(students, key=students.get))

