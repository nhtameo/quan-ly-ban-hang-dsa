import shutil
import tempfile
import unittest
from pathlib import Path

from sales_manager.data_structures import DynamicArray, HashTable, quick_sort
from sales_manager.manager import SalesError, SalesManager
from sales_manager.models import InvoiceLineInput, Product
from sales_manager.storage import ROOT_DIR


class DataStructureTest(unittest.TestCase):
    def test_dynamic_array_append_remove_and_sort(self):
        array = DynamicArray()
        array.append(Product("SP3", "C", "chiec", "Loai", 300, 1, 0))
        array.append(Product("SP1", "A", "chiec", "Loai", 100, 1, 0))
        array.append(Product("SP2", "B", "chiec", "Loai", 200, 1, 0))

        quick_sort(array, lambda item: item.price)

        self.assertEqual(array.get(0).sku, "SP1")
        self.assertEqual(array.get(2).sku, "SP3")
        removed = array.remove_at(1)
        self.assertEqual(removed.sku, "SP2")
        self.assertEqual(len(array), 2)

    def test_hash_table_put_get_update_remove(self):
        table = HashTable(capacity=11)
        table.put("SP001", "Alpha")
        table.put("sp001", "Alpha updated")
        table.put("SP002", "Beta")

        self.assertEqual(len(table), 2)
        self.assertEqual(table.get("SP001"), "Alpha updated")
        self.assertTrue(table.remove("SP002"))
        self.assertFalse(table.contains("SP002"))


class SalesManagerTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.data_dir = Path(self.tmp.name) / "data"
        shutil.copytree(ROOT_DIR / "data" / "sample", self.data_dir)

    def tearDown(self):
        self.tmp.cleanup()

    def test_create_invoice_updates_stock_and_persists(self):
        manager = SalesManager(self.data_dir)
        before = manager.product_index.get("SP001").stock
        lines = DynamicArray()
        lines.append(InvoiceLineInput("SP001", 2))
        lines.append(InvoiceLineInput("SP005", 1))

        invoice = manager.create_invoice("KH001", lines, discount_percent=10, vat_percent=8)

        self.assertEqual(invoice.invoice_id, "HD0001")
        self.assertGreater(invoice.total, 0)
        self.assertEqual(manager.product_index.get("SP001").stock, before - 2)

        reloaded = SalesManager(self.data_dir)
        self.assertEqual(len(reloaded.invoices), 1)
        self.assertEqual(reloaded.product_index.get("SP001").stock, before - 2)

    def test_create_invoice_blocks_insufficient_stock(self):
        manager = SalesManager(self.data_dir)
        lines = DynamicArray()
        lines.append(InvoiceLineInput("SP004", 999))

        with self.assertRaises(SalesError):
            manager.create_invoice("KH001", lines)

        self.assertEqual(len(manager.invoices), 0)

    def test_search_sort_and_report(self):
        manager = SalesManager(self.data_dir)
        results = manager.find_products("Laptop")
        self.assertEqual(len(results), 2)

        sorted_products = manager.sorted_products("price", reverse=True)
        self.assertEqual(sorted_products.get(0).sku, "SP004")

        lines = DynamicArray()
        lines.append(InvoiceLineInput("SP003", 1))
        manager.create_invoice("KH002", lines)

        report_path = manager.export_report(Path(self.tmp.name) / "sales_report.txt")
        report_text = report_path.read_text(encoding="utf-8")
        self.assertIn("BAO CAO BAN HANG", report_text)
        self.assertIn("SP003", report_text)


if __name__ == "__main__":
    unittest.main()

