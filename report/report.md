# TRƯỜNG ĐẠI HỌC BÁCH KHOA HÀ NỘI
# KHOA TOÁN - TIN


# BÁO CÁO BÀI TẬP LỚN
## HỌC PHẦN: KĨ THUẬT LẬP TRÌNH
## ĐỀ TÀI: HỆ THỐNG QUẢN LÝ BÁN HÀNG


Sinh viên thực hiện: Nhóm 15

Giảng viên hướng dẫn: Vũ Thành Nam

Repository GitHub: https://github.com/nhtameo/quan-ly-ban-hang-dsa


Thành viên nhóm:

Nguyễn Trịnh Mai Phương - 202418965

Trần Minh Quân - 202418973


Hà Nội, tháng 06 năm 2026

---

## LỜI CẢM ƠN

Nhóm 15 xin gửi lời cảm ơn tới giảng viên Vũ Thành Nam đã cung cấp danh sách chủ đề, yêu cầu chung và định hướng thực hiện bài tập lớn học phần Kĩ thuật lập trình. Trong quá trình thực hiện đề tài, nhóm đã vận dụng kiến thức về tổ chức chương trình, xử lý file, xây dựng menu, kiểm thử, cấu trúc dữ liệu cơ bản và thuật toán sắp xếp/tìm kiếm. Báo cáo này trình bày kết quả xây dựng hệ thống quản lý bán hàng đơn giản, có dữ liệu file text, chương trình chạy được, kiểm thử và hướng dẫn sử dụng.

## TÓM TẮT NỘI DUNG

Đề tài xây dựng chương trình quản lý bán hàng bằng Python theo yêu cầu học phần Kĩ thuật lập trình. Chương trình hỗ trợ quản lý sản phẩm, quản lý khách hàng, lập hóa đơn bán hàng, tính chiết khấu, thuế VAT, tổng tiền thanh toán, tự động giảm tồn kho sau khi bán và lập báo cáo doanh thu. Dữ liệu được lưu trong các file text có cấu trúc, gồm `products.txt`, `customers.txt`, `invoices.txt` và `invoice_items.txt`. Các cấu trúc dữ liệu như `DynamicArray`, `LinkedList`, `HashTable`, thuật toán tìm kiếm tuyến tính và quick sort được nhóm tự cài đặt để phục vụ nghiệp vụ. Chương trình có menu console, dữ liệu mẫu, ảnh minh họa file dữ liệu, ảnh minh họa từng bước chạy và bộ kiểm thử tự động.

---

## MỤC LỤC

1. LỜI CẢM ƠN ........................................................................ 2

2. TÓM TẮT NỘI DUNG .............................................................. 2

3. DANH MỤC HÌNH VẼ .............................................................. 3

4. DANH MỤC BẢNG BIỂU ............................................................ 3

5. CHƯƠNG 1. TỔNG QUAN VÀ PHÂN TÍCH YÊU CẦU ............................. 5

6. CHƯƠNG 2. THIẾT KẾ DỮ LIỆU VÀ CẤU TRÚC DỮ LIỆU ..................... 8

7. CHƯƠNG 3. THIẾT KẾ VÀ CÀI ĐẶT CHƯƠNG TRÌNH .......................... 12

8. CHƯƠNG 4. KIỂM THỬ VÀ HƯỚNG DẪN ...................................... 15

9. KẾT LUẬN .......................................................................... 18

10. TÀI LIỆU THAM KHẢO ........................................................... 18

11. PHỤ LỤC .......................................................................... 18

## DANH MỤC HÌNH VẼ

- Hình 1.1. Sơ đồ tổng quan nghiệp vụ quản lý bán hàng.
- Hình 2.1. Minh họa file `products.txt`.
- Hình 2.2. Minh họa file `customers.txt`.
- Hình 2.3. Minh họa file `invoices.txt` sau khi tạo dữ liệu demo.
- Hình 2.4. Minh họa file `invoice_items.txt` sau khi tạo dữ liệu demo.
- Hình 2.5. Minh họa cách sử dụng cấu trúc dữ liệu trong chương trình.
- Hình 3.1. Sơ đồ kiến trúc module chương trình.
- Hình 3.2. Luồng xử lý chức năng lập hóa đơn.
- Hình 4.1. Mở menu chương trình.
- Hình 4.2. Tạo dữ liệu demo.
- Hình 4.3. Xem tổng quan dữ liệu.
- Hình 4.4. Chạy kiểm thử tự động.
- Hình 4.5. Minh họa repository GitHub.

