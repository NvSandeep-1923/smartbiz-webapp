"""
Test Suite 01: Onboarding / Landing Page
=========================================
Tests the initial onboarding carousel, slide content,
navigation dots, and CTA buttons.
"""

import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from helpers import (
    log_event, wait_for_element, wait_for_visible,
    get_page_text, navigate_to, PAGE_LOAD_WAIT, DEFAULT_TIMEOUT,
)


class TestOnboardingPage:
    """Onboarding / Landing page test cases."""

    @pytest.fixture(autouse=True)
    def setup(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        navigate_to(driver, base_url, "")
        self.body = get_page_text(driver)
        log_event("INFO", "Navigated to Onboarding page")

    # ------------------------------------------------------------------
    # TC-ONB-001: Page loads successfully
    # ------------------------------------------------------------------
    def test_page_loads_successfully(self):
        """The onboarding page should load without errors."""
        assert self.driver.title, "Page title should not be empty"
        log_event("INFO", "TC-ONB-001 PASSED: Page loaded successfully")

    # ------------------------------------------------------------------
    # TC-ONB-002: Page title matches app name
    # ------------------------------------------------------------------
    def test_page_title_matches_app_name(self):
        """The page title should contain 'SmartBiz'."""
        assert "SmartBiz" in self.driver.title, (
            f"Expected 'SmartBiz' in title, got '{self.driver.title}'"
        )
        log_event("INFO", "TC-ONB-002 PASSED: Title matches")

    # ------------------------------------------------------------------
    # TC-ONB-003: Onboarding container is rendered
    # ------------------------------------------------------------------
    def test_onboarding_container_rendered(self):
        """The onboarding container should be visible."""
        container = self.driver.find_elements(
            By.CSS_SELECTOR, ".onboarding-container"
        )
        assert len(container) > 0, "Onboarding container not found"
        log_event("INFO", "TC-ONB-003 PASSED: Container rendered")

    # ------------------------------------------------------------------
    # TC-ONB-004: Slide 1 – Smart Inventory
    # ------------------------------------------------------------------
    def test_slide_smart_inventory_visible(self):
        """The 'Smart Inventory' slide text should be present."""
        assert "Smart Inventory" in self.body, (
            "Slide 'Smart Inventory' not found in page text"
        )
        log_event("INFO", "TC-ONB-004 PASSED: Smart Inventory slide present")

    # ------------------------------------------------------------------
    # TC-ONB-005: Slide 2 – Digital Invoicing
    # ------------------------------------------------------------------
    def test_slide_digital_invoicing_visible(self):
        """The 'Digital Invoicing' slide text should be present."""
        assert "Digital Invoicing" in self.body, (
            "Slide 'Digital Invoicing' not found in page text"
        )
        log_event("INFO", "TC-ONB-005 PASSED: Digital Invoicing slide present")

    # ------------------------------------------------------------------
    # TC-ONB-006: Slide 3 – Customer Ledger
    # ------------------------------------------------------------------
    def test_slide_customer_ledger_visible(self):
        """The 'Customer Ledger' slide text should be present."""
        assert "Customer Ledger" in self.body, (
            "Slide 'Customer Ledger' not found in page text"
        )
        log_event("INFO", "TC-ONB-006 PASSED: Customer Ledger slide present")

    # ------------------------------------------------------------------
    # TC-ONB-007: Carousel has exactly 3 slides
    # ------------------------------------------------------------------
    def test_carousel_has_three_slides(self):
        """The carousel should contain exactly 3 slides."""
        slides = self.driver.find_elements(
            By.CSS_SELECTOR, ".onboarding-slide"
        )
        assert len(slides) == 3, (
            f"Expected 3 slides, found {len(slides)}"
        )
        log_event("INFO", "TC-ONB-007 PASSED: 3 slides present")

    # ------------------------------------------------------------------
    # TC-ONB-008: Navigation dots are present
    # ------------------------------------------------------------------
    def test_navigation_dots_present(self):
        """Three navigation dots should be rendered."""
        dots = self.driver.find_elements(By.CSS_SELECTOR, ".dot")
        assert len(dots) == 3, f"Expected 3 dots, found {len(dots)}"
        log_event("INFO", "TC-ONB-008 PASSED: 3 dots present")

    # ------------------------------------------------------------------
    # TC-ONB-009: First dot is active by default
    # ------------------------------------------------------------------
    def test_first_dot_is_active(self):
        """The first navigation dot should be active."""
        dots = self.driver.find_elements(By.CSS_SELECTOR, ".dot")
        assert "active" in dots[0].get_attribute("class"), (
            "First dot is not active"
        )
        log_event("INFO", "TC-ONB-009 PASSED: First dot is active")

    # ------------------------------------------------------------------
    # TC-ONB-010: Get Started button is visible
    # ------------------------------------------------------------------
    def test_get_started_button_visible(self):
        """The 'Get Started' button should be present."""
        assert "Get Started" in self.body, (
            "'Get Started' button text not found"
        )
        log_event("INFO", "TC-ONB-010 PASSED: Get Started button visible")

    # ------------------------------------------------------------------
    # TC-ONB-011: Get Started button navigates to login
    # ------------------------------------------------------------------
    def test_get_started_navigates_to_login(self):
        """Clicking 'Get Started' should navigate to #login."""
        btn = self.driver.find_element(
            By.CSS_SELECTOR, ".onboarding-footer .btn-primary"
        )
        btn.click()
        time.sleep(2)
        assert "#login" in self.driver.current_url, (
            f"Expected #login in URL, got {self.driver.current_url}"
        )
        log_event("INFO", "TC-ONB-011 PASSED: Navigated to login")

    # ------------------------------------------------------------------
    # TC-ONB-012: Existing User link navigates to login
    # ------------------------------------------------------------------
    def test_existing_user_link_navigates_to_login(self):
        """The 'Existing User? Log In' link should navigate to #login."""
        navigate_to(self.driver, self.base_url, "")
        link = self.driver.find_element(By.CSS_SELECTOR, ".btn-text")
        link.click()
        time.sleep(2)
        assert "#login" in self.driver.current_url, (
            f"Expected #login in URL, got {self.driver.current_url}"
        )
        log_event("INFO", "TC-ONB-012 PASSED: Existing user link works")

    # ------------------------------------------------------------------
    # TC-ONB-013: Onboarding icons render
    # ------------------------------------------------------------------
    def test_onboarding_icons_render(self):
        """Onboarding slide icons (emoji) should render."""
        navigate_to(self.driver, self.base_url, "")
        icons = self.driver.find_elements(By.CSS_SELECTOR, ".onboarding-icon")
        assert len(icons) >= 3, f"Expected 3 icons, found {len(icons)}"
        log_event("INFO", "TC-ONB-013 PASSED: Icons rendered")

    # ------------------------------------------------------------------
    # TC-ONB-014: Slide descriptions are present
    # ------------------------------------------------------------------
    def test_slide_descriptions_present(self):
        """Each slide should have a description paragraph."""
        navigate_to(self.driver, self.base_url, "")
        body = get_page_text(self.driver)
        assert "Manage stock alerts" in body, "Slide 1 description missing"
        assert "GST invoices" in body, "Slide 2 description missing"
        assert "udhar" in body.lower() or "payment reminders" in body.lower(), (
            "Slide 3 description missing"
        )
        log_event("INFO", "TC-ONB-014 PASSED: Slide descriptions present")
