# ĐẠI HỌC BÁCH KHOA HÀ NỘI
# TRƯỜNG CÔNG NGHỆ THÔNG TIN VÀ TRUYỀN THÔNG
# KHOA KHOA HỌC MÁY TÍNH


# BÁO CÁO BÀI TẬP LỚN
## HỌC PHẦN: CẤU TRÚC DỮ LIỆU VÀ GIẢI THUẬT
## ĐỀ TÀI: HỆ THỐNG QUẢN LÝ BÁN HÀNG


Nhóm thực hiện: Nhóm 15

Giảng viên hướng dẫn: Vũ Thành Nam

Repository GitHub: https://github.com/nhtameo/quan-ly-ban-hang-dsa


Thành viên nhóm:

Nguyễn Trịnh Mai Phương - 202418965

Trần Minh Quân - 202418973


Hà Nội, tháng 06 năm 2026

---

## MỤC LỤC

- Thông tin đề tài và phân công nhóm.
- Tổng quan bài toán.
- Phân tích yêu cầu.
- Thiết kế dữ liệu lưu trữ.
- Thiết kế cấu trúc dữ liệu và thuật toán.
- Thiết kế chương trình.
- Cài đặt chức năng chính.
- Kiểm thử và đánh giá kết quả.
- Hướng dẫn chạy chương trình.
- Kết luận và hướng phát triển.
- Phụ lục mã nguồn tiêu biểu.

## DANH MỤC TỪ VIẾT TẮT

| Từ viết tắt | Ý nghĩa |
| --- | --- |
| CTDL | Cấu trúc dữ liệu |
| GT | Giải thuật |
| SKU | Stock Keeping Unit - mã sản phẩm |
| VAT | Thuế giá trị gia tăng |
| CLI | Command Line Interface - giao diện dòng lệnh |

---

## 1. THÔNG TIN ĐỀ TÀI VÀ PHÂN CÔNG NHÓM

### 1.1. Thông tin đề tài

Tên đề tài: Hệ thống quản lý bán hàng.  
Chủ đề trong danh sách project: Chủ đề 4 - Quản lý bán hàng.  
Ngôn ngữ lập trình: Python.  
Kiểu giao diện: Menu console.  
Hình thức lưu trữ: File text có cấu trúc.  
Link GitHub: https://github.com/nhtameo/quan-ly-ban-hang-dsa.

### 1.2. Thành viên và phân công

| STT | Họ tên | MSSV | Vai trò chính |
| --- | --- | --- | --- |
| 1 | Nguyễn Trịnh Mai Phương | 202418965 | Thiết kế chương trình, thiết kế dữ liệu, viết báo cáo. |
| 2 | Trần Minh Quân | 202418973 | Kiểm thử, chuẩn bị demo, viết báo cáo, hỗ trợ GitHub. |

Phân công chi tiết:

- Nguyễn Trịnh Mai Phương: nhóm trưởng; phân tích yêu cầu; thiết kế chương trình; thiết kế cấu trúc dữ liệu lưu trữ; cài đặt luồng đọc/ghi dữ liệu; viết các phần tổng quan, phân tích, thiết kế trong báo cáo; rà soát định dạng báo cáo Word/PDF.
- Trần Minh Quân: cài đặt và kiểm thử cấu trúc dữ liệu; xây dựng kịch bản test; kiểm thử chức năng lập hóa đơn, báo cáo, lưu file; chuẩn bị dữ liệu demo; viết phần kiểm thử, đánh giá, hướng dẫn chạy; hỗ trợ đóng gói zip và đưa mã nguồn lên GitHub.

Tỷ lệ đóng góp được chia cân bằng. Mai Phương phụ trách trọng tâm phần thiết kế và dữ liệu, Minh Quân phụ trách trọng tâm phần kiểm thử và đánh giá; cả hai cùng tham gia viết báo cáo và hoàn thiện sản phẩm bàn giao.