## DANH MỤC BẢNG BIỂU

- Bảng 1.1. Phân công công việc nhóm 15.
- Bảng 2.1. Mô tả dữ liệu đầu vào file sản phẩm.
- Bảng 2.2. Mô tả dữ liệu đầu vào file khách hàng.
- Bảng 2.3. Mô tả dữ liệu đầu vào file hóa đơn.
- Bảng 2.4. Độ phức tạp cấu trúc dữ liệu và thuật toán.
- Bảng 4.1. Test case kiểm thử chương trình.

---

## CHƯƠNG 1. TỔNG QUAN VÀ PHÂN TÍCH YÊU CẦU

### 1.1. Thông tin đề tài

Tên đề tài: Hệ thống quản lý bán hàng.  
Chủ đề trong danh sách project: Chủ đề 4 - Quản lý bán hàng.  
Ngôn ngữ lập trình: Python.  
Kiểu giao diện: Menu console.  
Hình thức lưu trữ: File text có cấu trúc.  
Repository GitHub: https://github.com/nhtameo/quan-ly-ban-hang-dsa.

### 1.2. Thành viên và phân công

Bảng 1.1. Phân công công việc nhóm 15

| STT | Họ tên | MSSV | Vai trò chính |
| --- | --- | --- | --- |
| 1 | Nguyễn Trịnh Mai Phương | 202418965 | Thiết kế chương trình, thiết kế dữ liệu, viết báo cáo. |
| 2 | Trần Minh Quân | 202418973 | Kiểm thử, chuẩn bị demo, viết báo cáo, hỗ trợ GitHub. |

Phân công chi tiết:

- Nguyễn Trịnh Mai Phương: nhóm trưởng; phân tích yêu cầu; thiết kế chương trình; thiết kế cấu trúc dữ liệu lưu trữ; cài đặt luồng đọc/ghi dữ liệu; viết các phần tổng quan, phân tích, thiết kế trong báo cáo; rà soát định dạng báo cáo Word/PDF.
- Trần Minh Quân: cài đặt và kiểm thử cấu trúc dữ liệu; xây dựng kịch bản test; kiểm thử chức năng lập hóa đơn, báo cáo, lưu file; chuẩn bị dữ liệu demo; viết phần kiểm thử, đánh giá, hướng dẫn chạy; hỗ trợ đóng gói và đưa mã nguồn lên GitHub.

Tỷ lệ đóng góp được chia cân bằng. Mai Phương phụ trách trọng tâm phần thiết kế và dữ liệu, Minh Quân phụ trách trọng tâm phần kiểm thử và đánh giá; cả hai cùng tham gia viết báo cáo và hoàn thiện sản phẩm bàn giao.

### 1.3. Bối cảnh bài toán

Trong hoạt động bán hàng, cửa hàng cần quản lý danh mục sản phẩm, thông tin khách hàng, hóa đơn và doanh thu. Nếu quản lý bằng sổ hoặc bảng tính đơn giản, dữ liệu dễ bị sai lệch: tồn kho không cập nhật kịp thời, hóa đơn thiếu chi tiết, doanh thu khó tổng hợp và khó xác định mặt hàng bán chạy. Vì vậy cần một chương trình nhỏ giúp quản lý các nghiệp vụ bán hàng cơ bản.

![Hình 1.1. Sơ đồ tổng quan nghiệp vụ quản lý bán hàng](report/assets/overview_flow.png)

Chú thích: Sơ đồ thể hiện chuỗi nghiệp vụ chính của hệ thống, từ dữ liệu sản phẩm/khách hàng, lập hóa đơn đến cập nhật tồn kho và lập báo cáo doanh thu.

### 1.4. Mục tiêu

Mục tiêu của đề tài:

- Xây dựng chương trình có menu để người dùng lựa chọn tác vụ.
- Lưu dữ liệu vào file text theo đúng yêu cầu học phần.
- Quản lý được sản phẩm, khách hàng, hóa đơn và chi tiết hóa đơn.
- Tính được chiết khấu, VAT và tổng tiền thanh toán.
- Cập nhật tồn kho sau khi bán.
- Thống kê doanh thu theo ngày/tháng và top sản phẩm bán chạy.
- Tự cài đặt cấu trúc dữ liệu và thuật toán, không phụ thuộc vào cơ sở dữ liệu.

