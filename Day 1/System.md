Mở website và xem nó hoạt động như thế nào
Theo dõi xem nó có thu thập dữ liệu người dùng mà không xin phép không
Kiểm tra các nút đồng ý (consent) có được thiết kế đúng cách không
Ghi lại tất cả vi phạm tìm được
Tạo báo cáo để gửi cho khách hàng


Classes & Objects: Python cũng có, cú pháp đơn giản hơn
Functions: Giống hệt, nhưng không cần khai báo kiểu trả về
Loops & Conditions: Tương tự, chỉ khác cú pháp
Exception Handling: try-catch trong Java = try-except trong Python



python <--- c++



Không cần biên dịch: Code Python chạy trực tiếp
Dynamic typing: Không cần khai báo int x, chỉ cần x = 5
Async/Await: Khái niệm mới, sẽ giải thích kỹ ở phần sau




c++ : compile & debug




┌─────────────┐
│   USER      │ ← Người dùng gửi yêu cầu quét website
└──────┬──────┘
       │
       ▼
┌─────────────────────────────────┐
│   FASTAPI BACKEND (API Server)  │ ← Nhận request, quản lý job
└──────┬──────────────────┬───────┘
       │                  │
       ▼                  ▼
┌─────────────┐    ┌─────────────┐
│  DATABASE   │    │   SCANNER   │ ← Playwright quét website
│ (PostgreSQL)│    │   ENGINE    │
└─────────────┘    └──────┬──────┘
                          │
                          ▼
                   ┌─────────────┐
                   │   REPORT    │ ← Tạo báo cáo PDF/HTML
                   └─────────────┘

MVC Pattern   model view controller