### 1.3. Sản phẩm bàn giao

- Thư mục mã nguồn `sales_manager`.
- Dữ liệu mẫu trong `data/sample`.
- Báo cáo Word `report/report.docx`.
- Báo cáo PDF `report/report.pdf`.
- Outline slide `report/slide-outline.md`.
- File nén bàn giao `release/QuanLyBanHang_DSA.zip`.
- Repository GitHub công khai: https://github.com/nhtameo/quan-ly-ban-hang-dsa.

## 2. TỔNG QUAN BÀI TOÁN

### 2.1. Bối cảnh

Trong hoạt động bán lẻ, cửa hàng cần quản lý danh mục sản phẩm, thông tin khách hàng, các hóa đơn bán hàng và báo cáo doanh thu. Nếu quản lý thủ công bằng sổ hoặc bảng tính, dữ liệu dễ bị sai lệch: tồn kho không được cập nhật kịp thời, hóa đơn thiếu chi tiết, doanh thu khó tổng hợp theo ngày/tháng và khó xác định mặt hàng bán chạy.

Đề tài xây dựng một chương trình quản lý bán hàng ở mức cơ bản nhưng có đầy đủ các nghiệp vụ chính: quản lý sản phẩm, quản lý khách hàng, lập hóa đơn, lưu hóa đơn và chi tiết hóa đơn, tính chiết khấu/VAT/tổng tiền, thống kê doanh thu và top sản phẩm bán chạy.

### 2.2. Mục tiêu

Chương trình hướng tới các mục tiêu sau:

- Cung cấp menu đơn giản để người dùng thao tác liên tục cho đến khi chọn thoát.
- Lưu trữ dữ liệu trong file text, đúng yêu cầu học phần.
- Không sử dụng cơ sở dữ liệu hay cấu trúc dữ liệu nâng cao có sẵn cho phần nghiệp vụ.
- Tự cài đặt và vận dụng các cấu trúc dữ liệu: mảng động, danh sách liên kết, bảng băm.
- Tự cài đặt thuật toán tìm kiếm và sắp xếp.
- Bảo đảm nghiệp vụ bán hàng không làm tồn kho âm.
- Có kiểm thử tự động để chứng minh các luồng chính hoạt động đúng.

### 2.3. Phạm vi

Phạm vi đã cài đặt:

- Quản lý danh mục sản phẩm.
- Quản lý danh sách khách hàng.
- Lập hóa đơn bán hàng nhiều dòng.
- Tự động giảm tồn kho sau khi lập hóa đơn.
- Lưu hóa đơn theo mô hình master-detail.
- Báo cáo doanh thu theo ngày/tháng.
- Thống kê top 10 sản phẩm bán chạy.
- Liệt kê sản phẩm sắp hết hàng.
- Xuất báo cáo text.

Phạm vi chưa cài đặt:

- Phân quyền người dùng.
- Giao diện đồ họa.
- Quản lý nhập kho riêng biệt.
- In từng hóa đơn ra PDF riêng.

## 3. PHÂN TÍCH YÊU CẦU

### 3.1. Yêu cầu chức năng

#### 3.1.1. Quản lý sản phẩm

Mỗi sản phẩm gồm:

- Mã sản phẩm.
- Tên sản phẩm.
- Đơn vị tính.
- Loại sản phẩm.
- Đơn giá bán.
- Số lượng tồn kho.
- Ngưỡng tồn kho tối thiểu.

Các chức năng:

- Xem danh sách sản phẩm.
- Thêm sản phẩm mới.
- Cập nhật sản phẩm ở lớp nghiệp vụ.
- Xóa sản phẩm ở lớp nghiệp vụ.
- Tìm kiếm sản phẩm theo mã, tên hoặc loại.
- Sắp xếp sản phẩm theo mã, tên, giá hoặc tồn kho.
- Liệt kê sản phẩm sắp hết hàng.

#### 3.1.2. Quản lý khách hàng