### 1.5. Yêu cầu chức năng

Các chức năng chính:

- Quản lý sản phẩm: xem danh sách, thêm, cập nhật/xóa ở lớp nghiệp vụ, tìm kiếm, sắp xếp, cảnh báo sắp hết hàng.
- Quản lý khách hàng: xem danh sách, thêm, cập nhật/xóa ở lớp nghiệp vụ, tìm kiếm theo mã/tên/số điện thoại.
- Lập hóa đơn: chọn khách hàng, nhập nhiều sản phẩm, kiểm tra tồn kho, tính tạm tính, chiết khấu, VAT, tổng tiền.
- Lưu hóa đơn master-detail: đầu hóa đơn lưu ở `invoices.txt`, chi tiết hóa đơn lưu ở `invoice_items.txt`.
- Báo cáo: doanh thu theo ngày/tháng, top 10 sản phẩm bán chạy, sản phẩm sắp hết hàng.

### 1.6. Yêu cầu phi chức năng

- Chạy được bằng Python trên máy cá nhân.
- Không cần cài đặt cơ sở dữ liệu.
- Dữ liệu được lưu lại sau khi thoát chương trình.
- Mã nguồn tách module rõ ràng.
- Có dữ liệu mẫu và kiểm thử tự động.

---

## CHƯƠNG 2. THIẾT KẾ DỮ LIỆU VÀ CẤU TRÚC DỮ LIỆU

### 2.1. Tổ chức file dữ liệu

Chương trình sử dụng dữ liệu đầu vào dạng file text. Mỗi file có một dòng tiêu đề và các dòng dữ liệu. Các trường được phân tách bằng ký tự `|`. Cách lưu này giúp dễ đọc bằng mắt thường, dễ kiểm tra, đồng thời vẫn đủ rõ ràng để chương trình phân tích thành các đối tượng dữ liệu.

Các file dữ liệu chính:

- `products.txt`: danh mục sản phẩm.
- `customers.txt`: danh sách khách hàng.
- `invoices.txt`: đầu hóa đơn.
- `invoice_items.txt`: chi tiết hóa đơn.

### 2.2. Dữ liệu đầu vào file sản phẩm

Bảng 2.1. Mô tả dữ liệu đầu vào file sản phẩm

| Trường | Kiểu dữ liệu | Ý nghĩa | Ví dụ |
| --- | --- | --- | --- |
| `sku` | Chuỗi | Mã sản phẩm, dùng làm khóa tra cứu | SP001 |
| `name` | Chuỗi | Tên sản phẩm | Dien thoai Alpha A1 |
| `unit` | Chuỗi | Đơn vị tính | chiec |
| `category` | Chuỗi | Loại sản phẩm | Dien thoai |
| `price` | Số nguyên | Đơn giá bán | 4990000 |
| `stock` | Số nguyên | Số lượng tồn kho hiện tại | 35 |
| `min_stock` | Số nguyên | Ngưỡng tồn kho tối thiểu để cảnh báo | 5 |

![Hình 2.1. Minh họa file products.txt](report/assets/data_products.png)

Chú thích: File `products.txt` là dữ liệu đầu vào quan trọng nhất của chương trình. Mỗi dòng sau header tương ứng một sản phẩm. Trường `stock` được chương trình cập nhật giảm sau khi lập hóa đơn thành công.

### 2.3. Dữ liệu đầu vào file khách hàng

Bảng 2.2. Mô tả dữ liệu đầu vào file khách hàng

| Trường | Kiểu dữ liệu | Ý nghĩa | Ví dụ |
| --- | --- | --- | --- |
| `customer_id` | Chuỗi | Mã khách hàng, dùng làm khóa tra cứu | KH001 |
| `name` | Chuỗi | Họ tên khách hàng | Nguyen Van An |
| `phone` | Chuỗi | Số điện thoại | 0901000001 |
| `address` | Chuỗi | Địa chỉ liên hệ | Cau Giay, Ha Noi |

![Hình 2.2. Minh họa file customers.txt](report/assets/data_customers.png)

Chú thích: File `customers.txt` cung cấp dữ liệu khách hàng ban đầu. Khi lập hóa đơn, chương trình tra cứu khách hàng bằng `customer_id`.

### 2.4. Dữ liệu đầu ra và đầu vào tiếp theo của hóa đơn

