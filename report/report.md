# BÁO CÁO BÀI TẬP LỚN

## Hệ thống quản lý bán hàng

- Học phần: Cấu trúc dữ liệu và Giải thuật.
- Chủ đề: Chủ đề 4 - Quản lý bán hàng.
- Ngôn ngữ lập trình: Python.
- Hình thức dữ liệu: File text có cấu trúc.
- Repository GitHub: https://github.com/nhtameo/quan-ly-ban-hang-dsa.

---

## 1. Thông tin chung

### 1.1. Thông tin người thực hiện

Nhóm thực hiện: điền tên nhóm trước khi nộp.  
Thành viên: điền họ tên, MSSV và phân công trước khi nộp.  

Phân công gợi ý:

- Phân tích yêu cầu, thiết kế dữ liệu: thành viên 1.
- Cài đặt cấu trúc dữ liệu và nghiệp vụ: thành viên 2.
- Kiểm thử, báo cáo, slide: thành viên 3.

### 1.2. Căn cứ yêu cầu

Theo danh sách chủ đề project 20252, chủ đề quản lý bán hàng yêu cầu xây dựng chương trình đơn giản cho phép:

- Quản lý thông tin sản phẩm: mã sản phẩm, tên sản phẩm, đơn vị tính, đơn giá.
- Quản lý thông tin khách hàng.
- Lập hóa đơn bán hàng, chọn sản phẩm, số lượng, áp dụng chiết khấu nếu có.
- Tính tổng tiền, thuế VAT và số tiền khách phải trả.
- Lưu trữ hóa đơn theo mô hình master-detail gồm hóa đơn và chi tiết hóa đơn.
- Báo cáo doanh thu theo ngày/tháng và thống kê top 10 mặt hàng bán chạy nhất.

Yêu cầu chung của môn học:

- Chương trình có menu để người dùng lựa chọn tác vụ cho đến khi kết thúc.
- Dữ liệu vào/ra được lưu trong file text.
- Không dùng trực tiếp cấu trúc dữ liệu nâng cao có sẵn cho nghiệp vụ; phải tự cài đặt cấu trúc dữ liệu và thuật toán.
- Có kiểm thử, báo cáo Word và file nén mã nguồn khi nộp.

## 2. Mô tả bài toán

Một cửa hàng bán thiết bị công nghệ cần quản lý danh mục hàng hóa, khách hàng và hoạt động bán hàng hằng ngày. Khi khách mua hàng, nhân viên lập hóa đơn gồm nhiều dòng chi tiết, mỗi dòng tương ứng với một sản phẩm và số lượng. Chương trình phải kiểm tra tồn kho trước khi bán, tự động giảm tồn kho sau khi lập hóa đơn, tính toán chiết khấu, VAT và tổng tiền thanh toán.

Bên cạnh thao tác bán hàng, người quản lý cần xem nhanh doanh thu theo ngày/tháng, biết sản phẩm nào bán chạy nhất và sản phẩm nào sắp hết hàng để nhập thêm.

### 2.1. Đầu vào

Đầu vào có hai nguồn:

- File dữ liệu text ban đầu:
  - `products.txt`: danh sách sản phẩm.
  - `customers.txt`: danh sách khách hàng.
  - `invoices.txt`: danh sách hóa đơn.
  - `invoice_items.txt`: danh sách chi tiết hóa đơn.
- Nhập liệu từ bàn phím thông qua menu console:
  - Thêm sản phẩm.
  - Thêm khách hàng.
  - Lập hóa đơn.
  - Nhập tiêu chí tìm kiếm/sắp xếp/báo cáo.

### 2.2. Đầu ra

Đầu ra gồm:

- Dữ liệu được lưu lại vào các file text sau mỗi thao tác làm thay đổi dữ liệu.
- Kết quả hiển thị trên màn hình console: danh sách sản phẩm, khách hàng, hóa đơn, báo cáo.
- File báo cáo text `output/sales_report.txt` khi chạy chức năng xuất báo cáo.
- Báo cáo nộp bài: `report/report.docx`, `report/report.pdf`.

## 3. Yêu cầu chức năng

### 3.1. Quản lý sản phẩm

Mỗi sản phẩm có các thuộc tính:

- Mã sản phẩm (`sku`).
- Tên sản phẩm.
- Đơn vị tính.
- Loại sản phẩm.
- Đơn giá bán.
- Số lượng tồn kho.
- Ngưỡng tồn kho tối thiểu.