Mỗi khách hàng gồm:

- Mã khách hàng.
- Họ tên.
- Số điện thoại.
- Địa chỉ.

Các chức năng:

- Xem danh sách khách hàng.
- Thêm khách hàng mới.
- Cập nhật khách hàng ở lớp nghiệp vụ.
- Xóa khách hàng nếu chưa có hóa đơn.
- Tìm kiếm khách hàng theo mã, tên hoặc số điện thoại.

#### 3.1.3. Lập hóa đơn

Hóa đơn bán hàng cần hỗ trợ:

- Chọn khách hàng theo mã.
- Nhập nhiều sản phẩm trong cùng một hóa đơn.
- Kiểm tra mã sản phẩm tồn tại.
- Kiểm tra số lượng tồn kho trước khi bán.
- Tính tạm tính, chiết khấu, VAT và tổng thanh toán.
- Tạo mã hóa đơn tự động.
- Lưu phần đầu hóa đơn và chi tiết hóa đơn.
- Giảm tồn kho sản phẩm sau khi bán thành công.

#### 3.1.4. Báo cáo

Các báo cáo cần có:

- Tổng quan dữ liệu: số sản phẩm, số khách hàng, số hóa đơn, doanh thu.
- Doanh thu theo ngày.
- Doanh thu theo tháng.
- Top 10 sản phẩm bán chạy nhất.
- Sản phẩm có tồn kho nhỏ hơn hoặc bằng ngưỡng tối thiểu.

### 3.2. Yêu cầu phi chức năng

- Dễ chạy trên máy cá nhân: chỉ cần Python, không cần cài thêm thư viện để chạy chương trình chính.
- Dữ liệu lưu được sau khi tắt chương trình.
- Mã nguồn tách module rõ ràng, dễ đọc, dễ kiểm thử.
- Có dữ liệu mẫu để người chấm chạy nhanh.
- Có test tự động.
- Báo cáo trình bày theo bố cục đồ án: bìa, mục lục, phân công, phân tích, thiết kế, cài đặt, kiểm thử, kết luận, phụ lục.

## 4. THIẾT KẾ DỮ LIỆU LƯU TRỮ

### 4.1. Nguyên tắc thiết kế

Theo yêu cầu học phần, dữ liệu được lưu trong file text. Mỗi file gồm một dòng tiêu đề và nhiều dòng bản ghi. Các trường trong một bản ghi được phân tách bằng ký tự `|`. Cách tổ chức này đủ đơn giản để đọc/ghi thủ công, đồng thời vẫn thể hiện rõ cấu trúc dữ liệu.

Chương trình sử dụng 4 file chính:

- `products.txt`: lưu danh mục sản phẩm.
- `customers.txt`: lưu danh sách khách hàng.
- `invoices.txt`: lưu đầu hóa đơn.
- `invoice_items.txt`: lưu chi tiết hóa đơn.

### 4.2. File sản phẩm

Tên file: `data/sample/products.txt`

```text
sku|name|unit|category|price|stock|min_stock
SP001|Dien thoai Alpha A1|chiec|Dien thoai|4990000|35|5
```

Ý nghĩa:

- `sku`: mã sản phẩm, khóa logic của sản phẩm.
- `name`: tên sản phẩm.
- `unit`: đơn vị tính.
- `category`: loại sản phẩm.
- `price`: đơn giá bán.
- `stock`: số lượng tồn kho.
- `min_stock`: ngưỡng tồn kho tối thiểu để cảnh báo.

### 4.3. File khách hàng

Tên file: `data/sample/customers.txt`

```text
customer_id|name|phone|address
KH001|Nguyen Van An|0901000001|Cau Giay, Ha Noi
```

### 4.4. File hóa đơn

Tên file: `data/sample/invoices.txt`

```text
invoice_id|customer_id|customer_name|created_at|discount_percent|vat_percent|subtotal|vat_amount|total
HD0001|KH001|Nguyen Van An|2026-06-22 00:00:00|2.00|8.00|5388000|422419|5810419
```