Sau khi người dùng lập hóa đơn, chương trình ghi dữ liệu vào `invoices.txt` và `invoice_items.txt`. Các file này đồng thời là dữ liệu đầu vào cho những lần chạy sau, vì chương trình sẽ nạp lại hóa đơn cũ để tính doanh thu, top sản phẩm bán chạy và sinh mã hóa đơn tiếp theo.

Bảng 2.3. Mô tả dữ liệu đầu vào/đầu ra của hóa đơn

| File | Trường chính | Ý nghĩa |
| --- | --- | --- |
| `invoices.txt` | `invoice_id`, `customer_id`, `created_at`, `subtotal`, `vat_amount`, `total` | Lưu đầu hóa đơn, thông tin khách và tổng tiền |
| `invoice_items.txt` | `invoice_id`, `sku`, `quantity`, `unit_price`, `line_total` | Lưu từng dòng hàng trong hóa đơn |

![Hình 2.3. Minh họa file invoices.txt sau khi tạo dữ liệu demo](report/assets/data_invoices.png)

![Hình 2.4. Minh họa file invoice_items.txt sau khi tạo dữ liệu demo](report/assets/data_invoice_items.png)

Chú thích: Hai file hóa đơn thể hiện mô hình master-detail. `invoice_id` liên kết đầu hóa đơn với nhiều dòng chi tiết. Cách tách này giúp lưu được một hóa đơn có nhiều sản phẩm.

### 2.5. Cấu trúc dữ liệu sử dụng

#### 2.5.1. Mảng động `DynamicArray`

`DynamicArray` được tự cài đặt để lưu các danh sách nghiệp vụ: sản phẩm, khách hàng, hóa đơn, chi tiết hóa đơn, kết quả tìm kiếm và kết quả báo cáo. Khi số phần tử vượt sức chứa, mảng tự tăng kích thước.

#### 2.5.2. Danh sách liên kết `LinkedList`

`LinkedList` được dùng làm bucket trong bảng băm. Mỗi node lưu một cặp khóa-giá trị và con trỏ tới node tiếp theo. Khi có va chạm khóa trong bảng băm, các phần tử cùng bucket được nối bằng danh sách liên kết.

#### 2.5.3. Bảng băm `HashTable`

`HashTable` dùng để tra cứu nhanh sản phẩm theo `sku`, khách hàng theo `customer_id` và gom nhóm dữ liệu báo cáo. Hàm băm chuỗi được cài đặt theo công thức:

```text
hash = (hash * 31 + ASCII(character)) mod capacity
```

![Hình 2.5. Minh họa cách sử dụng cấu trúc dữ liệu trong chương trình](report/assets/data_structures_flow.png)

Chú thích: `DynamicArray` lưu danh sách dữ liệu, `HashTable` tạo chỉ mục tra cứu nhanh, còn `LinkedList` xử lý các phần tử va chạm trong cùng bucket của bảng băm.

### 2.6. Thuật toán sử dụng

Các thuật toán chính:

- Tìm kiếm tuyến tính: dùng khi tìm sản phẩm/khách hàng theo từ khóa gần đúng.
- Quick sort: dùng khi sắp xếp sản phẩm và top sản phẩm bán chạy.
- Thuật toán lập hóa đơn: kiểm tra dữ liệu, tính tiền, tạo hóa đơn, trừ tồn kho và lưu file.

Bảng 2.4. Độ phức tạp cấu trúc dữ liệu và thuật toán

| Thành phần | Chức năng | Độ phức tạp trung bình |
| --- | --- | --- |
| `DynamicArray.append` | Thêm phần tử cuối mảng | O(1) |
| `DynamicArray.get/set` | Truy cập/cập nhật theo chỉ số | O(1) |
| `HashTable.get/put` | Tra cứu/thêm theo khóa | O(1) |
| Tìm kiếm tuyến tính | Tìm theo từ khóa | O(n) |
| Quick sort | Sắp xếp danh sách | O(n log n) |
| Lập hóa đơn k dòng | Xử lý một hóa đơn | O(k) |

---

## CHƯƠNG 3. THIẾT KẾ VÀ CÀI ĐẶT CHƯƠNG TRÌNH

### 3.1. Kiến trúc module

Chương trình được chia thành các module:

