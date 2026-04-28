students = []

n = int(input("Nhập số học sinh: "))

for i in range(n):
    print(f"\nHọc sinh {i+1}:")
    name = input("Họ tên: ")
    toan = float(input("Điểm Toán: "))
    ly = float(input("Điểm Lý: "))
    hoa = float(input("Điểm Hóa: "))
    
    dtb = (toan + ly + hoa) / 3
    
    students.append({
        "name": name,
        "dtb": dtb
    })

print("\nHọc sinh có điểm TB >= 8:")
for s in students:
    if s["dtb"] >= 8:
        print(s["name"], "-", round(s["dtb"], 2))

max_student = max(students, key=lambda x: x["dtb"])
print("\nHọc sinh có điểm TB cao nhất:")
print(max_student["name"], "-", round(max_student["dtb"], 2))

count = sum(1 for s in students if s["dtb"] < 5)
print("\nSố học sinh có điểm TB < 5:", count)