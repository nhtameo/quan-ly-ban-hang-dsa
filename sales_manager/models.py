from __future__ import annotations


def _clean(value: object) -> str:
    return str(value).replace("|", "/").replace("\n", " ").strip()


class Product:
    def __init__(
        self,
        sku: str,
        name: str,
        unit: str,
        category: str,
        price: int,
        stock: int,
        min_stock: int,
    ) -> None:
        self.sku = _clean(sku).upper()
        self.name = _clean(name)
        self.unit = _clean(unit)
        self.category = _clean(category)
        self.price = int(price)
        self.stock = int(stock)
        self.min_stock = int(min_stock)

    def to_record(self) -> str:
        return "|".join(
            [
                self.sku,
                _clean(self.name),
                _clean(self.unit),
                _clean(self.category),
                str(self.price),
                str(self.stock),
                str(self.min_stock),
            ]
        )

    @staticmethod
    def from_record(record: str) -> "Product":
        parts = record.rstrip("\n").split("|")
        if len(parts) != 7:
            raise ValueError(f"Dong san pham khong hop le: {record!r}")
        return Product(parts[0], parts[1], parts[2], parts[3], int(parts[4]), int(parts[5]), int(parts[6]))


class Customer:
    def __init__(self, customer_id: str, name: str, phone: str, address: str) -> None:
        self.customer_id = _clean(customer_id).upper()
        self.name = _clean(name)
        self.phone = _clean(phone)
        self.address = _clean(address)

    def to_record(self) -> str:
        return "|".join([self.customer_id, _clean(self.name), _clean(self.phone), _clean(self.address)])

    @staticmethod
    def from_record(record: str) -> "Customer":
        parts = record.rstrip("\n").split("|")
        if len(parts) != 4:
            raise ValueError(f"Dong khach hang khong hop le: {record!r}")
        return Customer(parts[0], parts[1], parts[2], parts[3])


class Invoice:
    def __init__(
        self,
        invoice_id: str,
        customer_id: str,
        customer_name: str,
        created_at: str,
        discount_percent: float,
        vat_percent: float,
        subtotal: int,
        vat_amount: int,
        total: int,
    ) -> None:
        self.invoice_id = _clean(invoice_id).upper()
        self.customer_id = _clean(customer_id).upper()
        self.customer_name = _clean(customer_name)
        self.created_at = _clean(created_at)
        self.discount_percent = float(discount_percent)
        self.vat_percent = float(vat_percent)
        self.subtotal = int(subtotal)
        self.vat_amount = int(vat_amount)
        self.total = int(total)

    def to_record(self) -> str:
        return "|".join(
            [
                self.invoice_id,
                self.customer_id,
                _clean(self.customer_name),
                self.created_at,
                f"{self.discount_percent:.2f}",
                f"{self.vat_percent:.2f}",
                str(self.subtotal),
                str(self.vat_amount),
                str(self.total),
            ]
        )

    @staticmethod
    def from_record(record: str) -> "Invoice":
        parts = record.rstrip("\n").split("|")
        if len(parts) != 9:
            raise ValueError(f"Dong hoa don khong hop le: {record!r}")
        return Invoice(
            parts[0],
            parts[1],
            parts[2],
            parts[3],
            float(parts[4]),
            float(parts[5]),
            int(parts[6]),
            int(parts[7]),
            int(parts[8]),
        )


class InvoiceItem:
    def __init__(
        self,
        invoice_id: str,
        sku: str,
        product_name: str,
        quantity: int,
        unit_price: int,
        line_total: int,
    ) -> None:
        self.invoice_id = _clean(invoice_id).upper()
        self.sku = _clean(sku).upper()
        self.product_name = _clean(product_name)
        self.quantity = int(quantity)
        self.unit_price = int(unit_price)
        self.line_total = int(line_total)

    def to_record(self) -> str:
        return "|".join(
            [
                self.invoice_id,
                self.sku,
                _clean(self.product_name),
                str(self.quantity),
                str(self.unit_price),
                str(self.line_total),
            ]
        )

    @staticmethod
    def from_record(record: str) -> "InvoiceItem":
        parts = record.rstrip("\n").split("|")
        if len(parts) != 6:
            raise ValueError(f"Dong chi tiet hoa don khong hop le: {record!r}")
        return InvoiceItem(parts[0], parts[1], parts[2], int(parts[3]), int(parts[4]), int(parts[5]))


class InvoiceLineInput:
    def __init__(self, sku: str, quantity: int) -> None:
        self.sku = _clean(sku).upper()
        self.quantity = int(quantity)


class ProductSaleStat:
    def __init__(self, sku: str, name: str) -> None:
        self.sku = sku
        self.name = name
        self.quantity = 0
        self.revenue = 0

    def add(self, quantity: int, revenue: int) -> None:
        self.quantity += int(quantity)
        self.revenue += int(revenue)

