"""
Test Suite 10: Settings Page
============================
Tests the settings hub including profile summary,
settings items list, logout, and version info.
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


class TestSettingsPage:
    """Settings page test cases (requires login)."""

    @pytest.fixture(autouse=True)
    def setup(self, logged_in_driver, base_url):
        self.driver = logged_in_driver
        self.base_url = base_url
        navigate_to(self.driver, base_url, "#settings")
        time.sleep(3)
        self.body = get_page_text(self.driver)
        log_event("INFO", "Navigated to Settings page")

    # ------------------------------------------------------------------
    # TC-SET-001: Settings page loads
    # ------------------------------------------------------------------
    def test_settings_page_loads(self):
        """Settings page should load with #settings in URL."""
        assert "#settings" in self.driver.current_url, (
            f"Settings URL not found: {self.driver.current_url}"
        )
        log_event("INFO", "TC-SET-001 PASSED: Settings page loaded")

    # ------------------------------------------------------------------
    # TC-SET-002: Profile name displayed
    # ------------------------------------------------------------------
    def test_profile_name_displayed(self):
        """Profile should show 'Rajesh Kumar'."""
        assert "Rajesh Kumar" in self.body, "Profile name not found"
        log_event("INFO", "TC-SET-002 PASSED: Profile name displayed")

    # ------------------------------------------------------------------
    # TC-SET-003: Pro Member label
    # ------------------------------------------------------------------
    def test_pro_member_label(self):
        """'SmartBiz Pro Member' label should be visible."""
        assert "SmartBiz Pro Member" in self.body, (
            "Pro Member label not found"
        )
        log_event("INFO", "TC-SET-003 PASSED: Pro Member label visible")

    # ------------------------------------------------------------------
    # TC-SET-004: Business Profile setting item
    # ------------------------------------------------------------------
    def test_business_profile_item(self):
        """'Business Profile' setting should be listed."""
        assert "Business Profile" in self.body, (
            "Business Profile item not found"
        )
        log_event("INFO", "TC-SET-004 PASSED: Business Profile listed")

    # ------------------------------------------------------------------
    # TC-SET-005: Staff Management setting item
    # ------------------------------------------------------------------
    def test_staff_management_item(self):
        """'Staff Management' setting should be listed."""
        assert "Staff Management" in self.body, (
            "Staff Management item not found"
        )
        log_event("INFO", "TC-SET-005 PASSED: Staff Management listed")

    # ------------------------------------------------------------------
    # TC-SET-006: Printer Settings item
    # ------------------------------------------------------------------
    def test_printer_settings_item(self):
        """'Printer Settings' setting should be listed."""
        assert "Printer Settings" in self.body, (
            "Printer Settings item not found"
        )
        log_event("INFO", "TC-SET-006 PASSED: Printer Settings listed")

    # ------------------------------------------------------------------
    # TC-SET-007: Notifications setting item
    # ------------------------------------------------------------------
    def test_notifications_item(self):
        """'Notifications' setting should be listed."""
        assert "Notifications" in self.body, "Notifications item not found"
        log_event("INFO", "TC-SET-007 PASSED: Notifications listed")

    # ------------------------------------------------------------------
    # TC-SET-008: Help & Support setting item
    # ------------------------------------------------------------------
    def test_help_support_item(self):
        """'Help & Support' setting should be listed."""
        assert "Help" in self.body and "Support" in self.body, (
            "Help & Support item not found"
        )
        log_event("INFO", "TC-SET-008 PASSED: Help & Support listed")

    # ------------------------------------------------------------------
    # TC-SET-009: Settings list has 6 items
    # ------------------------------------------------------------------
    def test_settings_list_count(self):
        """Settings list should have 6 clickable items."""
        items = self.driver.find_elements(
            By.CSS_SELECTOR, ".settings-list .settings-item"
        )
        assert len(items) == 6, f"Expected 6 settings, found {len(items)}"
        log_event("INFO", "TC-SET-009 PASSED: 6 settings items")

    # ------------------------------------------------------------------
    # TC-SET-010: Logout button present
    # ------------------------------------------------------------------
    def test_logout_button_present(self):
        """A logout button should be present on the settings page."""
        buttons = self.driver.find_elements(
            By.CSS_SELECTOR, ".btn-outline.text-error"
        )
        assert len(buttons) > 0, "Logout button not found"
        log_event("INFO", "TC-SET-010 PASSED: Logout button present")

    # ------------------------------------------------------------------
    # TC-SET-011: Version info displayed
    # ------------------------------------------------------------------
    def test_version_info(self):
        """Version info 'SmartBiz v2.4.0 (Stable)' should be visible."""
        assert "v2.4.0" in self.body, "Version info not found"
        log_event("INFO", "TC-SET-011 PASSED: Version info displayed")

    # ------------------------------------------------------------------
    # TC-SET-012: Logout navigates to login
    # ------------------------------------------------------------------
    def test_logout_navigates_to_login(self):
        """Clicking logout should navigate to #login."""
        btn = self.driver.find_element(
            By.CSS_SELECTOR, ".btn-outline.text-error"
        )
        btn.click()
        time.sleep(2)
        assert "#login" in self.driver.current_url, (
            f"Expected #login after logout, got {self.driver.current_url}"
        )
        log_event("INFO", "TC-SET-012 PASSED: Logout navigates to login")

    # ------------------------------------------------------------------
    # TC-SET-013: Business Profile link navigates correctly
    # ------------------------------------------------------------------
    def test_business_profile_link(self):
        """Clicking Business Profile should go to #settings/business_profile."""
        navigate_to(self.driver, self.base_url, "#settings")
        time.sleep(2)
        link = self.driver.find_element(
            By.CSS_SELECTOR, 'a[href="#settings/business_profile"]'
        )
        link.click()
        time.sleep(2)
        assert "#settings/business_profile" in self.driver.current_url, (
            f"Expected business_profile URL, got {self.driver.current_url}"
        )
        log_event("INFO", "TC-SET-013 PASSED: Business Profile navigates")
