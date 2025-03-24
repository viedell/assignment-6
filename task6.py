data = [
    {"name": "Nugraha", "birthdate": "1989-09-13"},
    {"name": "John", "birthdate": "1990-01-01"},
    {"name": "Jane", "birthdate": "1992-02-02"},
    {"name": "Doe", "birthdate": "1994-03-03"}
]

current_year = 2025

print("No | Name    | Age")
print("-----------------")

num = 1
for person in data:
    birth_year = int(person["birthdate"].split("-")[0])
    age = current_year - birth_year
    print(num, "|", person["name"], "|", age)
    num += 1
