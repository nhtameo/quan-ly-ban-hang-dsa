# Outline slide thuyết trình

## Slide 1 - Tên đề tài

Hệ thống quản lý bán hàng sử dụng cấu trúc dữ liệu tự cài đặt.

Nhóm 15:

- Nguyễn Trịnh Mai Phương - 202418965.
- Trần Minh Quân - 202418973.

## Slide 2 - Phân công nhóm

- Nguyễn Trịnh Mai Phương: thiết kế chương trình, thiết kế dữ liệu, cài đặt luồng đọc/ghi dữ liệu, viết báo cáo.
- Trần Minh Quân: kiểm thử, cài đặt/kịch bản test, chuẩn bị dữ liệu demo, viết báo cáo, hỗ trợ đóng gói và GitHub.

## Slide 3 - Yêu cầu bài toán

- Quản lý khách hàng, sản phẩm.
- Lập hóa đơn bán hàng có chiết khấu và VAT.
- Lưu hóa đơn và chi tiết hóa đơn theo mô hình master-detail.
- Báo cáo doanh thu và top sản phẩm bán chạy.
- Lưu dữ liệu bằng file text.

## Slide 4 - Dữ liệu đầu vào/đầu ra

- Đầu vào: `products.txt`, `customers.txt`, nhập liệu từ menu.
- Đầu ra: `invoices.txt`, `invoice_items.txt`, báo cáo text.
- Định dạng: các trường phân tách bằng dấu `|`.

## Slide 5 - Cấu trúc dữ liệu

- `DynamicArray`: lưu danh sách sản phẩm, khách hàng, hóa đơn.
- `LinkedList`: xử lý va chạm trong bảng băm.
- `HashTable`: tra cứu nhanh sản phẩm theo mã và khách hàng theo mã.

## Slide 6 - Thuật toán

- Tìm kiếm tuyến tính theo mã/tên/loại.
- Quick sort tự cài đặt để sắp xếp sản phẩm và báo cáo.
- Tính toán hóa đơn: tạm tính, chiết khấu, VAT, tổng tiền.
- Thống kê doanh thu theo ngày/tháng và best-sellers.

## Slide 7 - Thiết kế module

- `data_structures.py`: cấu trúc dữ liệu và thuật toán.
- `models.py`: mô hình bản ghi.
- `storage.py`: đọc/ghi file text.
- `manager.py`: nghiệp vụ.
- `cli.py`: giao diện menu.

## Slide 8 - Demo chương trình

- Hiển thị danh sách sản phẩm.
- Tìm kiếm sản phẩm.
- Lập hóa đơn.
- Xem doanh thu và top sản phẩm bán chạy.

## Slide 9 - Kiểm thử

- Lập hóa đơn làm giảm tồn kho và lưu được dữ liệu.
- Không cho bán vượt tồn kho.
- Tìm kiếm/sắp xếp đúng.
- Xuất báo cáo có nội dung doanh thu và sản phẩm bán.

## Slide 10 - Phân tích độ phức tạp

- Tra cứu bảng băm: trung bình O(1), xấu nhất O(n).
- Tìm kiếm tuyến tính: O(n).
- Quick sort: trung bình O(n log n), xấu nhất O(n^2).
- Lập hóa đơn k mặt hàng: O(k) sau khi tra cứu bằng bảng băm.

## Slide 11 - Kết luận

Chương trình đáp ứng yêu cầu quản lý bán hàng cơ bản, vận dụng cấu trúc dữ liệu tự cài đặt, lưu file text, có test và báo cáo bàn giao.
