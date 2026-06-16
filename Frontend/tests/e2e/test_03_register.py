"""
Test Suite 03: Registration Page
================================
Tests the registration form fields, validation rules,
and navigation between register and login pages.
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


class TestRegisterPage:
    """Registration page test cases."""

    @pytest.fixture(autouse=True)
    def setup(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        navigate_to(driver, base_url, "#register")
        self.body = get_page_text(driver)
        log_event("INFO", "Navigated to Register page")

    # ------------------------------------------------------------------
    # TC-REG-001: Registration form is visible
    # ------------------------------------------------------------------
    def test_register_form_visible(self):
        """The registration form with id='register-form' should exist."""
        form = self.driver.find_elements(By.ID, "register-form")
        assert len(form) > 0, "Registration form not found"
        log_event("INFO", "TC-REG-001 PASSED: Registration form visible")

    # ------------------------------------------------------------------
    # TC-REG-002: Create Account heading
    # ------------------------------------------------------------------
    def test_create_account_heading(self):
        """The heading 'Create an Account' should be visible."""
        assert "Create an Account" in self.body, (
            "'Create an Account' heading not found"
        )
        log_event("INFO", "TC-REG-002 PASSED: Heading present")

    # ------------------------------------------------------------------
    # TC-REG-003: Business Name field present
    # ------------------------------------------------------------------
    def test_business_name_field(self):
        """Business Name input with id='merchant_name' should exist."""
        field = self.driver.find_elements(By.ID, "merchant_name")
        assert len(field) > 0, "Business Name field not found"
        log_event("INFO", "TC-REG-003 PASSED: Business Name field present")

    # ------------------------------------------------------------------
    # TC-REG-004: Email field present
    # ------------------------------------------------------------------
    def test_email_field_present(self):
        """Email input with id='reg-email' should exist."""
        field = self.driver.find_elements(By.ID, "reg-email")
        assert len(field) > 0, "Email field not found"
        log_event("INFO", "TC-REG-004 PASSED: Email field present")

    # ------------------------------------------------------------------
    # TC-REG-005: Phone field present
    # ------------------------------------------------------------------
    def test_phone_field_present(self):
        """Phone input with id='phone' should exist."""
        field = self.driver.find_elements(By.ID, "phone")
        assert len(field) > 0, "Phone field not found"
        log_event("INFO", "TC-REG-005 PASSED: Phone field present")

    # ------------------------------------------------------------------
    # TC-REG-006: PIN field present with maxlength
    # ------------------------------------------------------------------
    def test_pin_field_with_maxlength(self):
        """PIN input should have maxlength='4'."""
        pw = self.driver.find_element(By.ID, "reg-password")
        maxlen = pw.get_attribute("maxlength")
        assert maxlen == "4", f"Expected maxlength=4, got '{maxlen}'"
        log_event("INFO", "TC-REG-006 PASSED: PIN maxlength=4")

    # ------------------------------------------------------------------
    # TC-REG-007: PIN field is password type
    # ------------------------------------------------------------------
    def test_pin_field_is_password_type(self):
        """PIN field type should be 'password' for masking."""
        pw = self.driver.find_element(By.ID, "reg-password")
        assert pw.get_attribute("type") == "password", (
            "PIN field is not type=password"
        )
        log_event("INFO", "TC-REG-007 PASSED: PIN field masked")

    # ------------------------------------------------------------------
    # TC-REG-008: Register button present
    # ------------------------------------------------------------------
    def test_register_button_present(self):
        """The 'Register Account' submit button should be visible."""
        assert "Register Account" in self.body, (
            "'Register Account' button not found"
        )
        log_event("INFO", "TC-REG-008 PASSED: Register button present")

    # ------------------------------------------------------------------
    # TC-REG-009: Login link present
    # ------------------------------------------------------------------
    def test_login_link_present(self):
        """'Login here' link should navigate to #login."""
        link = self.driver.find_element(
            By.CSS_SELECTOR, 'a[href="#login"]'
        )
        assert link is not None, "'Login here' link not found"
        log_event("INFO", "TC-REG-009 PASSED: Login link present")

    # ------------------------------------------------------------------
    # TC-REG-010: Login link navigates correctly
    # ------------------------------------------------------------------
    def test_login_link_navigates(self):
        """Clicking 'Login here' should go to #login."""
        link = self.driver.find_element(
            By.CSS_SELECTOR, 'a[href="#login"]'
        )
        link.click()
        time.sleep(2)
        assert "#login" in self.driver.current_url, (
            f"Expected #login, got {self.driver.current_url}"
        )
        log_event("INFO", "TC-REG-010 PASSED: Login link navigates")

    # ------------------------------------------------------------------
    # TC-REG-011: SB logo on register page
    # ------------------------------------------------------------------
    def test_sb_logo_on_register(self):
        """The 'SB' logo should be visible on the register page."""
        navigate_to(self.driver, self.base_url, "#register")
        body = get_page_text(self.driver)
        assert "SB" in body, "'SB' logo not found on register page"
        log_event("INFO", "TC-REG-011 PASSED: SB logo on register")

    # ------------------------------------------------------------------
    # TC-REG-012: Subtitle text present
    # ------------------------------------------------------------------
    def test_subtitle_text(self):
        """Subtitle 'Register your business to get started' should show."""
        navigate_to(self.driver, self.base_url, "#register")
        body = get_page_text(self.driver)
        assert "Register your business" in body, "Subtitle not found"
        log_event("INFO", "TC-REG-012 PASSED: Subtitle text present")