### 4.5. File chi tiết hóa đơn

Tên file: `data/sample/invoice_items.txt`

```text
invoice_id|sku|product_name|quantity|unit_price|line_total
HD0001|SP001|Dien thoai Alpha A1|1|4990000|4990000
```

### 4.6. Mô hình master-detail

Hóa đơn được thiết kế theo mô hình master-detail:

- Master: `Invoice` trong file `invoices.txt`.
- Detail: `InvoiceItem` trong file `invoice_items.txt`.
- Một hóa đơn có thể có nhiều dòng chi tiết.
- Mỗi dòng chi tiết thuộc đúng một hóa đơn thông qua `invoice_id`.

Thiết kế này giúp lưu được đầy đủ lịch sử bán hàng. Tên sản phẩm và đơn giá được ghi vào chi tiết hóa đơn tại thời điểm bán, vì vậy hóa đơn cũ không bị thay đổi nếu sau này cập nhật tên hoặc giá sản phẩm trong danh mục.

## 5. THIẾT KẾ CẤU TRÚC DỮ LIỆU VÀ THUẬT TOÁN

### 5.1. Mảng động `DynamicArray`

`DynamicArray` được cài đặt trong `sales_manager/data_structures.py`. Đây là cấu trúc dữ liệu chính để lưu các danh sách nghiệp vụ.

Vai trò:

- Lưu danh sách sản phẩm.
- Lưu danh sách khách hàng.
- Lưu danh sách hóa đơn.
- Lưu danh sách chi tiết hóa đơn.
- Lưu kết quả tìm kiếm và kết quả báo cáo.

Các thao tác:

| Thao tác | Ý nghĩa | Độ phức tạp |
| --- | --- | --- |
| `append` | Thêm cuối mảng | O(1) trung bình |
| `get` | Truy cập theo chỉ số | O(1) |
| `set` | Cập nhật theo chỉ số | O(1) |
| `insert` | Chèn vào vị trí bất kỳ | O(n) |
| `remove_at` | Xóa theo vị trí | O(n) |
| `copy` | Sao chép mảng | O(n) |

### 5.2. Danh sách liên kết `LinkedList`

`LinkedList` là danh sách liên kết đơn, dùng làm bucket trong bảng băm. Mỗi node lưu một cặp khóa-giá trị và con trỏ tới node tiếp theo.

Vai trò:

- Xử lý va chạm trong bảng băm.
- Cho phép nhiều khóa cùng rơi vào một bucket.

Độ phức tạp:

- Thêm đầu bucket: O(1).
- Tìm trong bucket: O(k), với k là số phần tử trong bucket.

### 5.3. Bảng băm `HashTable`

`HashTable` được tự cài đặt, không dùng `dict` cho dữ liệu nghiệp vụ. Bảng băm dùng mảng bucket, mỗi bucket là một `LinkedList`.

Vai trò:

- Tra cứu sản phẩm theo `sku`.
- Tra cứu khách hàng theo `customer_id`.
- Gom nhóm doanh thu theo ngày/tháng.
- Gom nhóm sản phẩm bán chạy theo mã sản phẩm.

Hàm băm chuỗi:

```text
hash = (hash * 31 + ASCII(character)) mod capacity
```

Độ phức tạp:

- Trung bình: thêm, xóa, tra cứu O(1).
- Trường hợp xấu: O(n) nếu nhiều khóa va chạm cùng bucket.

### 5.4. Tìm kiếm tuyến tính

Tìm kiếm tuyến tính được dùng khi người dùng nhập từ khóa không chính xác hoàn toàn, ví dụ tìm theo một phần tên sản phẩm hoặc loại sản phẩm.

Giả mã:

```text
linear_search(array, predicate):
    result = DynamicArray()
    for item in array:
        if predicate(item):
            result.append(item)
    return result
```

Độ phức tạp: O(n).

