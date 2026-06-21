from __future__ import annotations

from datetime import datetime
from pathlib import Path

from sales_manager.data_structures import DynamicArray, HashTable, linear_search, quick_sort
from sales_manager.models import Customer, Invoice, InvoiceItem, InvoiceLineInput, Product, ProductSaleStat
from sales_manager.storage import DEFAULT_DATA_DIR, Storage


class SalesError(Exception):
    pass


class SalesManager:
    def __init__(self, data_dir: str | Path = DEFAULT_DATA_DIR) -> None:
        self.storage = Storage(data_dir)
        self.products = DynamicArray()
        self.customers = DynamicArray()
        self.invoices = DynamicArray()
        self.invoice_items = DynamicArray()
        self.product_index = HashTable()
        self.customer_index = HashTable()
        self.load()

    def load(self) -> None:
        self.storage.ensure_files()
        self.products = self.storage.load_products()
        self.customers = self.storage.load_customers()
        self.invoices = self.storage.load_invoices()
        self.invoice_items = self.storage.load_invoice_items()
        self._rebuild_indexes()

    def save(self) -> None:
        self.storage.save_products(self.products)
        self.storage.save_customers(self.customers)
        self.storage.save_invoices(self.invoices)
        self.storage.save_invoice_items(self.invoice_items)

    def add_product(self, product: Product) -> None:
        self._validate_product(product)
        if self.product_index.contains(product.sku):
            raise SalesError(f"Ma san pham {product.sku} da ton tai.")
        self.products.append(product)
        self.product_index.put(product.sku, product)
        self.save()

    def update_product(self, product: Product) -> None:
        self._validate_product(product)
        index = self.products.find_index(lambda item: item.sku == product.sku)
        if index < 0:
            raise SalesError(f"Khong tim thay san pham {product.sku}.")
        self.products.set(index, product)
        self.product_index.put(product.sku, product)
        self.save()

    def delete_product(self, sku: str) -> None:
        code = sku.strip().upper()
        index = self.products.find_index(lambda item: item.sku == code)
        if index < 0:
            raise SalesError(f"Khong tim thay san pham {code}.")
        self.products.remove_at(index)
        self.product_index.remove(code)
        self.save()

    def add_customer(self, customer: Customer) -> None:
        self._validate_customer(customer)
        if self.customer_index.contains(customer.customer_id):
            raise SalesError(f"Ma khach hang {customer.customer_id} da ton tai.")
        self.customers.append(customer)
        self.customer_index.put(customer.customer_id, customer)
        self.save()

    def update_customer(self, customer: Customer) -> None:
        self._validate_customer(customer)
        index = self.customers.find_index(lambda item: item.customer_id == customer.customer_id)
        if index < 0:
            raise SalesError(f"Khong tim thay khach hang {customer.customer_id}.")
        self.customers.set(index, customer)
        self.customer_index.put(customer.customer_id, customer)
        self.save()

    def delete_customer(self, customer_id: str) -> None:
        code = customer_id.strip().upper()
        if self.invoices.find_index(lambda inv: inv.customer_id == code) >= 0:
            raise SalesError("Khong the xoa khach hang da co hoa don.")
        index = self.customers.find_index(lambda item: item.customer_id == code)
        if index < 0:
            raise SalesError(f"Khong tim thay khach hang {code}.")
        self.customers.remove_at(index)
        self.customer_index.remove(code)
        self.save()

    def find_products(self, keyword: str) -> DynamicArray:
        key = keyword.strip().lower()
        return linear_search(
            self.products,
            lambda item: key in item.sku.lower()
            or key in item.name.lower()
            or key in item.category.lower(),
        )

    def find_customers(self, keyword: str) -> DynamicArray:
        key = keyword.strip().lower()
        return linear_search(
            self.customers,
            lambda item: key in item.customer_id.lower()
            or key in item.name.lower()
            or key in item.phone.lower(),
        )

    def sorted_products(self, field: str = "sku", reverse: bool = False) -> DynamicArray:
        result = self.products.copy()
        if field == "name":
            quick_sort(result, lambda item: item.name.lower(), reverse)
        elif field == "price":
            quick_sort(result, lambda item: item.price, reverse)
        elif field == "stock":
            quick_sort(result, lambda item: item.stock, reverse)
        else:
            quick_sort(result, lambda item: item.sku, reverse)
        return result

    def create_invoice(
        self,
        customer_id: str,
        lines: DynamicArray,
        discount_percent: float = 0.0,
        vat_percent: float = 8.0,
    ) -> Invoice:
        if lines.is_empty():
            raise SalesError("Hoa don phai co it nhat mot mat hang.")
        customer = self.customer_index.get(customer_id)
        if customer is None:
            raise SalesError(f"Khong tim thay khach hang {customer_id}.")
        if discount_percent < 0 or discount_percent > 100:
            raise SalesError("Chiet khau phai nam trong khoang 0-100.")
        if vat_percent < 0 or vat_percent > 100:
            raise SalesError("VAT phai nam trong khoang 0-100.")

        subtotal = 0
        validated_products = DynamicArray()
        for line in lines:
            if line.quantity <= 0:
                raise SalesError("So luong ban phai lon hon 0.")
            product = self.product_index.get(line.sku)
            if product is None:
                raise SalesError(f"Khong tim thay san pham {line.sku}.")
            if product.stock < line.quantity:
                raise SalesError(f"San pham {line.sku} chi con {product.stock} {product.unit}.")
            validated_products.append(product)
            subtotal += product.price * line.quantity

        invoice_id = self._next_invoice_id()
        discount_amount = round(subtotal * discount_percent / 100)
        vat_amount = round((subtotal - discount_amount) * vat_percent / 100)
        total = subtotal - discount_amount + vat_amount
        invoice = Invoice(
            invoice_id=invoice_id,
            customer_id=customer.customer_id,
            customer_name=customer.name,
            created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            discount_percent=discount_percent,
            vat_percent=vat_percent,
            subtotal=subtotal,
            vat_amount=vat_amount,
            total=total,
        )

        index = 0
        while index < len(lines):
            line = lines.get(index)
            product = validated_products.get(index)
            line_total = product.price * line.quantity
            self.invoice_items.append(
                InvoiceItem(invoice_id, product.sku, product.name, line.quantity, product.price, line_total)
            )
            product.stock -= line.quantity
            index += 1
        self.invoices.append(invoice)
        self.save()
        return invoice

    def revenue_by_day(self) -> DynamicArray:
        return self._revenue_grouped(slice_start=0, slice_end=10)

    def revenue_by_month(self) -> DynamicArray:
        return self._revenue_grouped(slice_start=0, slice_end=7)

    def best_sellers(self, top_n: int = 10) -> DynamicArray:
        stats = HashTable()
        for item in self.invoice_items:
            stat = stats.get(item.sku)
            if stat is None:
                stat = ProductSaleStat(item.sku, item.product_name)
                stats.put(item.sku, stat)
            stat.add(item.quantity, item.line_total)
        result = stats.values()
        quick_sort(result, lambda item: item.quantity, reverse=True)
        limited = DynamicArray()
        index = 0
        while index < len(result) and index < top_n:
            limited.append(result.get(index))
            index += 1
        return limited

    def low_stock_products(self) -> DynamicArray:
        return linear_search(self.products, lambda item: item.stock <= item.min_stock)

    def export_report(self, output_file: str | Path) -> Path:
        path = Path(output_file)
        path.parent.mkdir(parents=True, exist_ok=True)
        summary = self.summary()
        with path.open("w", encoding="utf-8", newline="\n") as f:
            f.write("BAO CAO BAN HANG\n")
            f.write("================\n")
            f.write(f"So san pham: {summary.product_count}\n")
            f.write(f"So khach hang: {summary.customer_count}\n")
            f.write(f"So hoa don: {summary.invoice_count}\n")
            f.write(f"Tong doanh thu: {format_money(summary.revenue)}\n\n")
            f.write("Doanh thu theo ngay\n")
            for row in self.revenue_by_day():
                f.write(f"- {row.key}: {format_money(row.revenue)} ({row.count} hoa don)\n")
            f.write("\nTop san pham ban chay\n")
            for stat in self.best_sellers(10):
                f.write(f"- {stat.sku} | {stat.name} | SL: {stat.quantity} | DT: {format_money(stat.revenue)}\n")
        return path

    def summary(self) -> "Summary":
        revenue = 0
        for invoice in self.invoices:
            revenue += invoice.total
        return Summary(
            product_count=len(self.products),
            customer_count=len(self.customers),
            invoice_count=len(self.invoices),
            invoice_item_count=len(self.invoice_items),
            revenue=revenue,
        )

    def _revenue_grouped(self, slice_start: int, slice_end: int) -> DynamicArray:
        table = HashTable()
        for invoice in self.invoices:
            key = invoice.created_at[slice_start:slice_end]
            row = table.get(key)
            if row is None:
                row = RevenueRow(key)
                table.put(key, row)
            row.add(invoice.total)
        result = table.values()
        quick_sort(result, lambda item: item.key, reverse=True)
        return result

    def _next_invoice_id(self) -> str:
        max_number = 0
        for invoice in self.invoices:
            if invoice.invoice_id.startswith("HD"):
                try:
                    number = int(invoice.invoice_id[2:])
                    if number > max_number:
                        max_number = number
                except ValueError:
                    continue
        return f"HD{max_number + 1:04d}"

    def _rebuild_indexes(self) -> None:
        self.product_index = HashTable()
        for product in self.products:
            self.product_index.put(product.sku, product)
        self.customer_index = HashTable()
        for customer in self.customers:
            self.customer_index.put(customer.customer_id, customer)

    def _validate_product(self, product: Product) -> None:
        if not product.sku or not product.name:
            raise SalesError("Ma va ten san pham khong duoc de trong.")
        if product.price < 0 or product.stock < 0 or product.min_stock < 0:
            raise SalesError("Gia, ton kho va nguong ton toi thieu khong duoc am.")

    def _validate_customer(self, customer: Customer) -> None:
        if not customer.customer_id or not customer.name:
            raise SalesError("Ma va ten khach hang khong duoc de trong.")


class RevenueRow:
    def __init__(self, key: str) -> None:
        self.key = key
        self.count = 0
        self.revenue = 0

    def add(self, total: int) -> None:
        self.count += 1
        self.revenue += int(total)


class Summary:
    def __init__(
        self,
        product_count: int,
        customer_count: int,
        invoice_count: int,
        invoice_item_count: int,
        revenue: int,
    ) -> None:
        self.product_count = product_count
        self.customer_count = customer_count
        self.invoice_count = invoice_count
        self.invoice_item_count = invoice_item_count
        self.revenue = revenue


def format_money(value: int | float) -> str:
    return f"{int(value):,} VND".replace(",", ".")
