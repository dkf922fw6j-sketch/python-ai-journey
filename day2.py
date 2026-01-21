def read_grades(filename):
    students = []
    with open(filename, "r") as file:
        for line in file:
            name, grade = line.strip().split(",")
            students.append((name, int(grade)))
    return students


def calculate_average(students):
    total = 0
    for _, grade in students:
        total += grade
    return total // len(students)


def analyze_results(students, passing_grade):
    results = []
    for name, grade in students:
        if grade >= passing_grade:
            results.append(f"{name}: GEÇTİ")
        else:
            results.append(f"{name}: KALDI")
    return results


def write_results(results, average):
    with open("result.txt", "w") as file:
        for line in results:
            file.write(line + "\n")
        file.write(f"\nOrtalama: {average}")


passing_grade = int(input("Geçme notu gir: "))

students = read_grades("grades.txt")
average = calculate_average(students)
results = analyze_results(students, passing_grade)

write_results(results, average)

print("Bitti. Sonuçlar result.txt dosyasına yazıldı.")