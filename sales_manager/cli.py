from __future__ import annotations

import argparse
import shutil
from pathlib import Path

from sales_manager.data_structures import DynamicArray
from sales_manager.manager import SalesError, SalesManager, format_money
from sales_manager.models import Customer, InvoiceLineInput, Product
from sales_manager.storage import DEFAULT_DATA_DIR, ROOT_DIR


def main() -> None:
    parser = argparse.ArgumentParser(description="He thong quan ly ban hang DSA")
    parser.add_argument("--data-dir", default=str(DEFAULT_DATA_DIR), help="Thu muc chua file du lieu text")
    subparsers = parser.add_subparsers(dest="command")
    subparsers.add_parser("menu", help="Mo menu console")
    subparsers.add_parser("summary", help="In tong quan du lieu")
    subparsers.add_parser("report", help="Xuat bao cao text")
    subparsers.add_parser("demo", help="Tao du lieu demo va 3 hoa don mau")
    args = parser.parse_args()

    if args.command == "demo":
        run_demo(Path(args.data_dir))
        return

    manager = SalesManager(args.data_dir)
    if args.command == "summary":
        print_summary(manager)
    elif args.command == "report":
        out = manager.export_report(ROOT_DIR / "output" / "sales_report.txt")
        print(f"Da xuat bao cao: {out}")
    else:
        menu_loop(manager)


def menu_loop(manager: SalesManager) -> None:
    while True:
        print("\n===== HE THONG QUAN LY BAN HANG =====")
        print("1. Xem danh sach san pham")
        print("2. Them san pham")
        print("3. Tim kiem san pham")
        print("4. Sap xep san pham")
        print("5. Xem danh sach khach hang")
        print("6. Them khach hang")
        print("7. Lap hoa don ban hang")
        print("8. Bao cao doanh thu")
        print("9. Top san pham ban chay")
        print("10. San pham sap het hang")
        print("11. Luu va tai lai du lieu")
        print("0. Thoat")
        choice = input("Chon chuc nang: ").strip()
        try:
            if choice == "1":
                print_products(manager.products)
            elif choice == "2":
                add_product_flow(manager)
            elif choice == "3":
                keyword = input("Nhap tu khoa: ")
                print_products(manager.find_products(keyword))
            elif choice == "4":
                sort_products_flow(manager)
            elif choice == "5":
                print_customers(manager.customers)
            elif choice == "6":
                add_customer_flow(manager)
            elif choice == "7":
                create_invoice_flow(manager)
            elif choice == "8":
                print_revenue(manager)
            elif choice == "9":
                print_best_sellers(manager)
            elif choice == "10":
                print_products(manager.low_stock_products())
            elif choice == "11":
                manager.save()
                manager.load()
                print("Da luu va tai lai du lieu.")
            elif choice == "0":
                manager.save()
                print("Tam biet.")
                break
            else:
                print("Lua chon khong hop le.")
        except (SalesError, ValueError) as exc:
            print(f"Loi: {exc}")


def add_product_flow(manager: SalesManager) -> None:
    sku = input("Ma SP: ")
    name = input("Ten SP: ")
    unit = input("Don vi tinh: ") or "chiec"
    category = input("Loai SP: ")
    price = int(input("Don gia ban: "))
    stock = int(input("So luong ton: "))
    min_stock = int(input("Nguong ton toi thieu: "))
    manager.add_product(Product(sku, name, unit, category, price, stock, min_stock))
    print("Da them san pham.")


def add_customer_flow(manager: SalesManager) -> None:
    customer_id = input("Ma KH: ")
    name = input("Ten KH: ")
    phone = input("So dien thoai: ")
    address = input("Dia chi: ")
    manager.add_customer(Customer(customer_id, name, phone, address))
    print("Da them khach hang.")


def create_invoice_flow(manager: SalesManager) -> None:
    customer_id = input("Ma khach hang: ").strip().upper()
    lines = DynamicArray()
    print("Nhap tung dong san pham. De trong ma SP de ket thuc.")
    while True:
        sku = input("Ma SP: ").strip().upper()
        if not sku:
            break
        quantity = int(input("So luong: "))
        lines.append(InvoiceLineInput(sku, quantity))
    discount = float(input("Chiet khau (%): ") or "0")
    vat = float(input("VAT (%): ") or "8")
    invoice = manager.create_invoice(customer_id, lines, discount, vat)
    print(f"Da lap hoa don {invoice.invoice_id}, tong tien: {format_money(invoice.total)}")


