"""
Test Suite 07: Billing / Create Invoice Page
=============================================
Tests the invoice creation flow including customer selection,
item addition, quantity controls, summary, and checkout.
"""

import time
import pytest
from selenium.webdriver.common.by import By
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from helpers import (
    log_event, get_page_text, navigate_to,
    PAGE_LOAD_WAIT, DEFAULT_TIMEOUT,
)


class TestBillingPage:
    """Billing / Invoice creation test cases (requires login)."""

    @pytest.fixture(autouse=True)
    def setup(self, logged_in_driver, base_url):
        self.driver = logged_in_driver
        self.base_url = base_url
        navigate_to(self.driver, base_url, "#billing")
        time.sleep(3)
        self.body = get_page_text(self.driver)
        log_event("INFO", "Navigated to Billing page")

    # ------------------------------------------------------------------
    # TC-BIL-001: Billing page loads
    # ------------------------------------------------------------------
    def test_billing_page_loads(self):
        """The billing page should load with #billing in URL."""
        assert "#billing" in self.driver.current_url, (
            f"Billing URL not found: {self.driver.current_url}"
        )
        log_event("INFO", "TC-BIL-001 PASSED: Billing page loaded")

    # ------------------------------------------------------------------
    # TC-BIL-002: Header shows Create Invoice
    # ------------------------------------------------------------------
    def test_header_title(self):
        """Header should display 'Create Invoice'."""
        assert "Create Invoice" in self.body, "Create Invoice header not found"
        log_event("INFO", "TC-BIL-002 PASSED: Header title correct")

    # ------------------------------------------------------------------
    # TC-BIL-003: Step indicator present
    # ------------------------------------------------------------------
    def test_step_indicator(self):
        """Step indicator 'Step 2 of 3' should be visible."""
        assert "Step 2 of 3" in self.body, "Step indicator not found"
        log_event("INFO", "TC-BIL-003 PASSED: Step indicator present")

    # ------------------------------------------------------------------
    # TC-BIL-004: Customer dropdown present
    # ------------------------------------------------------------------
    def test_customer_dropdown_present(self):
        """Customer selection dropdown should exist."""
        select = self.driver.find_elements(By.ID, "billing-customer")
        assert len(select) > 0, "Customer dropdown not found"
        log_event("INFO", "TC-BIL-004 PASSED: Customer dropdown present")

    # ------------------------------------------------------------------
    # TC-BIL-005: Inventory dropdown present
    # ------------------------------------------------------------------
    def test_inventory_dropdown_present(self):
        """Inventory item selection dropdown should exist."""
        select = self.driver.find_elements(By.ID, "billing-inventory")
        assert len(select) > 0, "Inventory dropdown not found"
        log_event("INFO", "TC-BIL-005 PASSED: Inventory dropdown present")

    # ------------------------------------------------------------------
    # TC-BIL-006: Add item button present
    # ------------------------------------------------------------------
    def test_add_item_button(self):
        """The 'Add' item button should be present."""
        btn = self.driver.find_elements(By.ID, "btn-add-item")
        assert len(btn) > 0, "Add item button not found"
        log_event("INFO", "TC-BIL-006 PASSED: Add item button present")

    # ------------------------------------------------------------------
    # TC-BIL-007: Invoice summary shows Subtotal
    # ------------------------------------------------------------------
    def test_subtotal_displayed(self):
        """The Subtotal field should be visible."""
        assert "Subtotal" in self.body, "Subtotal not found in summary"
        log_event("INFO", "TC-BIL-007 PASSED: Subtotal displayed")

    # ------------------------------------------------------------------
    # TC-BIL-008: Invoice summary shows Total GST
    # ------------------------------------------------------------------
    def test_total_gst_displayed(self):
        """The Total GST field should be visible."""
        assert "Total GST" in self.body, "Total GST not found in summary"
        log_event("INFO", "TC-BIL-008 PASSED: Total GST displayed")

    # ------------------------------------------------------------------
    # TC-BIL-009: Invoice summary shows Grand Total
    # ------------------------------------------------------------------
    def test_grand_total_displayed(self):
        """The Grand Total field should be visible."""
        assert "Grand Total" in self.body, "Grand Total not found in summary"
        log_event("INFO", "TC-BIL-009 PASSED: Grand Total displayed")

    # ------------------------------------------------------------------
    # TC-BIL-010: Save & Preview button present
    # ------------------------------------------------------------------
    def test_save_preview_button(self):
        """The 'Save & Preview' button should be present."""
        btn = self.driver.find_elements(By.ID, "btn-checkout")
        assert len(btn) > 0, "Save & Preview button not found"
        log_event("INFO", "TC-BIL-010 PASSED: Save & Preview button present")

    # ------------------------------------------------------------------
    # TC-BIL-011: Save Draft button present
    # ------------------------------------------------------------------
    def test_save_draft_button(self):
        """The 'Save Draft' button should be present."""
        assert "Save Draft" in self.body, "Save Draft button not found"
        log_event("INFO", "TC-BIL-011 PASSED: Save Draft button present")

    # ------------------------------------------------------------------
    # TC-BIL-012: Invoice items list container exists
    # ------------------------------------------------------------------
    def test_items_list_container(self):
        """Invoice items list container should exist."""
        container = self.driver.find_elements(By.ID, "invoice-items-list")
        assert len(container) > 0, "Invoice items list not found"
        log_event("INFO", "TC-BIL-012 PASSED: Items list container exists")

    # ------------------------------------------------------------------
    # TC-BIL-013: Select Customer label present
    # ------------------------------------------------------------------
    def test_select_customer_label(self):
        """'Select Customer' label should be visible."""
        assert "Select Customer" in self.body, (
            "Select Customer label not found"
        )
        log_event("INFO", "TC-BIL-013 PASSED: Select Customer label present")