### 5.5. Quick sort

Quick sort được dùng để sắp xếp danh sách sản phẩm và thống kê top sản phẩm bán chạy.

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

### 5.6. Thuật toán lập hóa đơn

Giả mã:

```text
create_invoice(customer_id, lines, discount_percent, vat_percent):
    customer = customer_hash.get(customer_id)
    if customer is None:
        raise error

    subtotal = 0
    for line in lines:
        product = product_hash.get(line.sku)
        if product is None:
            raise error
        if product.stock < line.quantity:
            raise error
        subtotal += product.price * line.quantity

    discount = subtotal * discount_percent / 100
    vat = (subtotal - discount) * vat_percent / 100
    total = subtotal - discount + vat

    create invoice
    for line in lines:
        create invoice item
        product.stock -= line.quantity

    save all data files
```

Nếu hóa đơn có k dòng hàng, thời gian xử lý chính là O(k) sau khi bảng băm sản phẩm và khách hàng đã được xây dựng.

## 6. THIẾT KẾ CHƯƠNG TRÌNH

### 6.1. Kiến trúc module

| Module | Vai trò |
| --- | --- |
| `sales_manager/data_structures.py` | Cài đặt `DynamicArray`, `LinkedList`, `HashTable`, tìm kiếm tuyến tính và quick sort. |
| `sales_manager/models.py` | Định nghĩa các lớp dữ liệu: `Product`, `Customer`, `Invoice`, `InvoiceItem`, `InvoiceLineInput`, `ProductSaleStat`. |
| `sales_manager/storage.py` | Đọc/ghi dữ liệu từ các file text. |
| `sales_manager/manager.py` | Xử lý nghiệp vụ: quản lý sản phẩm, khách hàng, lập hóa đơn, báo cáo. |
| `sales_manager/cli.py` | Giao diện menu console và các lệnh demo/report. |
| `tests/test_sales_manager.py` | Kiểm thử cấu trúc dữ liệu và nghiệp vụ chính. |

### 6.2. Luồng chạy tổng quát

```text
File text -> Storage -> DynamicArray -> HashTable index -> SalesManager -> CLI -> File text/Báo cáo
```

Diễn giải:

1. `Storage` đọc dữ liệu từ file text.
2. Dữ liệu được đưa vào các `DynamicArray`.
3. `SalesManager` xây dựng bảng băm cho sản phẩm và khách hàng.
4. Người dùng thao tác qua menu CLI.
5. Nghiệp vụ được xử lý trong `SalesManager`.
6. Sau thao tác thay đổi dữ liệu, chương trình ghi lại file text.

### 6.3. Menu chương trình

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

Menu chạy trong vòng lặp. Khi người dùng chọn `0`, chương trình lưu dữ liệu và kết thúc.

## 7. CÀI ĐẶT CHỨC NĂNG CHÍNH

### 7.1. Quản lý sản phẩm

Chức năng quản lý sản phẩm dùng `DynamicArray` để lưu danh sách và `HashTable` để tra cứu nhanh theo mã sản phẩm.

Các hàm chính:

- `add_product(product)`.
- `update_product(product)`.
- `delete_product(sku)`.
- `find_products(keyword)`.
- `sorted_products(field, reverse)`.
- `low_stock_products()`.

### 7.2. Quản lý khách hàng

Danh sách khách hàng cũng được lưu bằng `DynamicArray`, đồng thời tạo chỉ mục `HashTable` theo `customer_id`.

Các hàm chính:

- `add_customer(customer)`.
- `update_customer(customer)`.
- `delete_customer(customer_id)`.
- `find_customers(keyword)`.

### 7.3. Lập hóa đơn

Chức năng lập hóa đơn là nghiệp vụ quan trọng nhất. Chương trình kiểm tra các ràng buộc trước khi ghi dữ liệu:

