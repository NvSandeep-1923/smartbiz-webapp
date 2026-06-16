"""
Test Suite 08: Customers Page
=============================
Tests the customer listing, search, filter chips,
FAB button, and customer navigation.
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


class TestCustomersPage:
    """Customers page test cases (requires login)."""

    @pytest.fixture(autouse=True)
    def setup(self, logged_in_driver, base_url):
        self.driver = logged_in_driver
        self.base_url = base_url
        navigate_to(self.driver, base_url, "#customers")
        time.sleep(3)
        self.body = get_page_text(self.driver)
        log_event("INFO", "Navigated to Customers page")

    # ------------------------------------------------------------------
    # TC-CUS-001: Customers page loads
    # ------------------------------------------------------------------
    def test_customers_page_loads(self):
        """The customers page should load with #customers in URL."""
        assert "#customers" in self.driver.current_url, (
            f"Customers URL not found: {self.driver.current_url}"
        )
        log_event("INFO", "TC-CUS-001 PASSED: Customers page loaded")

    # ------------------------------------------------------------------
    # TC-CUS-002: Search bar present
    # ------------------------------------------------------------------
    def test_search_bar_present(self):
        """The customer search input should be present."""
        search = self.driver.find_elements(By.ID, "customer-search")
        assert len(search) > 0, "Customer search bar not found"
        log_event("INFO", "TC-CUS-002 PASSED: Search bar present")

    # ------------------------------------------------------------------
    # TC-CUS-003: Search placeholder text
    # ------------------------------------------------------------------
    def test_search_placeholder(self):
        """Search input should say 'Search customers...'."""
        search = self.driver.find_element(By.ID, "customer-search")
        placeholder = search.get_attribute("placeholder")
        assert "Search customers" in placeholder, (
            f"Unexpected placeholder: '{placeholder}'"
        )
        log_event("INFO", "TC-CUS-003 PASSED: Search placeholder correct")

    # ------------------------------------------------------------------
    # TC-CUS-004: Filter chips present
    # ------------------------------------------------------------------
    def test_filter_chips_present(self):
        """Filter chips (All, You will Give, You will Get) should exist."""
        chips = self.driver.find_elements(By.CSS_SELECTOR, ".chip")
        chip_texts = [c.text.strip() for c in chips]
        assert "All" in chip_texts, "'All' chip missing"
        assert any("Give" in t for t in chip_texts), "'You will Give' chip missing"
        assert any("Get" in t for t in chip_texts), "'You will Get' chip missing"
        log_event("INFO", "TC-CUS-004 PASSED: Filter chips present")

    # ------------------------------------------------------------------
    # TC-CUS-005: FAB button for adding customer
    # ------------------------------------------------------------------
    def test_fab_button_present(self):
        """The add customer FAB button should be present."""
        fab = self.driver.find_elements(By.ID, "btn-add-customer-fab")
        assert len(fab) > 0, "Add customer FAB not found"
        log_event("INFO", "TC-CUS-005 PASSED: FAB button present")

    # ------------------------------------------------------------------
    # TC-CUS-006: Customer list container exists
    # ------------------------------------------------------------------
    def test_customer_list_container(self):
        """Customer list container should exist."""
        container = self.driver.find_elements(By.ID, "customer-list-container")
        assert len(container) > 0, "Customer list container not found"
        log_event("INFO", "TC-CUS-006 PASSED: List container exists")

    # ------------------------------------------------------------------
    # TC-CUS-007: Customer list shows items or empty state
    # ------------------------------------------------------------------
    def test_customer_list_content(self):
        """Customer list should show items or an empty state."""
        container = self.driver.find_element(By.ID, "customer-list-container")
        text = container.text
        has_items = len(self.driver.find_elements(
            By.CSS_SELECTOR, ".customer-item"
        )) > 0
        has_empty = "No customers" in text or "Loading" in text or "Failed" in text
        assert has_items or has_empty, "Neither items nor empty state shown"
        log_event("INFO", "TC-CUS-007 PASSED: Content displayed correctly")

    # ------------------------------------------------------------------
    # TC-CUS-008: Header title shows Customers
    # ------------------------------------------------------------------
    def test_header_title(self):
        """Header title should display 'Customers'."""
        assert "Customers" in self.body, "Customers header not found"
        log_event("INFO", "TC-CUS-008 PASSED: Header title correct")

    # ------------------------------------------------------------------
    # TC-CUS-009: Bottom navigation visible
    # ------------------------------------------------------------------
    def test_bottom_nav_present(self):
        """Bottom navigation should be visible."""
        nav = self.driver.find_elements(By.CSS_SELECTOR, ".bottom-nav")
        assert len(nav) > 0, "Bottom navigation not found"
        log_event("INFO", "TC-CUS-009 PASSED: Bottom nav present")

    # ------------------------------------------------------------------
    # TC-CUS-010: 'All' chip is active by default
    # ------------------------------------------------------------------
    def test_all_chip_active(self):
        """The 'All' chip should be active by default."""
        chips = self.driver.find_elements(By.CSS_SELECTOR, ".chip")
        first_active = [c for c in chips if "active" in c.get_attribute("class")]
        assert len(first_active) > 0, "No active chip found"
        assert "All" in first_active[0].text, "Active chip is not 'All'"
        log_event("INFO", "TC-CUS-010 PASSED: 'All' chip active")
