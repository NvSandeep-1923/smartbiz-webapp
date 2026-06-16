"""
Test Suite 04: Dashboard Page
=============================
Tests the main dashboard after login including KPI cards,
quick actions, charts, recent transactions, and navigation.
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


class TestDashboard:
    """Dashboard page test cases (requires login)."""

    @pytest.fixture(autouse=True)
    def setup(self, logged_in_driver, base_url):
        self.driver = logged_in_driver
        self.base_url = base_url
        navigate_to(self.driver, base_url, "#dashboard")
        time.sleep(3)
        self.body = get_page_text(self.driver)
        log_event("INFO", "Navigated to Dashboard page (logged in)")

    # ------------------------------------------------------------------
    # TC-DSH-001: Dashboard loads after login
    # ------------------------------------------------------------------
    def test_dashboard_loads(self):
        """Dashboard page should load with #dashboard in URL."""
        assert "#dashboard" in self.driver.current_url, (
            f"Dashboard URL not found: {self.driver.current_url}"
        )
        log_event("INFO", "TC-DSH-001 PASSED: Dashboard loaded")

    # ------------------------------------------------------------------
    # TC-DSH-002: KPI card – Total Sales
    # ------------------------------------------------------------------
    def test_kpi_total_sales_visible(self):
        """The 'Total Sales' KPI card should be visible."""
        kpi = self.driver.find_elements(By.ID, "kpi-total-sales")
        assert len(kpi) > 0, "Total Sales KPI not found"
        log_event("INFO", "TC-DSH-002 PASSED: Total Sales KPI visible")

    # ------------------------------------------------------------------
    # TC-DSH-003: KPI card – Total Udhar
    # ------------------------------------------------------------------
    def test_kpi_total_udhar_visible(self):
        """The 'Total Udhar' KPI card should be visible."""
        kpi = self.driver.find_elements(By.ID, "kpi-total-udhar")
        assert len(kpi) > 0, "Total Udhar KPI not found"
        log_event("INFO", "TC-DSH-003 PASSED: Total Udhar KPI visible")

    # ------------------------------------------------------------------
    # TC-DSH-004: KPI card – Stock Alerts
    # ------------------------------------------------------------------
    def test_kpi_stock_alerts_visible(self):
        """The 'Stock Alerts' KPI card should be visible."""
        kpi = self.driver.find_elements(By.ID, "kpi-stock-alerts")
        assert len(kpi) > 0, "Stock Alerts KPI not found"
        log_event("INFO", "TC-DSH-004 PASSED: Stock Alerts KPI visible")

    # ------------------------------------------------------------------
    # TC-DSH-005: KPI card – Cash in Hand
    # ------------------------------------------------------------------
    def test_kpi_cash_in_hand_visible(self):
        """The 'Cash in Hand' KPI card should be visible."""
        kpi = self.driver.find_elements(By.ID, "kpi-cash-hand")
        assert len(kpi) > 0, "Cash in Hand KPI not found"
        log_event("INFO", "TC-DSH-005 PASSED: Cash in Hand KPI visible")

    # ------------------------------------------------------------------
    # TC-DSH-006: KPI values display currency symbol
    # ------------------------------------------------------------------
    def test_kpi_values_display_currency(self):
        """KPI values should display the ₹ currency symbol."""
        kpi_sales = self.driver.find_element(By.ID, "kpi-total-sales")
        assert "₹" in kpi_sales.text, "Currency ₹ not found in Total Sales"
        log_event("INFO", "TC-DSH-006 PASSED: Currency symbol displayed")

    # ------------------------------------------------------------------
    # TC-DSH-007: Quick Actions section visible
    # ------------------------------------------------------------------
    def test_quick_actions_visible(self):
        """The Quick Actions section should be present."""
        actions = self.driver.find_elements(By.CSS_SELECTOR, ".quick-actions")
        assert len(actions) > 0, "Quick Actions section not found"
        log_event("INFO", "TC-DSH-007 PASSED: Quick Actions visible")

    # ------------------------------------------------------------------
    # TC-DSH-008: Add Customer quick action
    # ------------------------------------------------------------------
    def test_add_customer_button(self):
        """'Add Customer' quick action button should exist."""
        btn = self.driver.find_elements(By.ID, "btn-add-customer")
        assert len(btn) > 0, "Add Customer button not found"
        log_event("INFO", "TC-DSH-008 PASSED: Add Customer button found")

    # ------------------------------------------------------------------
    # TC-DSH-009: Add Customer navigates to customers
    # ------------------------------------------------------------------
    def test_add_customer_navigates(self):
        """Clicking Add Customer should navigate to #customers."""
        btn = self.driver.find_element(By.ID, "btn-add-customer")
        btn.click()
        time.sleep(2)
        assert "#customers" in self.driver.current_url, (
            f"Expected #customers, got {self.driver.current_url}"
        )
        log_event("INFO", "TC-DSH-009 PASSED: Add Customer navigates")

    # ------------------------------------------------------------------
    # TC-DSH-010: Create Invoice quick action
    # ------------------------------------------------------------------
    def test_create_invoice_button(self):
        """'Create Invoice' quick action button should exist."""
        navigate_to(self.driver, self.base_url, "#dashboard")
        time.sleep(2)
        btn = self.driver.find_elements(By.ID, "btn-new-invoice")
        assert len(btn) > 0, "Create Invoice button not found"
        log_event("INFO", "TC-DSH-010 PASSED: Create Invoice button found")

    # ------------------------------------------------------------------
    # TC-DSH-011: Add Stock quick action
    # ------------------------------------------------------------------
    def test_add_stock_button(self):
        """'Add Stock' quick action button should exist."""
        navigate_to(self.driver, self.base_url, "#dashboard")
        time.sleep(2)
        btn = self.driver.find_elements(By.ID, "btn-add-stock")
        assert len(btn) > 0, "Add Stock button not found"
        log_event("INFO", "TC-DSH-011 PASSED: Add Stock button found")

    # ------------------------------------------------------------------
    # TC-DSH-012: Reports quick action
    # ------------------------------------------------------------------
    def test_reports_button(self):
        """'Reports' quick action button should exist."""
        navigate_to(self.driver, self.base_url, "#dashboard")
        time.sleep(2)
        btn = self.driver.find_elements(By.ID, "btn-check-reports")
        assert len(btn) > 0, "Reports button not found"
        log_event("INFO", "TC-DSH-012 PASSED: Reports button found")

    # ------------------------------------------------------------------
    # TC-DSH-013: Weekly Sales chart section
    # ------------------------------------------------------------------
    def test_weekly_sales_chart_visible(self):
        """The Weekly Sales Trend chart section should be present."""
        navigate_to(self.driver, self.base_url, "#dashboard")
        time.sleep(2)
        body = get_page_text(self.driver)
        assert "Weekly Sales Trend" in body, "Sales chart section not found"
        log_event("INFO", "TC-DSH-013 PASSED: Sales chart visible")

    # ------------------------------------------------------------------
    # TC-DSH-014: Bar chart has 7 bars
    # ------------------------------------------------------------------
    def test_bar_chart_seven_bars(self):
        """The bar chart should contain 7 bars for each day."""
        navigate_to(self.driver, self.base_url, "#dashboard")
        time.sleep(2)
        bars = self.driver.find_elements(By.CSS_SELECTOR, ".bar-chart .bar")
        assert len(bars) == 7, f"Expected 7 bars, found {len(bars)}"
        log_event("INFO", "TC-DSH-014 PASSED: 7 bars in chart")

    # ------------------------------------------------------------------
    # TC-DSH-015: Recent Transactions section
    # ------------------------------------------------------------------
    def test_recent_transactions_section(self):
        """The Recent Transactions section should be present."""
        navigate_to(self.driver, self.base_url, "#dashboard")
        time.sleep(2)
        body = get_page_text(self.driver)
        assert "Recent Transactions" in body, (
            "Recent Transactions section not found"
        )
        log_event("INFO", "TC-DSH-015 PASSED: Recent Transactions visible")

    # ------------------------------------------------------------------
    # TC-DSH-016: Notification bell in header
    # ------------------------------------------------------------------
    def test_notification_bell_present(self):
        """The notification bell icon should be in the header."""
        navigate_to(self.driver, self.base_url, "#dashboard")
        time.sleep(2)
        bells = self.driver.find_elements(By.CSS_SELECTOR, ".ph-bell")
        assert len(bells) > 0, "Notification bell icon not found"
        log_event("INFO", "TC-DSH-016 PASSED: Notification bell present")

    # ------------------------------------------------------------------
    # TC-DSH-017: Bottom navigation is visible
    # ------------------------------------------------------------------
    def test_bottom_navigation_visible(self):
        """The bottom navigation bar should be present."""
        navigate_to(self.driver, self.base_url, "#dashboard")
        time.sleep(2)
        nav = self.driver.find_elements(By.CSS_SELECTOR, ".bottom-nav")
        assert len(nav) > 0, "Bottom navigation not found"
        log_event("INFO", "TC-DSH-017 PASSED: Bottom nav visible")