- Khách hàng phải tồn tại.
- Sản phẩm phải tồn tại.
- Số lượng bán phải lớn hơn 0.
- Số lượng bán không được vượt tồn kho.
- Chiết khấu và VAT phải nằm trong khoảng hợp lệ.

Sau khi hợp lệ:

- Chương trình sinh mã hóa đơn mới dạng `HD0001`, `HD0002`, ...
- Tạo bản ghi `Invoice`.
- Tạo các bản ghi `InvoiceItem`.
- Giảm tồn kho sản phẩm.
- Lưu dữ liệu vào file text.

### 7.4. Báo cáo doanh thu

Báo cáo doanh thu sử dụng `HashTable` để gom nhóm theo ngày hoặc tháng:

- Khóa là chuỗi ngày `YYYY-MM-DD` hoặc tháng `YYYY-MM`.
- Giá trị là đối tượng `RevenueRow`, lưu số hóa đơn và tổng doanh thu.
- Sau khi gom nhóm, kết quả được sắp xếp giảm dần theo thời gian.

### 7.5. Top sản phẩm bán chạy

Top sản phẩm bán chạy được tính từ danh sách `InvoiceItem`:

1. Duyệt toàn bộ chi tiết hóa đơn.
2. Gom nhóm theo `sku` bằng `HashTable`.
3. Cộng dồn số lượng và doanh thu từng sản phẩm.
4. Sắp xếp giảm dần theo số lượng bán bằng quick sort.
5. Lấy tối đa 10 sản phẩm đầu tiên.

## 8. KIỂM THỬ VÀ ĐÁNH GIÁ KẾT QUẢ

### 8.1. Chiến lược kiểm thử

Nhóm sử dụng `unittest` để kiểm thử tự động. Các test tập trung vào hai nhóm:

- Kiểm thử cấu trúc dữ liệu: mảng động, bảng băm, quick sort.
- Kiểm thử nghiệp vụ: lập hóa đơn, kiểm tra tồn kho, tìm kiếm, sắp xếp, xuất báo cáo.

### 8.2. Bảng test case

| STT | Tình huống | Dữ liệu kiểm thử | Kết quả mong đợi |
| --- | --- | --- | --- |
| 1 | Mảng động thêm, xóa, sắp xếp | 3 sản phẩm có giá 300, 100, 200 | Sau quick sort, thứ tự giá tăng dần; xóa đúng phần tử ở giữa. |
| 2 | Bảng băm thêm/cập nhật/xóa | Khóa `SP001`, `SP002` | Tra cứu đúng; cập nhật không làm tăng kích thước; xóa thành công. |
| 3 | Lập hóa đơn hợp lệ | KH001 mua SP001 số lượng 2 và SP005 số lượng 1 | Sinh hóa đơn `HD0001`; tồn kho SP001 giảm 2; dữ liệu lưu được. |
| 4 | Bán vượt tồn kho | SP004 số lượng 999 | Chương trình báo lỗi và không tạo hóa đơn. |
| 5 | Tìm kiếm, sắp xếp, xuất báo cáo | Từ khóa Laptop, sắp xếp giá giảm dần | Tìm được 2 laptop; SP004 đứng đầu; báo cáo có sản phẩm đã bán. |

### 8.3. Kết quả chạy test

Lệnh chạy:

```powershell
python -m unittest discover -s tests
```

Kết quả:

```text
.....
----------------------------------------------------------------------
Ran 5 tests

OK
```

### 8.4. Kết quả demo

Lệnh tạo demo:

```powershell
python -m sales_manager.cli --data-dir data/demo demo
```

Kết quả tổng quan:

```text
Tong quan du lieu
- San pham: 8
- Khach hang: 4
- Hoa don: 3
- Chi tiet hoa don: 6
- Doanh thu: 25.770.733 VND
```

Các file được tạo sau demo:

- `data/demo/products.txt`: sản phẩm sau khi đã giảm tồn kho.
- `data/demo/invoices.txt`: 3 hóa đơn mẫu.
- `data/demo/invoice_items.txt`: 6 dòng chi tiết hóa đơn.
- `output/sales_report.txt`: báo cáo doanh thu và top sản phẩm bán chạy.