Chức năng:

- Hiển thị danh sách sản phẩm.
- Thêm sản phẩm mới.
- Cập nhật/xóa sản phẩm ở lớp nghiệp vụ.
- Tìm kiếm theo mã, tên hoặc loại.
- Sắp xếp theo mã, tên, đơn giá hoặc tồn kho.
- Liệt kê sản phẩm sắp hết hàng.

### 3.2. Quản lý khách hàng

Mỗi khách hàng có:

- Mã khách hàng.
- Họ tên.
- Số điện thoại.
- Địa chỉ.

Chức năng:

- Hiển thị danh sách khách hàng.
- Thêm khách hàng mới.
- Cập nhật/xóa khách hàng ở lớp nghiệp vụ.
- Tìm kiếm theo mã, tên hoặc số điện thoại.

### 3.3. Lập hóa đơn bán hàng

Một hóa đơn gồm phần đầu hóa đơn và nhiều dòng chi tiết:

- Đầu hóa đơn: mã hóa đơn, mã khách hàng, tên khách hàng, thời gian lập, chiết khấu, VAT, tạm tính, tiền VAT, tổng tiền.
- Chi tiết hóa đơn: mã hóa đơn, mã sản phẩm, tên sản phẩm, số lượng, đơn giá, thành tiền.

Luồng xử lý:

1. Nhân viên nhập mã khách hàng.
2. Nhân viên nhập từng mã sản phẩm và số lượng.
3. Chương trình tra cứu sản phẩm bằng bảng băm.
4. Chương trình kiểm tra số lượng tồn kho.
5. Nếu hợp lệ, chương trình tính tạm tính, chiết khấu, VAT và tổng tiền.
6. Chương trình tạo hóa đơn mới, thêm các dòng chi tiết hóa đơn.
7. Chương trình giảm tồn kho từng sản phẩm đã bán.
8. Chương trình lưu lại file text.

### 3.4. Báo cáo

Các báo cáo được cài đặt:

- Tổng quan: số sản phẩm, số khách hàng, số hóa đơn, số dòng chi tiết, tổng doanh thu.
- Doanh thu theo ngày.
- Doanh thu theo tháng.
- Top 10 sản phẩm bán chạy nhất.
- Sản phẩm sắp hết hàng.

## 4. Thiết kế dữ liệu file text

Chương trình không sử dụng cơ sở dữ liệu. Tất cả dữ liệu được lưu trong các file text có dòng tiêu đề và các trường phân tách bằng dấu `|`.

### 4.1. File `products.txt`

```text
sku|name|unit|category|price|stock|min_stock
SP001|Dien thoai Alpha A1|chiec|Dien thoai|4990000|35|5
```

Ý nghĩa:

- `sku`: khóa chính logic của sản phẩm.
- `name`: tên sản phẩm.
- `unit`: đơn vị tính.
- `category`: loại hàng.
- `price`: đơn giá bán.
- `stock`: tồn kho hiện tại.
- `min_stock`: ngưỡng cảnh báo tồn kho.

### 4.2. File `customers.txt`

```text
customer_id|name|phone|address
KH001|Nguyen Van An|0901000001|Cau Giay, Ha Noi
```

### 4.3. File `invoices.txt`

```text
invoice_id|customer_id|customer_name|created_at|discount_percent|vat_percent|subtotal|vat_amount|total
HD0001|KH001|Nguyen Van An|2026-06-21 20:00:00|2.00|8.00|5388000|422419|5810419
```

### 4.4. File `invoice_items.txt`

```text
invoice_id|sku|product_name|quantity|unit_price|line_total
HD0001|SP001|Dien thoai Alpha A1|1|4990000|4990000
```

Mô hình này bảo đảm hóa đơn và chi tiết hóa đơn là quan hệ master-detail:

- Một hóa đơn có nhiều chi tiết hóa đơn.
- Mỗi chi tiết hóa đơn thuộc đúng một hóa đơn.
- Thông tin tên sản phẩm và đơn giá tại thời điểm bán được lưu trong chi tiết để không bị sai lệch nếu danh mục sản phẩm thay đổi sau này.

## 5. Cấu trúc dữ liệu sử dụng

### 5.1. `DynamicArray`

`DynamicArray` là mảng động tự cài đặt trong file `sales_manager/data_structures.py`.

Vai trò:

