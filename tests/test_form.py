import pytest
from pages.form_page import FormPage

def take_screenshot(driver, name):
    driver.save_screenshot(f"screenshots/{name}.png")


def test_valid_form_submission(driver):
    form = FormPage(driver)
    form.open()

    form.fill_form("Divyaraj", "test@example.com", "Rajkot Gujarat")
    form.submit_form()

    try:
        assert "Divyaraj" in form.get_output_name()
        assert "test@example.com" in form.get_output_email()
    except Exception:
        take_screenshot(driver, "valid_form_failure")
        raise


def test_invalid_email_submission(driver):
    form = FormPage(driver)
    form.open()

    form.fill_form("Divyaraj", "invalid-email", "Rajkot Gujarat")
    form.submit_form()

    try:
        assert form.is_email_invalid()
    except Exception:
        take_screenshot(driver, "invalid_email_failure")
        raise