### 8.5. Đánh giá

Chương trình đáp ứng các yêu cầu cốt lõi của đề tài. Các nghiệp vụ chính đều có kiểm thử. Thiết kế dữ liệu rõ ràng, dễ kiểm tra bằng mắt thường vì dùng file text. Việc tự cài đặt cấu trúc dữ liệu giúp thể hiện đúng nội dung học phần Cấu trúc dữ liệu và Giải thuật.

Một số giới hạn còn tồn tại:

- Giao diện console chưa thân thiện bằng giao diện đồ họa.
- Chưa có chức năng nhập kho riêng.
- Bảng băm chưa tự động mở rộng khi số lượng bản ghi tăng lớn.
- Chưa có chức năng lọc báo cáo theo khoảng ngày tùy chọn.

## 9. HƯỚNG DẪN CHẠY CHƯƠNG TRÌNH

### 9.1. Yêu cầu môi trường

- Python 3.10 trở lên.
- Không cần cài thêm thư viện ngoài để chạy chương trình chính.

### 9.2. Chạy menu chính

```powershell
python -m sales_manager.cli menu
```

Hoặc nhấp đúp file:

```text
run_sales_manager.bat
```

### 9.3. Tạo dữ liệu demo

```powershell
python -m sales_manager.cli --data-dir data/demo demo
```

### 9.4. Xem tổng quan dữ liệu

```powershell
python -m sales_manager.cli --data-dir data/demo summary
```

### 9.5. Xuất báo cáo text

```powershell
python -m sales_manager.cli --data-dir data/demo report
```

### 9.6. Chạy kiểm thử

```powershell
python -m unittest discover -s tests
```

## 10. KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN

### 10.1. Kết luận

Bài tập đã xây dựng được hệ thống quản lý bán hàng cơ bản bằng Python, có menu console, lưu dữ liệu bằng file text và vận dụng các cấu trúc dữ liệu tự cài đặt. Chương trình đáp ứng các yêu cầu chính: quản lý sản phẩm, quản lý khách hàng, lập hóa đơn master-detail, tính chiết khấu/VAT/tổng tiền, cập nhật tồn kho và thống kê doanh thu.

Về mặt học phần, sản phẩm thể hiện được việc áp dụng mảng động, danh sách liên kết, bảng băm, tìm kiếm tuyến tính và quick sort vào một bài toán quản lý thực tế.

### 10.2. Hướng phát triển

Các hướng phát triển tiếp theo:

- Bổ sung chức năng nhập kho và nhật ký nhập/xuất.
- Bổ sung giao diện đồ họa bằng Tkinter.
- Thêm báo cáo theo khoảng thời gian do người dùng chọn.
- Cài đặt rehash cho `HashTable` khi hệ số tải tăng cao.
- Xuất hóa đơn riêng ra PDF.
- Bổ sung sao lưu và phục hồi dữ liệu.

## 11. PHỤ LỤC MÃ NGUỒN TIÊU BIỂU

### 11.1. Hàm main

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

### 11.2. Hàm băm chuỗi

File: `sales_manager/data_structures.py`

```python
def _hash(self, key: str) -> int:
    value = 0
    for ch in key:
        value = (value * 31 + ord(ch)) % self._capacity
    return value
```

### 11.3. Ý tưởng hàm lập hóa đơn

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

    # Tinh tien, tao hoa don, tao chi tiet hoa don,
    # tru ton kho va luu lai file text.
```

## TÀI LIỆU THAM KHẢO

1. Tài liệu yêu cầu project 20252 của học phần Cấu trúc dữ liệu và Giải thuật.
2. Tài liệu Python chuẩn về xử lý file và kiểm thử `unittest`.
3. Bài giảng học phần Cấu trúc dữ liệu và Giải thuật.