- Lưu danh sách sản phẩm.
- Lưu danh sách khách hàng.
- Lưu danh sách hóa đơn.
- Lưu danh sách chi tiết hóa đơn.
- Lưu kết quả tìm kiếm, sắp xếp, báo cáo.

Các thao tác chính:

- `append(value)`: thêm phần tử vào cuối.
- `get(index)`: truy cập theo chỉ số.
- `set(index, value)`: cập nhật phần tử.
- `insert(index, value)`: chèn phần tử.
- `remove_at(index)`: xóa phần tử theo vị trí.
- `copy()`: tạo bản sao để sắp xếp mà không làm thay đổi dữ liệu gốc.

Độ phức tạp:

- Truy cập theo chỉ số: O(1).
- Thêm cuối: O(1) trung bình, O(n) khi resize.
- Xóa/chèn giữa mảng: O(n).
- Duyệt toàn bộ: O(n).

### 5.2. `LinkedList`

`LinkedList` là danh sách liên kết đơn, dùng làm bucket trong bảng băm.

Vai trò:

- Xử lý va chạm trong bảng băm theo kỹ thuật separate chaining.
- Mỗi node lưu một cặp khóa-giá trị.

Độ phức tạp:

- Thêm đầu danh sách: O(1).
- Tìm kiếm trong một bucket: O(k), với k là số phần tử trong bucket.

### 5.3. `HashTable`

`HashTable` là bảng băm tự cài đặt, không dùng `dict` cho dữ liệu nghiệp vụ.

Vai trò:

- Tra cứu sản phẩm theo mã `sku`.
- Tra cứu khách hàng theo mã `customer_id`.
- Gom nhóm doanh thu theo ngày/tháng.
- Gom nhóm sản phẩm bán chạy theo mã sản phẩm.

Cách cài đặt:

- Mảng bucket có kích thước cố định.
- Mỗi bucket là một `LinkedList`.
- Hàm băm chuỗi tự cài đặt theo công thức:

```text
hash = (hash * 31 + ASCII(character)) mod capacity
```

Độ phức tạp:

- Tra cứu/thêm/xóa trung bình: O(1).
- Trường hợp xấu khi nhiều khóa rơi vào cùng bucket: O(n).

## 6. Thuật toán sử dụng

### 6.1. Tìm kiếm tuyến tính

Tìm kiếm tuyến tính được dùng khi người dùng nhập từ khóa tìm sản phẩm hoặc khách hàng. Vì từ khóa có thể xuất hiện trong mã, tên, loại hoặc số điện thoại nên không thể chỉ dùng tra cứu chính xác bằng mã.

Giả mã:

```text
linear_search(array, predicate):
    result = DynamicArray()
    for each item in array:
        if predicate(item) is true:
            result.append(item)
    return result
```

Độ phức tạp: O(n).

### 6.2. Quick sort

Quick sort được dùng để sắp xếp sản phẩm theo mã, tên, giá, tồn kho và sắp xếp báo cáo top sản phẩm bán chạy.

Giả mã:

```text
quick_sort(array, left, right):
    if left >= right:
        return
    pivot = partition(array, left, right)
    quick_sort(array, left, pivot - 1)
    quick_sort(array, pivot + 1, right)
```

Độ phức tạp:

- Trung bình: O(n log n).
- Xấu nhất: O(n^2).
- Không gian phụ do đệ quy: O(log n) trung bình.

### 6.3. Thuật toán lập hóa đơn

```text
create_invoice(customer_id, lines, discount_percent, vat_percent):
    customer = customer_hash.get(customer_id)
    if customer not found:
        báo lỗi

    subtotal = 0
    for line in lines:
        product = product_hash.get(line.sku)
        if product not found:
            báo lỗi
        if product.stock < line.quantity:
            báo lỗi không đủ tồn kho
        subtotal += product.price * line.quantity

    discount = subtotal * discount_percent / 100
    vat = (subtotal - discount) * vat_percent / 100
    total = subtotal - discount + vat

    tạo invoice_id mới
    thêm Invoice vào danh sách hóa đơn
    for line in lines:
        thêm InvoiceItem
        giảm product.stock

    lưu products, invoices, invoice_items ra file text
```

Nếu hóa đơn có k dòng hàng, sau khi đã có bảng băm sản phẩm/khách hàng, thời gian xử lý chính là O(k).

## 7. Thiết kế module chương trình

