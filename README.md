# Hệ thống quản lý bán hàng

Bài tập lớn môn Cấu trúc dữ liệu và Giải thuật, chủ đề 4: Quản lý bán hàng.

Nhóm thực hiện: Nhóm 15

- Nguyễn Trịnh Mai Phương - 202418965: thiết kế chương trình, thiết kế dữ liệu, cài đặt luồng đọc/ghi dữ liệu, viết báo cáo.
- Trần Minh Quân - 202418973: kiểm thử, cài đặt/kịch bản test, chuẩn bị dữ liệu demo, viết báo cáo, hỗ trợ đóng gói và GitHub.

## Nội dung chính

- Quản lý sản phẩm: thêm, sửa/xóa qua menu, tìm kiếm theo mã/tên/loại, sắp xếp theo mã, tên, giá, tồn kho.
- Quản lý khách hàng: thêm, tìm kiếm, lưu thông tin liên hệ.
- Lập hóa đơn bán hàng: chọn khách hàng, chọn nhiều sản phẩm, kiểm tra tồn kho, tính chiết khấu, VAT và tổng tiền.
- Lưu hóa đơn master-detail: `invoices.txt` và `invoice_items.txt`.
- Báo cáo: doanh thu theo ngày/tháng, top 10 sản phẩm bán chạy, danh sách sắp hết hàng.
- Dữ liệu lưu bằng file text có cấu trúc `|`, không dùng cơ sở dữ liệu.
- Cấu trúc dữ liệu và thuật toán tự cài đặt: `DynamicArray`, `LinkedList`, `HashTable`, `linear_search`, `quick_sort`.

## Cách chạy

Yêu cầu: Python 3.10 trở lên.

Chạy menu chính:

```powershell
python -m sales_manager.cli menu
```

Hoặc nhấp đúp:

```text
run_sales_manager.bat
```

Tạo dữ liệu demo và 3 hóa đơn mẫu:

```powershell
python -m sales_manager.cli --data-dir data/demo demo
```

Xem tổng quan:

```powershell
python -m sales_manager.cli summary
```

Xuất báo cáo text:

```powershell
python -m sales_manager.cli --data-dir data/demo report
```

Chạy kiểm thử:

```powershell
python -m unittest discover -s tests
```

## Cấu trúc thư mục

```text
sales_manager/
  data_structures.py  # DynamicArray, LinkedList, HashTable, search, sort
  models.py           # Product, Customer, Invoice, InvoiceItem
  storage.py          # đọc/ghi file text
  manager.py          # xử lý nghiệp vụ bán hàng
  cli.py              # menu console và lệnh demo/report
data/sample/          # dữ liệu mẫu ban đầu
tests/                # unit test
report/               # báo cáo Word/PDF/Markdown
```

## File dữ liệu

- `products.txt`: sản phẩm.
- `customers.txt`: khách hàng.
- `invoices.txt`: hóa đơn.
- `invoice_items.txt`: chi tiết hóa đơn.

Mỗi file có dòng tiêu đề và các dòng dữ liệu phân tách bằng dấu `|`.

## Link GitHub

https://github.com/nhtameo/quan-ly-ban-hang-dsa
