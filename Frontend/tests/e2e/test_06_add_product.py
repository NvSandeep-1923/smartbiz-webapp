"""
Test Suite 06: Add Product Page
===============================
Tests the product creation form including all input fields,
dropdowns, sections, and form submission behaviour.
"""

import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from helpers import (
    log_event, get_page_text, navigate_to,
    PAGE_LOAD_WAIT, DEFAULT_TIMEOUT,
)


class TestAddProductPage:
    """Add Product form test cases (requires login)."""

    @pytest.fixture(autouse=True)
    def setup(self, logged_in_driver, base_url):
        self.driver = logged_in_driver
        self.base_url = base_url
        navigate_to(self.driver, base_url, "#inventory/add")
        time.sleep(3)
        self.body = get_page_text(self.driver)
        log_event("INFO", "Navigated to Add Product page")

    # ------------------------------------------------------------------
    # TC-ADD-001: Add Product form loads
    # ------------------------------------------------------------------
    def test_add_product_form_loads(self):
        """The add product form should be present."""
        form = self.driver.find_elements(By.ID, "add-product-form")
        assert len(form) > 0, "Add product form not found"
        log_event("INFO", "TC-ADD-001 PASSED: Add product form loaded")

    # ------------------------------------------------------------------
    # TC-ADD-002: Header title shows Add New Item
    # ------------------------------------------------------------------
    def test_header_title(self):
        """Header should display 'Add New Item'."""
        assert "Add New Item" in self.body, "Header title not found"
        log_event("INFO", "TC-ADD-002 PASSED: Header title correct")

    # ------------------------------------------------------------------
    # TC-ADD-003: Item Name field present
    # ------------------------------------------------------------------
    def test_item_name_field(self):
        """Item Name input with id='p-name' should exist."""
        field = self.driver.find_elements(By.ID, "p-name")
        assert len(field) > 0, "Item Name field not found"
        log_event("INFO", "TC-ADD-003 PASSED: Item Name field present")

    # ------------------------------------------------------------------
    # TC-ADD-004: Category dropdown options
    # ------------------------------------------------------------------
    def test_category_dropdown_options(self):
        """Category dropdown should have Grains, Dairy, Beverages options."""
        select_el = self.driver.find_element(By.ID, "p-cat")
        options = [o.text for o in select_el.find_elements(By.TAG_NAME, "option")]
        assert any("Grains" in o for o in options), "Grains option missing"
        assert any("Dairy" in o for o in options), "Dairy option missing"
        assert any("Beverages" in o for o in options), "Beverages option missing"
        log_event("INFO", "TC-ADD-004 PASSED: Category options correct")

    # ------------------------------------------------------------------
    # TC-ADD-005: Unit dropdown options
    # ------------------------------------------------------------------
    def test_unit_dropdown_options(self):
        """Unit dropdown should have kg, pcs, ltr options."""
        select_el = self.driver.find_element(By.ID, "p-unit")
        options = [o.text for o in select_el.find_elements(By.TAG_NAME, "option")]
        assert "kg" in options, "kg option missing"
        assert "pcs" in options, "pcs option missing"
        assert "ltr" in options, "ltr option missing"
        log_event("INFO", "TC-ADD-005 PASSED: Unit options correct")

    # ------------------------------------------------------------------
    # TC-ADD-006: GST Rate dropdown options
    # ------------------------------------------------------------------
    def test_gst_rate_dropdown(self):
        """GST Rate dropdown should have 0%, 5%, 12%, 18% options."""
        select_el = self.driver.find_element(By.ID, "p-gst")
        options = [o.text for o in select_el.find_elements(By.TAG_NAME, "option")]
        assert "0%" in options, "0% GST option missing"
        assert "5%" in options, "5% GST option missing"
        assert "12%" in options, "12% GST option missing"
        assert "18%" in options, "18% GST option missing"
        log_event("INFO", "TC-ADD-006 PASSED: GST rate options correct")

    # ------------------------------------------------------------------
    # TC-ADD-007: HSN Code field present
    # ------------------------------------------------------------------
    def test_hsn_code_field(self):
        """HSN Code input with id='p-hsn' should exist."""
        field = self.driver.find_elements(By.ID, "p-hsn")
        assert len(field) > 0, "HSN Code field not found"
        log_event("INFO", "TC-ADD-007 PASSED: HSN Code field present")

    # ------------------------------------------------------------------
    # TC-ADD-008: Price fields present
    # ------------------------------------------------------------------
    def test_price_fields_present(self):
        """Purchase and Sales Price fields should exist."""
        cost = self.driver.find_elements(By.ID, "p-cost")
        sale = self.driver.find_elements(By.ID, "p-sale")
        assert len(cost) > 0, "Purchase Price field not found"
        assert len(sale) > 0, "Sales Price field not found"
        log_event("INFO", "TC-ADD-008 PASSED: Price fields present")

    # ------------------------------------------------------------------
    # TC-ADD-009: Stock level field present
    # ------------------------------------------------------------------
    def test_stock_level_field(self):
        """Stock level input with id='p-stock' should exist."""
        field = self.driver.find_elements(By.ID, "p-stock")
        assert len(field) > 0, "Stock level field not found"
        log_event("INFO", "TC-ADD-009 PASSED: Stock level field present")

    # ------------------------------------------------------------------
    # TC-ADD-010: Save Product button present
    # ------------------------------------------------------------------
    def test_save_button_present(self):
        """The 'Save Product' button should be present."""
        assert "Save Product" in self.body, "Save Product button not found"
        log_event("INFO", "TC-ADD-010 PASSED: Save button present")

    # ------------------------------------------------------------------
    # TC-ADD-011: Cancel button present
    # ------------------------------------------------------------------
    def test_cancel_button_present(self):
        """The 'Cancel' button should be present."""
        assert "Cancel" in self.body, "Cancel button not found"
        log_event("INFO", "TC-ADD-011 PASSED: Cancel button present")

    # ------------------------------------------------------------------
    # TC-ADD-012: Basic Details section header
    # ------------------------------------------------------------------
    def test_basic_details_section(self):
        """The 'Basic Details' section should be present."""
        assert "Basic Details" in self.body, "Basic Details section not found"
        log_event("INFO", "TC-ADD-012 PASSED: Basic Details section present")

    # ------------------------------------------------------------------
    # TC-ADD-013: Pricing section header
    # ------------------------------------------------------------------
    def test_pricing_section(self):
        """The 'Pricing Information' section should be present."""
        assert "Pricing Information" in self.body, (
            "Pricing Information section not found"
        )
        log_event("INFO", "TC-ADD-013 PASSED: Pricing section present")

    # ------------------------------------------------------------------
    # TC-ADD-014: Stock Inventory section header
    # ------------------------------------------------------------------
    def test_stock_section(self):
        """The 'Stock Inventory' section should be present."""
        assert "Stock Inventory" in self.body, (
            "Stock Inventory section not found"
        )
        log_event("INFO", "TC-ADD-014 PASSED: Stock section present")