### 7.1. `sales_manager/data_structures.py`

Chứa toàn bộ cấu trúc dữ liệu và thuật toán tự cài đặt:

- `DynamicArray`.
- `LinkedList`.
- `HashTable`.
- `linear_search`.
- `quick_sort`.

### 7.2. `sales_manager/models.py`

Định nghĩa các lớp bản ghi:

- `Product`: sản phẩm.
- `Customer`: khách hàng.
- `Invoice`: hóa đơn.
- `InvoiceItem`: chi tiết hóa đơn.
- `InvoiceLineInput`: dòng nhập khi lập hóa đơn.
- `ProductSaleStat`: thống kê sản phẩm bán chạy.

Mỗi lớp dữ liệu có hàm chuyển đổi giữa object và dòng text để đọc/ghi file.

### 7.3. `sales_manager/storage.py`

Phụ trách:

- Tạo file dữ liệu nếu chưa tồn tại.
- Đọc dữ liệu từ file text vào `DynamicArray`.
- Ghi `DynamicArray` ra file text.

### 7.4. `sales_manager/manager.py`

Đây là lớp nghiệp vụ chính:

- Nạp dữ liệu và xây dựng bảng băm.
- Thêm, sửa, xóa sản phẩm/khách hàng.
- Tìm kiếm và sắp xếp.
- Lập hóa đơn.
- Tính doanh thu, top sản phẩm, cảnh báo tồn kho.
- Xuất báo cáo text.

### 7.5. `sales_manager/cli.py`

Giao diện menu console:

- In menu.
- Nhận lựa chọn từ người dùng.
- Gọi lớp `SalesManager`.
- Hiển thị kết quả dạng bảng văn bản.

## 8. Giao diện menu

Menu chính:

```text
===== HE THONG QUAN LY BAN HANG =====
1. Xem danh sach san pham
2. Them san pham
3. Tim kiem san pham
4. Sap xep san pham
5. Xem danh sach khach hang
6. Them khach hang
7. Lap hoa don ban hang
8. Bao cao doanh thu
9. Top san pham ban chay
10. San pham sap het hang
11. Luu va tai lai du lieu
0. Thoat
```

Chương trình chạy lặp cho đến khi người dùng chọn `0`.

## 9. Kiểm thử

Kiểm thử được viết bằng `unittest`, đặt trong thư mục `tests`.

### 9.1. Bảng tình huống kiểm thử

| STT | Tình huống | Dữ liệu kiểm thử | Kết quả mong đợi |
| --- | --- | --- | --- |
| 1 | Thêm, xóa, sắp xếp mảng động | 3 sản phẩm giá 300, 100, 200 | Sau quick sort, thứ tự giá tăng dần; xóa đúng phần tử |
| 2 | Bảng băm thêm/cập nhật/xóa | Khóa `SP001`, `SP002` | Tra cứu đúng, cập nhật không tăng kích thước, xóa thành công |
| 3 | Lập hóa đơn hợp lệ | KH001 mua SP001 số lượng 2 và SP005 số lượng 1 | Sinh hóa đơn HD0001, tồn kho SP001 giảm 2, dữ liệu lưu được |
| 4 | Bán vượt tồn kho | SP004 số lượng 999 | Chương trình báo lỗi, không tạo hóa đơn |
| 5 | Tìm kiếm/sắp xếp/xuất báo cáo | Từ khóa Laptop, sắp xếp giá giảm dần | Tìm được 2 laptop, SP004 đứng đầu, báo cáo có sản phẩm đã bán |

### 9.2. Kết quả kiểm thử

Lệnh chạy:

```powershell
python -m unittest discover -s tests
```

Kết quả:

```text
Ran 5 tests
OK
```

## 10. Hướng dẫn chạy chương trình

### 10.1. Chạy menu

```powershell
python -m sales_manager.cli menu
```

Hoặc nhấp đúp:

```text
run_sales_manager.bat
```

### 10.2. Tạo dữ liệu demo

```powershell
python -m sales_manager.cli --data-dir data/demo demo
```

Lệnh này sao chép dữ liệu mẫu sang `data/demo`, tạo 3 hóa đơn mẫu và xuất báo cáo text.

### 10.3. Xem tổng quan

```powershell
python -m sales_manager.cli --data-dir data/demo summary
```

### 10.4. Xuất báo cáo text

```powershell
python -m sales_manager.cli --data-dir data/demo report
```

