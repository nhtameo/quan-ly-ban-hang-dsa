from __future__ import annotations

from pathlib import Path
from typing import Callable

from sales_manager.data_structures import DynamicArray
from sales_manager.models import Customer, Invoice, InvoiceItem, Product

ROOT_DIR = Path(__file__).resolve().parents[1]
DEFAULT_DATA_DIR = ROOT_DIR / "data" / "sample"

PRODUCT_HEADER = "sku|name|unit|category|price|stock|min_stock"
CUSTOMER_HEADER = "customer_id|name|phone|address"
INVOICE_HEADER = "invoice_id|customer_id|customer_name|created_at|discount_percent|vat_percent|subtotal|vat_amount|total"
INVOICE_ITEM_HEADER = "invoice_id|sku|product_name|quantity|unit_price|line_total"


class Storage:
    def __init__(self, data_dir: str | Path = DEFAULT_DATA_DIR) -> None:
        self.data_dir = Path(data_dir)
        self.products_file = self.data_dir / "products.txt"
        self.customers_file = self.data_dir / "customers.txt"
        self.invoices_file = self.data_dir / "invoices.txt"
        self.invoice_items_file = self.data_dir / "invoice_items.txt"

    def ensure_files(self) -> None:
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self._ensure_file(self.products_file, PRODUCT_HEADER)
        self._ensure_file(self.customers_file, CUSTOMER_HEADER)
        self._ensure_file(self.invoices_file, INVOICE_HEADER)
        self._ensure_file(self.invoice_items_file, INVOICE_ITEM_HEADER)

    def load_products(self) -> DynamicArray:
        return self._load_records(self.products_file, Product.from_record)

    def save_products(self, products: DynamicArray) -> None:
        self._save_records(self.products_file, PRODUCT_HEADER, products)

    def load_customers(self) -> DynamicArray:
        return self._load_records(self.customers_file, Customer.from_record)

    def save_customers(self, customers: DynamicArray) -> None:
        self._save_records(self.customers_file, CUSTOMER_HEADER, customers)

    def load_invoices(self) -> DynamicArray:
        return self._load_records(self.invoices_file, Invoice.from_record)

    def save_invoices(self, invoices: DynamicArray) -> None:
        self._save_records(self.invoices_file, INVOICE_HEADER, invoices)

    def load_invoice_items(self) -> DynamicArray:
        return self._load_records(self.invoice_items_file, InvoiceItem.from_record)

    def save_invoice_items(self, items: DynamicArray) -> None:
        self._save_records(self.invoice_items_file, INVOICE_ITEM_HEADER, items)

    def _ensure_file(self, path: Path, header: str) -> None:
        if not path.exists():
            path.write_text(header + "\n", encoding="utf-8")

    def _load_records(self, path: Path, factory: Callable[[str], object]) -> DynamicArray:
        self.ensure_files()
        records = DynamicArray()
        with path.open("r", encoding="utf-8") as f:
            line_number = 0
            for line in f:
                line_number += 1
                if line_number == 1 or not line.strip():
                    continue
                records.append(factory(line))
        return records

    def _save_records(self, path: Path, header: str, records: DynamicArray) -> None:
        self.data_dir.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8", newline="\n") as f:
            f.write(header + "\n")
            for record in records:
                f.write(record.to_record() + "\n")

