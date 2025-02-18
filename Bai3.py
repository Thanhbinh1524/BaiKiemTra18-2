import string

def word_count(file_path):
    # Khởi tạo dictionary để lưu trữ từ và số lần xuất hiện
    word_dict = {}
    
    # Đọc tệp tin
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Loại bỏ dấu câu và chuyển tất cả về chữ thường
            line = line.translate(str.maketrans('', '', string.punctuation)).lower()
            words = line.split()
            
            # Đếm số lần xuất hiện của từ
            for word in words:
                word_dict[word] = word_dict.get(word, 0) + 1
    
    return word_dict

# Ví dụ sử dụng
file_path = 'c:\\Users\\azin\\OneDrive\\Máy tính\\P1_data.txt'  # Thay đổi đường dẫn đến tệp của bạn
result = word_count(file_path)
print(result)