## 11. Kết quả demo

Sau khi chạy `demo`, chương trình tạo:

- `data/demo/products.txt`: sản phẩm sau khi đã giảm tồn kho theo hóa đơn.
- `data/demo/invoices.txt`: 3 hóa đơn mẫu.
- `data/demo/invoice_items.txt`: các dòng chi tiết hóa đơn.
- `output/sales_report.txt`: báo cáo doanh thu và top sản phẩm bán chạy.

Ví dụ tổng quan:

```text
Tong quan du lieu
- San pham: 8
- Khach hang: 4
- Hoa don: 3
- Chi tiet hoa don: 6
- Doanh thu: 25.770.733 VND
```

Số tiền trên được lấy từ lần chạy demo hiện tại với 3 hóa đơn mẫu.

## 12. Tổng kết kỹ thuật đã vận dụng

Các kỹ thuật đã vận dụng:

- Thiết kế chương trình theo module.
- Tự cài đặt cấu trúc dữ liệu: mảng động, danh sách liên kết, bảng băm.
- Tự cài đặt thuật toán tìm kiếm và sắp xếp.
- Xử lý file text có cấu trúc.
- Xử lý nghiệp vụ có ràng buộc: không cho bán vượt tồn kho, tính VAT, chiết khấu.
- Thiết kế master-detail cho hóa đơn và chi tiết hóa đơn.
- Viết kiểm thử tự động bằng `unittest`.
- Đóng gói chương trình và báo cáo để nộp.

## 13. Hạn chế và hướng phát triển

Hạn chế:

- Chương trình dùng giao diện console, chưa có giao diện đồ họa.
- Chưa có phân quyền người dùng.
- Chưa có chức năng nhập hàng riêng; tồn kho ban đầu được quản lý qua file sản phẩm và giảm khi bán.
- Bảng băm dùng kích thước cố định, chưa tự động rehash khi tải cao.

Hướng phát triển:

- Bổ sung chức năng nhập hàng và nhật ký nhập/xuất kho.
- Bổ sung giao diện đồ họa bằng Tkinter.
- Thêm thống kê theo khoảng ngày do người dùng chọn.
- Thêm rehash cho `HashTable`.
- Xuất hóa đơn ra PDF riêng.

## 14. Phụ lục mã nguồn quan trọng

### 14.1. Hàm main

File: `sales_manager/cli.py`

```python
def main() -> None:
    parser = argparse.ArgumentParser(description="He thong quan ly ban hang DSA")
    parser.add_argument("--data-dir", default=str(DEFAULT_DATA_DIR), help="Thu muc chua file du lieu text")
    subparsers = parser.add_subparsers(dest="command")
    subparsers.add_parser("menu", help="Mo menu console")
    subparsers.add_parser("summary", help="In tong quan du lieu")
    subparsers.add_parser("report", help="Xuat bao cao text")
    subparsers.add_parser("demo", help="Tao du lieu demo va 3 hoa don mau")
    args = parser.parse_args()
```

### 14.2. Hàm lập hóa đơn

File: `sales_manager/manager.py`

```python
def create_invoice(self, customer_id, lines, discount_percent=0.0, vat_percent=8.0):
    customer = self.customer_index.get(customer_id)
    if customer is None:
        raise SalesError("Khong tim thay khach hang")
    for line in lines:
        product = self.product_index.get(line.sku)
        if product is None:
            raise SalesError("Khong tim thay san pham")
        if product.stock < line.quantity:
            raise SalesError("Khong du ton kho")
    # tinh tien, tao hoa don, tru ton kho, luu file
```

### 14.3. Hàm băm chuỗi

File: `sales_manager/data_structures.py`

```python
def _hash(self, key: str) -> int:
    value = 0
    for ch in key:
        value = (value * 31 + ord(ch)) % self._capacity
    return value
```

## 15. Kết luận

Chương trình đã đáp ứng yêu cầu chính của chủ đề quản lý bán hàng: quản lý sản phẩm, quản lý khách hàng, lập hóa đơn master-detail, tính chiết khấu/VAT/tổng tiền, lưu dữ liệu bằng file text và tạo các báo cáo cơ bản. Về mặt môn học, chương trình vận dụng trực tiếp các cấu trúc dữ liệu và thuật toán tự cài đặt thay vì dựa vào cấu trúc dữ liệu có sẵn của ngôn ngữ.
