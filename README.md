# FastAPI Project - Chat with Gemini API

Dự án này sử dụng **FastAPI** để xây dựng API cho việc trò chuyện với **Gemini** API. Đây là một ứng dụng API đơn giản với FastAPI.

## Hướng dẫn cài đặt và chạy dự án

### 1. **Clone dự án từ GitHub**

Đầu tiên, bạn cần clone dự án về máy của mình bằng lệnh sau:

```bash
git clone https://github.com/abetdt/fastapi-chat-with-gemini.git
cd fastapi-chat-with-gemini
```

## 2. **Cài đặt môi trường ảo (virtual environment)**

Để đảm bảo rằng các thư viện phụ thuộc của dự án không xung đột với các dự án khác trên máy của bạn, bạn nên sử dụng một môi trường ảo. Môi trường ảo giúp quản lý các thư viện phụ thuộc riêng biệt cho từng dự án, đảm bảo tính độc lập và tránh xung đột phiên bản giữa các dự án.

### **Cài đặt môi trường ảo**

Dưới đây là các phương án để cài đặt môi trường ảo:

#### **Với pipenv** (Công cụ quản lý môi trường và thư viện):

Nếu bạn chưa cài đặt `pipenv`, bạn có thể cài đặt bằng lệnh:

```bash
pip install pipenv
```
## 3. **Tạo một môi trường ảo mới:**

Gõ lệnh sau tạo môi trường ảo venv:
```bash
python3 -m venv venv
```

### **Kích hoạt môi trường ảo**

Trên Linux:
```bash
source venv/bin/activate
```
Trên Windows:
```bash
venv\Scripts\activate
```
Khi môi trường ảo được kích hoạt, bạn sẽ thấy tên môi trường ảo xuất hiện ở đầu dòng lệnh, ví dụ:
```bash
(.venv) user@hostname:~/project-name$
```
## 4. **Cài thư viện:**

Trong mỗi trường ảo cài thư viện bằng cách gõ lệnh sau:
```bash
pip install -r requirements.txt
```

## 5. **Thêm API key của bạn trong file main:**

Lên google và search cách lấy API key của Gemini và dán vào chỗ **my_key** chỗ đoạn code bên dưới trong file main
```python
check_configure_genai(api_key="my_key")
```
Bạn có thể xem file main.py từ dự án tại [main.py](main.py).


## 6. **Thêm API key của bạn trong file main:**

Sau khi đã cài đặt môi trường ảo, cấu hình API key, và cài đặt các thư viện yêu cầu, bạn có thể chạy ứng dụng FastAPI như sau:
```bash
uvicorn main:app --reload
```
Ứng dụng FastAPI sẽ chạy trên http://127.0.0.1:8000. Bạn có thể truy cập API bằng Swagger UI
```bash
http://127.0.0.1:8000/docs
```
