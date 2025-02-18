def count_chars(string):
    # Khởi tạo một dictionary để lưu trữ số lần xuất hiện của các ký tự
    char_count = {}

    # Duyệt qua từng ký tự trong chuỗi
    for char in string:
        # Chỉ xét các ký tự trong khoảng [a-z] và [A-Z]
        if char.isalpha():  # Kiểm tra xem ký tự có phải là chữ cái không
            # Chuyển ký tự thành chữ thường để đếm không phân biệt hoa thường
            char = char.lower()
            # Nếu ký tự đã có trong dictionary, tăng giá trị lên 1
            if char in char_count:
                char_count[char] += 1
            else:
                # Nếu chưa có, thêm ký tự vào dictionary với giá trị 1
                char_count[char] = 1

    return char_count

# Ví dụ sử dụng
string1 = "ThBinh"
result1 = count_chars(string1)
print(result1)  

string2 = "ThDiem"
result2 = count_chars(string2)
print(result2)  