def sort_products_flow(manager: SalesManager) -> None:
    field = input("Sap xep theo sku/name/price/stock: ").strip().lower() or "sku"
    direction = input("Giam dan? (y/N): ").strip().lower()
    print_products(manager.sorted_products(field, reverse=direction == "y"))


def print_products(products: DynamicArray) -> None:
    print("\n{:<8} {:<28} {:<10} {:<20} {:>14} {:>8} {:>8}".format(
        "Ma", "Ten san pham", "DVT", "Loai", "Don gia", "Ton", "Min"
    ))
    print("-" * 104)
    for p in products:
        print(
            "{:<8} {:<28} {:<10} {:<20} {:>14} {:>8} {:>8}".format(
                p.sku,
                p.name[:28],
                p.unit,
                p.category[:20],
                format_money(p.price),
                p.stock,
                p.min_stock,
            )
        )
    print(f"Tong: {len(products)} san pham")


def print_customers(customers: DynamicArray) -> None:
    print("\n{:<8} {:<24} {:<14} {:<32}".format("Ma KH", "Ten khach hang", "SDT", "Dia chi"))
    print("-" * 82)
    for c in customers:
        print("{:<8} {:<24} {:<14} {:<32}".format(c.customer_id, c.name[:24], c.phone, c.address[:32]))
    print(f"Tong: {len(customers)} khach hang")


def print_summary(manager: SalesManager) -> None:
    summary = manager.summary()
    print("Tong quan du lieu")
    print(f"- San pham: {summary.product_count}")
    print(f"- Khach hang: {summary.customer_count}")
    print(f"- Hoa don: {summary.invoice_count}")
    print(f"- Chi tiet hoa don: {summary.invoice_item_count}")
    print(f"- Doanh thu: {format_money(summary.revenue)}")


def print_revenue(manager: SalesManager) -> None:
    print("\nDoanh thu theo ngay")
    print("{:<14} {:>10} {:>18}".format("Ngay", "So HD", "Doanh thu"))
    print("-" * 44)
    for row in manager.revenue_by_day():
        print("{:<14} {:>10} {:>18}".format(row.key, row.count, format_money(row.revenue)))
    print("\nDoanh thu theo thang")
    print("{:<14} {:>10} {:>18}".format("Thang", "So HD", "Doanh thu"))
    print("-" * 44)
    for row in manager.revenue_by_month():
        print("{:<14} {:>10} {:>18}".format(row.key, row.count, format_money(row.revenue)))


def print_best_sellers(manager: SalesManager) -> None:
    print("\nTop san pham ban chay")
    print("{:<8} {:<28} {:>10} {:>18}".format("Ma", "Ten san pham", "SL ban", "Doanh thu"))
    print("-" * 70)
    for stat in manager.best_sellers(10):
        print("{:<8} {:<28} {:>10} {:>18}".format(stat.sku, stat.name[:28], stat.quantity, format_money(stat.revenue)))


def run_demo(data_dir: Path) -> None:
    sample_dir = ROOT_DIR / "data" / "sample"
    if data_dir.resolve() == sample_dir.resolve():
        data_dir = ROOT_DIR / "data" / "demo"
    if data_dir.exists():
        shutil.rmtree(data_dir)
    shutil.copytree(sample_dir, data_dir)
    manager = SalesManager(data_dir)

    lines = DynamicArray()
    lines.append(InvoiceLineInput("SP001", 1))
    lines.append(InvoiceLineInput("SP005", 2))
    manager.create_invoice("KH001", lines, discount_percent=2, vat_percent=8)

    lines = DynamicArray()
    lines.append(InvoiceLineInput("SP003", 1))
    lines.append(InvoiceLineInput("SP007", 1))
    manager.create_invoice("KH002", lines, discount_percent=5, vat_percent=8)

    lines = DynamicArray()
    lines.append(InvoiceLineInput("SP006", 3))
    lines.append(InvoiceLineInput("SP008", 1))
    manager.create_invoice("KH003", lines, discount_percent=0, vat_percent=8)

    report_path = manager.export_report(ROOT_DIR / "output" / "sales_report.txt")
    print_summary(manager)
    print(f"Da tao du lieu demo tai: {data_dir}")
    print(f"Bao cao text: {report_path}")


if __name__ == "__main__":
    main()
