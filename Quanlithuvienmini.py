Thuvien = []

while True:
    print("\nQUẢN LÍ THƯ VIỆN MINI")
    print("1. Thêm sách")
    print("2. Hiển thị toàn bộ sách")
    print("3. Tìm kiếm sách qua tên tác giả")
    print("4. Xoá sách")
    print("5. Thoát")
    choice = input("Chọn (1-5): ")

    if choice == "1":
        tensach = input("Nhập tên sách: ")
        tacgia = input("Nhập tên tác giả: ")
        
        sách = {
            "Tên sách": tensach,
            "Tên tác giả": tacgia,
        }
        Thuvien.append(sách)
        print("ĐÃ THÊM SÁCH!")
    
    elif choice == "2":
        if not Thuvien:
            print("CHƯA CÓ SÁCH NÀO")
        else:
            for i, t in enumerate(Thuvien, start = 1):
                print(f"{i}. {t['Tên sách']} - {t['Tên tác giả']}")

    elif choice == "3":
        keyword = input("Nhập tên tác giả để tìm: ").lower()
        found = []
        for sách in Thuvien:
            if keyword in sách['Tên sách'].lower() or keyword in sách['Tên tác giả'].lower():
                found.append(sách)
            
        if found:
            print("\nKẾT QUẢ TÌM KIẾM:")
            for i, sách in enumerate(found, 1):
                print(f"{i}. {sách['Tên sách']} - {sách['Tên tác giả']}")
        else:
            print("KHÔNG TÌM THẤY SÁCH NÀO!")

    elif choice == "4":
        for i, sách in enumerate(found, 1):
            print(f"{i}. {sách['Tên sách']} - {sách['Tên tác giả']}")
        num = int(input("Nhập số thứ tự cần xoá: "))
        if 0 < num <= len(Thuvien):
            Thuvien.pop(num-1)
            print("ĐÃ XOÁ SÁCH!")
        else:
            print("KHÔNG HỢP LỆ!")

    elif choice == "5":
        print("TẠM BIỆT!")
        break
    
    else:
        print("KHÔNG HỢP LỆ!!!")
