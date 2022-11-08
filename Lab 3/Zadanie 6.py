# Zastosuj instrukcje continue w programie z zad. 5 tak, aby po podaniu liczby punktów spoza
# przedziału 0 – 100 pomijać dalsze wykonywanie pętli. Sprawdź działanie programu. Następnie zmień pętlę na
# nieskończoną, czyli taką której warunek zawsze jest prawdziwy. Zakończ działanie pętli przy użyciu instrukcji
# break

number_student = int(input("Enter n "))

current_student = 1

summary = 0

while True:
    mark = int(input(f"Enter mark of student #{current_student} "))

    if 0 < mark < 100:
        summary += mark
        current_student += 1
    if current_student > number_student:
        break

print(summary / number_student)