- `sales_manager/data_structures.py`: cài đặt `DynamicArray`, `LinkedList`, `HashTable`, tìm kiếm và sắp xếp.
- `sales_manager/models.py`: định nghĩa `Product`, `Customer`, `Invoice`, `InvoiceItem`, `InvoiceLineInput`, `ProductSaleStat`.
- `sales_manager/storage.py`: đọc/ghi dữ liệu file text.
- `sales_manager/manager.py`: xử lý nghiệp vụ bán hàng.
- `sales_manager/cli.py`: giao diện menu console.

Luồng xử lý tổng quát:

```text
File text -> Storage -> DynamicArray -> HashTable index -> SalesManager -> CLI -> File text/Báo cáo
```

![Hình 3.1. Sơ đồ kiến trúc module chương trình](report/assets/module_architecture.png)

Chú thích: Các module được tách theo trách nhiệm: lưu trữ, mô hình dữ liệu, cấu trúc dữ liệu, xử lý nghiệp vụ và giao diện menu.

### 3.2. Thiết kế lớp dữ liệu

Mỗi bản ghi trong file text được ánh xạ thành một lớp dữ liệu. Ví dụ:

- Dòng trong `products.txt` được chuyển thành `Product`.
- Dòng trong `customers.txt` được chuyển thành `Customer`.
- Dòng trong `invoices.txt` được chuyển thành `Invoice`.
- Dòng trong `invoice_items.txt` được chuyển thành `InvoiceItem`.

Mỗi lớp có hàm chuyển đổi từ object sang dòng text và từ dòng text sang object. Cách làm này giúp tách riêng phần lưu trữ và phần xử lý nghiệp vụ.

### 3.3. Chức năng lập hóa đơn

Các bước lập hóa đơn:

1. Nhập mã khách hàng.
2. Nhập các dòng sản phẩm gồm mã sản phẩm và số lượng.
3. Tra cứu khách hàng bằng `HashTable`.
4. Tra cứu sản phẩm bằng `HashTable`.
5. Kiểm tra số lượng tồn kho.
6. Tính tạm tính, chiết khấu, VAT và tổng tiền.
7. Sinh mã hóa đơn mới.
8. Ghi đầu hóa đơn và chi tiết hóa đơn.
9. Giảm tồn kho sản phẩm.
10. Lưu lại các file dữ liệu.

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
    create invoice items
    decrease product stock
    save files
