"""
Test Suite 09: Reports Page
===========================
Tests the reports hub including AI insights, business report
links, customer credit risk section, and navigation.
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


class TestReportsPage:
    """Reports page test cases (requires login)."""

    @pytest.fixture(autouse=True)
    def setup(self, logged_in_driver, base_url):
        self.driver = logged_in_driver
        self.base_url = base_url
        navigate_to(self.driver, base_url, "#reports")
        time.sleep(3)
        self.body = get_page_text(self.driver)
        log_event("INFO", "Navigated to Reports page")

    # ------------------------------------------------------------------
    # TC-RPT-001: Reports page loads
    # ------------------------------------------------------------------
    def test_reports_page_loads(self):
        """The reports page should load with #reports in URL."""
        assert "#reports" in self.driver.current_url, (
            f"Reports URL not found: {self.driver.current_url}"
        )
        log_event("INFO", "TC-RPT-001 PASSED: Reports page loaded")

    # ------------------------------------------------------------------
    # TC-RPT-002: Data Insights section visible
    # ------------------------------------------------------------------
    def test_data_insights_section(self):
        """The 'Data Insights' section should be present."""
        assert "Data Insights" in self.body, "Data Insights section not found"
        log_event("INFO", "TC-RPT-002 PASSED: Data Insights visible")

    # ------------------------------------------------------------------
    # TC-RPT-003: AI insights section has gradient style
    # ------------------------------------------------------------------
    def test_ai_insights_gradient_section(self):
        """The AI insights card should exist with styling."""
        card = self.driver.find_elements(By.CSS_SELECTOR, ".ai-insights")
        assert len(card) > 0, "AI insights card not found"
        log_event("INFO", "TC-RPT-003 PASSED: AI insights card exists")

    # ------------------------------------------------------------------
    # TC-RPT-004: Create Order button present
    # ------------------------------------------------------------------
    def test_create_order_button(self):
        """The 'Create Order' button should be present."""
        assert "Create Order" in self.body, "Create Order button not found"
        log_event("INFO", "TC-RPT-004 PASSED: Create Order button present")

    # ------------------------------------------------------------------
    # TC-RPT-005: Create Order navigates to inventory/add
    # ------------------------------------------------------------------
    def test_create_order_navigates(self):
        """Clicking 'Create Order' should navigate to #inventory/add."""
        btn = self.driver.find_element(By.ID, "btn-reports-action")
        btn.click()
        time.sleep(2)
        assert "#inventory/add" in self.driver.current_url, (
            f"Expected #inventory/add, got {self.driver.current_url}"
        )
        log_event("INFO", "TC-RPT-005 PASSED: Create Order navigates")

    # ------------------------------------------------------------------
    # TC-RPT-006: Business Reports section visible
    # ------------------------------------------------------------------
    def test_business_reports_section(self):
        """The 'Business Reports' section should be present."""
        navigate_to(self.driver, self.base_url, "#reports")
        time.sleep(2)
        body = get_page_text(self.driver)
        assert "Business Reports" in body, "Business Reports section not found"
        log_event("INFO", "TC-RPT-006 PASSED: Business Reports visible")

    # ------------------------------------------------------------------
    # TC-RPT-007: Daybook report link
    # ------------------------------------------------------------------
    def test_daybook_link_present(self):
        """The Daybook report link should exist."""
        navigate_to(self.driver, self.base_url, "#reports")
        time.sleep(2)
        link = self.driver.find_elements(
            By.CSS_SELECTOR, 'a[href="#reports/daybook"]'
        )
        assert len(link) > 0, "Daybook link not found"
        log_event("INFO", "TC-RPT-007 PASSED: Daybook link present")

    # ------------------------------------------------------------------
    # TC-RPT-008: P&L report link
    # ------------------------------------------------------------------
    def test_pnl_link_present(self):
        """The P&L Statement report link should exist."""
        navigate_to(self.driver, self.base_url, "#reports")
        time.sleep(2)
        link = self.driver.find_elements(
            By.CSS_SELECTOR, 'a[href="#reports/pnl"]'
        )
        assert len(link) > 0, "P&L link not found"
        log_event("INFO", "TC-RPT-008 PASSED: P&L link present")

    # ------------------------------------------------------------------
    # TC-RPT-009: Tax & GST report link
    # ------------------------------------------------------------------
    def test_tax_link_present(self):
        """The Tax & GST report link should exist."""
        navigate_to(self.driver, self.base_url, "#reports")
        time.sleep(2)
        link = self.driver.find_elements(
            By.CSS_SELECTOR, 'a[href="#reports/tax"]'
        )
        assert len(link) > 0, "Tax & GST link not found"
        log_event("INFO", "TC-RPT-009 PASSED: Tax link present")

    # ------------------------------------------------------------------
    # TC-RPT-010: Sales Forecast report link
    # ------------------------------------------------------------------
    def test_forecast_link_present(self):
        """The Sales Forecast report link should exist."""
        navigate_to(self.driver, self.base_url, "#reports")
        time.sleep(2)
        link = self.driver.find_elements(
            By.CSS_SELECTOR, 'a[href="#reports/forecast"]'
        )
        assert len(link) > 0, "Sales Forecast link not found"
        log_event("INFO", "TC-RPT-010 PASSED: Forecast link present")

    # ------------------------------------------------------------------
    # TC-RPT-011: Customer Credit Risk section
    # ------------------------------------------------------------------
    def test_credit_risk_section(self):
        """The 'Customer Credit Risk' section should be present."""
        navigate_to(self.driver, self.base_url, "#reports")
        time.sleep(2)
        body = get_page_text(self.driver)
        assert "Customer Credit Risk" in body, (
            "Credit Risk section not found"
        )
        log_event("INFO", "TC-RPT-011 PASSED: Credit Risk section visible")

    # ------------------------------------------------------------------
    # TC-RPT-012: Portfolio Health gauge visible
    # ------------------------------------------------------------------
    def test_portfolio_health_gauge(self):
        """The portfolio health gauge showing percentage should exist."""
        navigate_to(self.driver, self.base_url, "#reports")
        time.sleep(2)
        gauge = self.driver.find_elements(By.CSS_SELECTOR, ".risk-gauge")
        assert len(gauge) > 0, "Portfolio health gauge not found"
        assert "%" in gauge[0].text, "Gauge does not show percentage"
        log_event("INFO", "TC-RPT-012 PASSED: Health gauge visible")

    # ------------------------------------------------------------------
    # TC-RPT-013: Reports grid has 4 items
    # ------------------------------------------------------------------
    def test_reports_grid_count(self):
        """Reports grid should have exactly 4 report items."""
        navigate_to(self.driver, self.base_url, "#reports")
        time.sleep(2)
        items = self.driver.find_elements(
            By.CSS_SELECTOR, ".reports-grid .report-item"
        )
        assert len(items) == 4, f"Expected 4 report items, found {len(items)}"
        log_event("INFO", "TC-RPT-013 PASSED: 4 report items in grid")
