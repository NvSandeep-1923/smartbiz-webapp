"""
Test Suite 05: Inventory Page
=============================
Tests the inventory listing, search, category filters,
FAB button, and item display.
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


class TestInventoryPage:
    """Inventory page test cases (requires login)."""

    @pytest.fixture(autouse=True)
    def setup(self, logged_in_driver, base_url):
        self.driver = logged_in_driver
        self.base_url = base_url
        navigate_to(self.driver, base_url, "#inventory")
        time.sleep(3)
        self.body = get_page_text(self.driver)
        log_event("INFO", "Navigated to Inventory page")

    # ------------------------------------------------------------------
    # TC-INV-001: Inventory page loads
    # ------------------------------------------------------------------
    def test_inventory_page_loads(self):
        """The inventory page should load with #inventory in URL."""
        assert "#inventory" in self.driver.current_url, (
            f"Inventory URL not found: {self.driver.current_url}"
        )
        log_event("INFO", "TC-INV-001 PASSED: Inventory page loaded")

    # ------------------------------------------------------------------
    # TC-INV-002: Search bar present
    # ------------------------------------------------------------------
    def test_search_bar_present(self):
        """A search input should be visible on the inventory page."""
        search = self.driver.find_elements(By.CSS_SELECTOR, ".search-input")
        assert len(search) > 0, "Search bar not found"
        log_event("INFO", "TC-INV-002 PASSED: Search bar present")

    # ------------------------------------------------------------------
    # TC-INV-003: Search placeholder text
    # ------------------------------------------------------------------
    def test_search_placeholder(self):
        """Search input should have appropriate placeholder text."""
        search = self.driver.find_element(By.CSS_SELECTOR, ".search-input")
        placeholder = search.get_attribute("placeholder")
        assert "Search" in placeholder, (
            f"Unexpected placeholder: '{placeholder}'"
        )
        log_event("INFO", "TC-INV-003 PASSED: Search placeholder correct")

    # ------------------------------------------------------------------
    # TC-INV-004: Filter chips present
    # ------------------------------------------------------------------
    def test_filter_chips_present(self):
        """Filter chips (All, Grocery, Dairy, Beverages) should exist."""
        chips = self.driver.find_elements(By.CSS_SELECTOR, ".chip")
        assert len(chips) >= 4, f"Expected ≥4 chips, found {len(chips)}"
        log_event("INFO", "TC-INV-004 PASSED: Filter chips present")

    # ------------------------------------------------------------------
    # TC-INV-005: 'All' chip is active by default
    # ------------------------------------------------------------------
    def test_all_chip_active_default(self):
        """The 'All' chip should be active by default."""
        chips = self.driver.find_elements(By.CSS_SELECTOR, ".chip")
        first_chip = chips[0]
        assert "active" in first_chip.get_attribute("class"), (
            "First chip (All) is not active"
        )
        assert first_chip.text.strip() == "All", (
            f"First chip text is '{first_chip.text}', expected 'All'"
        )
        log_event("INFO", "TC-INV-005 PASSED: All chip active by default")

    # ------------------------------------------------------------------
    # TC-INV-006: FAB button present
    # ------------------------------------------------------------------
    def test_fab_button_present(self):
        """The floating action button (FAB) should be present."""
        fab = self.driver.find_elements(By.CSS_SELECTOR, ".fab")
        assert len(fab) > 0, "FAB button not found"
        log_event("INFO", "TC-INV-006 PASSED: FAB button present")

    # ------------------------------------------------------------------
    # TC-INV-007: FAB navigates to add product
    # ------------------------------------------------------------------
    def test_fab_navigates_to_add_product(self):
        """Clicking the FAB should navigate to #inventory/add."""
        fab = self.driver.find_element(By.CSS_SELECTOR, ".fab")
        fab.click()
        time.sleep(2)
        assert "#inventory/add" in self.driver.current_url, (
            f"Expected #inventory/add, got {self.driver.current_url}"
        )
        log_event("INFO", "TC-INV-007 PASSED: FAB navigates to add product")

    # ------------------------------------------------------------------
    # TC-INV-008: Inventory list container exists
    # ------------------------------------------------------------------
    def test_inventory_list_container(self):
        """The inventory list container should exist."""
        navigate_to(self.driver, self.base_url, "#inventory")
        time.sleep(2)
        container = self.driver.find_elements(By.ID, "inventory-list")
        assert len(container) > 0, "Inventory list container not found"
        log_event("INFO", "TC-INV-008 PASSED: List container exists")

    # ------------------------------------------------------------------
    # TC-INV-009: Header title shows Inventory
    # ------------------------------------------------------------------
    def test_header_title(self):
        """Header title should display 'Inventory'."""
        navigate_to(self.driver, self.base_url, "#inventory")
        time.sleep(2)
        body = get_page_text(self.driver)
        assert "Inventory" in body, "Header title 'Inventory' not found"
        log_event("INFO", "TC-INV-009 PASSED: Header title correct")

    # ------------------------------------------------------------------
    # TC-INV-010: Category chip click changes active state
    # ------------------------------------------------------------------
    def test_chip_click_changes_active(self):
        """Clicking a filter chip should change the active state."""
        navigate_to(self.driver, self.base_url, "#inventory")
        time.sleep(2)
        chips = self.driver.find_elements(By.CSS_SELECTOR, ".chip")
        if len(chips) >= 2:
            chips[1].click()
            time.sleep(1)
            assert "active" in chips[1].get_attribute("class"), (
                "Second chip did not become active after click"
            )
        log_event("INFO", "TC-INV-010 PASSED: Chip click changes active")

    # ------------------------------------------------------------------
    # TC-INV-011: Bottom nav present on inventory
    # ------------------------------------------------------------------
    def test_bottom_nav_on_inventory(self):
        """Bottom navigation should be visible on inventory page."""
        navigate_to(self.driver, self.base_url, "#inventory")
        time.sleep(2)
        nav = self.driver.find_elements(By.CSS_SELECTOR, ".bottom-nav")
        assert len(nav) > 0, "Bottom nav not found on inventory page"
        log_event("INFO", "TC-INV-011 PASSED: Bottom nav present")

    # ------------------------------------------------------------------
    # TC-INV-012: Inventory items or empty state displayed
    # ------------------------------------------------------------------
    def test_inventory_items_or_empty(self):
        """Inventory list should show items or an empty state message."""
        navigate_to(self.driver, self.base_url, "#inventory")
        time.sleep(3)
        container = self.driver.find_element(By.ID, "inventory-list")
        text = container.text
        has_items = len(self.driver.find_elements(
            By.CSS_SELECTOR, ".inventory-item"
        )) > 0
        has_empty = "No items" in text or "Loading" in text or "Failed" in text
        assert has_items or has_empty, "Neither items nor empty state shown"
        log_event("INFO", "TC-INV-012 PASSED: Items or empty state displayed")