```

![Hình 3.2. Luồng xử lý chức năng lập hóa đơn](report/assets/invoice_flow.png)

Chú thích: Luồng lập hóa đơn bắt đầu từ nhập dữ liệu bán hàng, sau đó kiểm tra khách hàng/sản phẩm/tồn kho, tính tiền và lưu đồng thời hai file `invoices.txt`, `invoice_items.txt`.

### 3.4. Chức năng báo cáo

Báo cáo doanh thu theo ngày/tháng được tạo bằng cách gom nhóm hóa đơn theo chuỗi ngày hoặc tháng. Top sản phẩm bán chạy được tạo bằng cách duyệt toàn bộ chi tiết hóa đơn, cộng dồn số lượng theo `sku`, sau đó sắp xếp giảm dần bằng quick sort.

### 3.5. Menu chương trình

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

---

## CHƯƠNG 4. KIỂM THỬ, HƯỚNG DẪN SỬ DỤNG VÀ GITHUB

### 4.1. Kiểm thử

Nhóm sử dụng `unittest` để kiểm thử tự động. Các test tập trung vào cấu trúc dữ liệu và nghiệp vụ chính.

Bảng 4.1. Test case kiểm thử chương trình

| STT | Tình huống | Dữ liệu kiểm thử | Kết quả mong đợi |
| --- | --- | --- | --- |
| 1 | Mảng động thêm, xóa, sắp xếp | 3 sản phẩm giá 300, 100, 200 | Sắp xếp đúng, xóa đúng phần tử |
| 2 | Bảng băm thêm/cập nhật/xóa | Khóa `SP001`, `SP002` | Tra cứu, cập nhật, xóa đúng |
| 3 | Lập hóa đơn hợp lệ | KH001 mua SP001 và SP005 | Sinh hóa đơn, tồn kho giảm |
| 4 | Bán vượt tồn kho | SP004 số lượng 999 | Báo lỗi, không tạo hóa đơn |
| 5 | Tìm kiếm, sắp xếp, xuất báo cáo | Từ khóa Laptop | Kết quả đúng và báo cáo có dữ liệu |

Lệnh kiểm thử:

```powershell
python -m unittest discover -s tests
```

Kết quả hiện tại:

```text
Ran 5 tests
OK
```

### 4.2. Hướng dẫn sử dụng có minh họa

#### Bước 1. Mở menu chương trình

Lệnh:

```powershell
python -m sales_manager.cli menu
```

![Hình 4.1. Mở menu chương trình](report/assets/step_menu.png)

Chú thích: Menu hiển thị các chức năng chính. Người dùng nhập số tương ứng để chọn chức năng, nhập `0` để thoát.

#### Bước 2. Tạo dữ liệu demo

Lệnh:

```powershell
python -m sales_manager.cli --data-dir data/demo demo
```

![Hình 4.2. Tạo dữ liệu demo](report/assets/step_demo.png)

Chú thích: Lệnh này sao chép dữ liệu mẫu, tạo 3 hóa đơn minh họa và xuất báo cáo text.

#### Bước 3. Xem tổng quan dữ liệu

Lệnh:

```powershell
python -m sales_manager.cli --data-dir data/demo summary
```

![Hình 4.3. Xem tổng quan dữ liệu](report/assets/step_summary.png)

Chú thích: Tổng quan cho biết số sản phẩm, số khách hàng, số hóa đơn, số chi tiết hóa đơn và tổng doanh thu.

#### Bước 4. Chạy kiểm thử tự động

Lệnh:

```powershell
python -m unittest discover -s tests
```

![Hình 4.4. Chạy kiểm thử tự động](report/assets/step_tests.png)

Chú thích: Bộ kiểm thử giúp kiểm tra nhanh chương trình sau khi thay đổi mã nguồn.

### 4.3. Đưa mã nguồn lên GitHub

Repository GitHub: https://github.com/nhtameo/quan-ly-ban-hang-dsa.

Nội dung đưa lên GitHub chỉ gồm các nhóm file cần thiết:

- Chương trình: thư mục `sales_manager` và các file chạy `.bat`.
- File dữ liệu: thư mục `data/sample`.
- Báo cáo: thư mục `report`, gồm báo cáo Word/PDF/Markdown và ảnh minh họa.
- File hướng dẫn ngắn: `README.md`.

Không đưa các file tạm như `tmp`, `output`, `release` lên GitHub. Phần mô tả ngắn của repository được đặt là: `Quản lý bán hàng`.

![Hình 4.5. Minh họa repository GitHub](report/assets/github_repo.png)

Chú thích: Repository chỉ cần phần mô tả ngắn gọn và chứa đúng các nhóm file cần nộp: chương trình, dữ liệu mẫu, báo cáo và hướng dẫn chạy.

---

## KẾT LUẬN

Đề tài đã xây dựng được chương trình quản lý bán hàng cơ bản, đáp ứng các yêu cầu chính của chủ đề: quản lý sản phẩm, quản lý khách hàng, lập hóa đơn master-detail, tính chiết khấu/VAT/tổng tiền, cập nhật tồn kho, thống kê doanh thu và sản phẩm bán chạy. Chương trình sử dụng file text để lưu dữ liệu và tự cài đặt các cấu trúc dữ liệu/thuật toán cần thiết.

Qua quá trình thực hiện, nhóm đã củng cố kiến thức về mảng động, danh sách liên kết, bảng băm, tìm kiếm, sắp xếp, xử lý file, kiểm thử và tổ chức chương trình theo module. Hướng phát triển tiếp theo là bổ sung nhập kho, lọc báo cáo theo khoảng thời gian, giao diện đồ họa và xuất hóa đơn riêng ra PDF.

## TÀI LIỆU THAM KHẢO

1. Tài liệu môn học kĩ thuật lập trình, thầy vũ thành nam.
2. Tài liệu yêu cầu project 20252 của học phần Kĩ thuật lập trình.
3. Tài liệu Python chuẩn về xử lý file và kiểm thử `unittest`.
4. Mẫu báo cáo/đồ án tốt nghiệp Đại học Bách khoa Hà Nội.

## PHỤ LỤC

### Phụ lục A. Hàm băm chuỗi

```python
def _hash(self, key: str) -> int:
    value = 0
    for ch in key:
        value = (value * 31 + ord(ch)) % self._capacity
    return value
```

### Phụ lục B. Ý tưởng hàm lập hóa đơn

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
