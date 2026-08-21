# File này chứa "dữ liệu giả" (mock data) và 2 chức năng chính: đăng ký, đăng nhập.
# Không dùng mã hóa hay thư viện phức tạp, chỉ so sánh chuỗi (string) đơn giản.

# Dữ liệu người dùng giả lập, lưu trong một dict (giống như bảng "users" trong database).
# Key = tên đăng nhập, value = thông tin của người dùng đó.
users = {
    "admin": {"password": "admin123", "email": "admin@example.com"},
    "user1": {"password": "password1", "email": "user1@example.com"},
}


def reset_users():
    # Đưa dữ liệu về lại trạng thái ban đầu, dùng khi chạy unittest.
    global users
    users = {
        "admin": {"password": "admin123", "email": "admin@example.com"},
        "user1": {"password": "password1", "email": "user1@example.com"},
    }


def register(username, password, email):
    # Kiểm tra người dùng có bỏ trống ô nào không.
    if not username or not password or not email:
        return False, "Vui lòng nhập đầy đủ thông tin."

    # Kiểm tra tên đăng nhập đã có người dùng chưa.
    if username in users:
        return False, "Tên đăng nhập đã tồn tại."

    # Lưu tài khoản mới vào dict users.
    users[username] = {"password": password, "email": email}
    return True, "Đăng ký thành công."


def login(username, password):
    # Kiểm tra tên đăng nhập có tồn tại không.
    if username not in users:
        return False, "Tên đăng nhập hoặc mật khẩu không đúng."

    # So sánh mật khẩu nhập vào với mật khẩu đã lưu.
    if users[username]["password"] != password:
        return False, "Tên đăng nhập hoặc mật khẩu không đúng."

    return True, "Đăng nhập thành công."
