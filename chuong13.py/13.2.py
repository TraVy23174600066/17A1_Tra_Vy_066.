try:
    # Mở tập tin để đọc
    with open('HumptyDumpty.txt', 'r') as file:
        # Đọc nội dung của tập tin
        content = file.read()

        # Hiển thị nội dung của tập tin
        print("Nội dung của tập tin:")
        print(content)

        # Đếm số ký tự
        so_ky_tu = len(content)
        print(f"Tập tin có {so_ky_tu} ký tự.")

except FileNotFoundError:
    print("Tập tin không tồn tại.")
except Exception as e:
    print(f"Có lỗi xảy ra: {e}")







