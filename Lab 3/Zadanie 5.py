# Grupa laboratoryjna składa się z n studentów (wartość n podaje użytkownik). Wprowadzamy
# liczbę punktów dla każdego studenta. Napisz program, który obliczy średnią liczbę punktów w grupie z
# wykorzystaniem pętli while

number_student = int(input("Enter n "))

current_student = 1

summary = 0

while current_student <= number_student:
    mark = int(input(f"Enter mark of student #{current_student}:"))
    summary += mark
    current_student += 1

print(summary / number_student)
