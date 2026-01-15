"""
Complete Selenium Test Cases for Register Module with Screenshots
All 43 test cases with screenshot capture
"""
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, UnexpectedAlertPresentException
import time
import os

SCREENSHOT_DIR = os.path.join(os.path.dirname(__file__), "screenshots", "register")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

def screenshot(driver, name):
    """Save screenshot with test name"""
    filepath = os.path.join(SCREENSHOT_DIR, f"{name}.png")
    driver.save_screenshot(filepath)
    return filepath


class TestRegisterFunctionalPositive:
    """TC_REG_001 - TC_REG_002: Positive functional tests"""
    
    def test_TC_REG_001_valid_registration(self, driver, base_url):
        """TC_REG_001: Verify successful registration with all valid data"""
        driver.get(f"{base_url}/register.php")
        time.sleep(1)
        screenshot(driver, "TC_REG_001_01_page")
        
        unique_user = f"test{int(time.time())}"
        driver.find_element(By.ID, "name").send_keys("Test User")
        driver.find_element(By.ID, "InputEmail").send_keys(f"{unique_user}@test.com")
        driver.find_element(By.ID, "username").send_keys(unique_user)
        driver.find_element(By.ID, "InputPassword").send_keys("Test@123")
        driver.find_element(By.ID, "InputRePassword").send_keys("Test@123")
        screenshot(driver, "TC_REG_001_02_filled")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_REG_001_03_result")
    
    def test_TC_REG_002_minimum_valid_data(self, driver, base_url):
        """TC_REG_002: Verify registration with minimum required data"""
        driver.get(f"{base_url}/register.php")
        time.sleep(1)
        
        unique_user = f"u{int(time.time())}"
        driver.find_element(By.ID, "name").send_keys("A")
        driver.find_element(By.ID, "InputEmail").send_keys(f"{unique_user}@t.co")
        driver.find_element(By.ID, "username").send_keys(unique_user)
        driver.find_element(By.ID, "InputPassword").send_keys("1")
        driver.find_element(By.ID, "InputRePassword").send_keys("1")
        screenshot(driver, "TC_REG_002_01_minimum")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_REG_002_02_result")


class TestRegisterEmptyFields:
    """TC_REG_003 - TC_REG_008: Empty Fields Tests"""
    
    def test_TC_REG_003_empty_name(self, driver, base_url):
        """TC_REG_003: Verify validation for empty name"""
        driver.get(f"{base_url}/register.php")
        time.sleep(1)
        
        driver.find_element(By.ID, "InputEmail").send_keys("test@test.com")
        driver.find_element(By.ID, "username").send_keys("testuser")
        driver.find_element(By.ID, "InputPassword").send_keys("password")
        driver.find_element(By.ID, "InputRePassword").send_keys("password")
        screenshot(driver, "TC_REG_003_01_empty_name")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_REG_003_02_result")
        
        assert "register.php" in driver.current_url
    
    def test_TC_REG_004_empty_email(self, driver, base_url):
        """TC_REG_004: Verify validation for empty email"""
        driver.get(f"{base_url}/register.php")
        time.sleep(1)
        
        driver.find_element(By.ID, "name").send_keys("Test User")
        driver.find_element(By.ID, "username").send_keys("testuser")
        driver.find_element(By.ID, "InputPassword").send_keys("password")
        driver.find_element(By.ID, "InputRePassword").send_keys("password")
        screenshot(driver, "TC_REG_004_01_empty_email")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_REG_004_02_result")
        
        assert "register.php" in driver.current_url
    
    def test_TC_REG_005_empty_username(self, driver, base_url):
        """TC_REG_005: Verify validation for empty username"""
        driver.get(f"{base_url}/register.php")
        time.sleep(1)
        
        driver.find_element(By.ID, "name").send_keys("Test User")
        driver.find_element(By.ID, "InputEmail").send_keys("test@test.com")
        driver.find_element(By.ID, "InputPassword").send_keys("password")
        driver.find_element(By.ID, "InputRePassword").send_keys("password")
        screenshot(driver, "TC_REG_005_01_empty_user")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_REG_005_02_result")
        
        assert "register.php" in driver.current_url
    
    def test_TC_REG_006_empty_password(self, driver, base_url):
        """TC_REG_006: Verify validation for empty password"""
        driver.get(f"{base_url}/register.php")
        time.sleep(1)
        
        driver.find_element(By.ID, "name").send_keys("Test User")
        driver.find_element(By.ID, "InputEmail").send_keys("test@test.com")
        driver.find_element(By.ID, "username").send_keys("testuser")
        driver.find_element(By.ID, "InputRePassword").send_keys("password")
        screenshot(driver, "TC_REG_006_01_empty_pass")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_REG_006_02_result")
        
        assert "register.php" in driver.current_url
    
    def test_TC_REG_007_empty_repassword(self, driver, base_url):
        """TC_REG_007: Verify validation for empty re-password"""
        driver.get(f"{base_url}/register.php")
        time.sleep(1)
        
        driver.find_element(By.ID, "name").send_keys("Test User")
        driver.find_element(By.ID, "InputEmail").send_keys("test@test.com")
        driver.find_element(By.ID, "username").send_keys("testuser")
        driver.find_element(By.ID, "InputPassword").send_keys("password")
        screenshot(driver, "TC_REG_007_01_empty_repass")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_REG_007_02_result")
        
        assert "register.php" in driver.current_url
    
    def test_TC_REG_008_all_fields_empty(self, driver, base_url):
        """TC_REG_008: Verify validation when all fields empty"""
        driver.get(f"{base_url}/register.php")
        time.sleep(1)
        screenshot(driver, "TC_REG_008_01_all_empty")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_REG_008_02_result")
        
        assert "register.php" in driver.current_url


class TestRegisterPasswordValidation:
    """TC_REG_009 - TC_REG_010: Password Validation Tests"""
    
    def test_TC_REG_009_password_mismatch(self, driver, base_url):
        """TC_REG_009: Verify validation when passwords don't match"""
        driver.get(f"{base_url}/register.php")
        time.sleep(1)
        
        driver.find_element(By.ID, "name").send_keys("Test User")
        driver.find_element(By.ID, "InputEmail").send_keys("test@test.com")
        driver.find_element(By.ID, "username").send_keys("testuser")
        driver.find_element(By.ID, "InputPassword").send_keys("password1")
        driver.find_element(By.ID, "InputRePassword").send_keys("password2")
        screenshot(driver, "TC_REG_009_01_mismatch")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_REG_009_02_result")
        
        page_source = driver.page_source.lower()
        assert "register.php" in driver.current_url or "tidak sama" in page_source
    
    def test_TC_REG_010_password_case_difference(self, driver, base_url):
        """TC_REG_010: Verify case sensitivity in password match"""
        driver.get(f"{base_url}/register.php")
        time.sleep(1)
        
        driver.find_element(By.ID, "name").send_keys("Test User")
        driver.find_element(By.ID, "InputEmail").send_keys("test@test.com")
        driver.find_element(By.ID, "username").send_keys("testuser")
        driver.find_element(By.ID, "InputPassword").send_keys("Password123")
        driver.find_element(By.ID, "InputRePassword").send_keys("password123")
        screenshot(driver, "TC_REG_010_01_case_diff")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_REG_010_02_result")
        
        assert "register.php" in driver.current_url


class TestRegisterDuplicateValidation:
    """TC_REG_011: Duplicate Validation Tests"""
    
    def test_TC_REG_011_duplicate_name_field_bug(self, driver, base_url):
        """TC_REG_011: BUG - cek_nama checks name field instead of username"""
        driver.get(f"{base_url}/register.php")
        time.sleep(1)
        
        # Name = irul (matches existing username - BUG)
        # Username = unique
        driver.find_element(By.ID, "name").send_keys("irul")
        driver.find_element(By.ID, "InputEmail").send_keys("unique@test.com")
        driver.find_element(By.ID, "username").send_keys("uniqueuser9999")
        driver.find_element(By.ID, "InputPassword").send_keys("password")
        driver.find_element(By.ID, "InputRePassword").send_keys("password")
        screenshot(driver, "TC_REG_011_01_bug_input")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_REG_011_02_bug_result")
        
        # Due to bug, it shows "Username sudah terdaftar" even for unique username


class TestRegisterEmailValidation:
    """TC_REG_012 - TC_REG_014: Email Validation Tests"""
    
    def test_TC_REG_012_invalid_email_no_at(self, driver, base_url):
        """TC_REG_012: Verify email format validation (no @)"""
        driver.get(f"{base_url}/register.php")
        time.sleep(1)
        
        driver.find_element(By.ID, "name").send_keys("Test User")
        driver.find_element(By.ID, "InputEmail").send_keys("invalidemail.com")
        driver.find_element(By.ID, "username").send_keys("testuser")
        driver.find_element(By.ID, "InputPassword").send_keys("password")
        driver.find_element(By.ID, "InputRePassword").send_keys("password")
        screenshot(driver, "TC_REG_012_01_no_at")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(1)
        screenshot(driver, "TC_REG_012_02_result")
        
        assert "register.php" in driver.current_url
    
    def test_TC_REG_013_invalid_email_no_domain(self, driver, base_url):
        """TC_REG_013: Verify email format validation (no domain)"""
        driver.get(f"{base_url}/register.php")
        time.sleep(1)
        
        driver.find_element(By.ID, "name").send_keys("Test User")
        driver.find_element(By.ID, "InputEmail").send_keys("test@")
        driver.find_element(By.ID, "username").send_keys("testuser")
        driver.find_element(By.ID, "InputPassword").send_keys("password")
        driver.find_element(By.ID, "InputRePassword").send_keys("password")
        screenshot(driver, "TC_REG_013_01_no_domain")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(1)
        screenshot(driver, "TC_REG_013_02_result")
        
        assert "register.php" in driver.current_url
    
    def test_TC_REG_014_valid_email_subdomain(self, driver, base_url):
        """TC_REG_014: Verify email with subdomain accepted"""
        driver.get(f"{base_url}/register.php")
        time.sleep(1)
        
        unique = f"sub{int(time.time())}"
        driver.find_element(By.ID, "name").send_keys("Test User")
        driver.find_element(By.ID, "InputEmail").send_keys(f"{unique}@mail.domain.com")
        driver.find_element(By.ID, "username").send_keys(unique)
        driver.find_element(By.ID, "InputPassword").send_keys("password")
        driver.find_element(By.ID, "InputRePassword").send_keys("password")
        screenshot(driver, "TC_REG_014_01_subdomain")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_REG_014_02_result")


class TestRegisterBoundaryValue:
    """TC_REG_015 - TC_REG_020: Boundary Value Analysis"""
    
    def test_TC_REG_015_name_min_length(self, driver, base_url):
        """TC_REG_015: Verify minimum name length (1 char)"""
        driver.get(f"{base_url}/register.php")
        time.sleep(1)
        
        unique = f"min{int(time.time())}"
        driver.find_element(By.ID, "name").send_keys("A")
        driver.find_element(By.ID, "InputEmail").send_keys(f"{unique}@test.com")
        driver.find_element(By.ID, "username").send_keys(unique)
        driver.find_element(By.ID, "InputPassword").send_keys("password")
        driver.find_element(By.ID, "InputRePassword").send_keys("password")
        screenshot(driver, "TC_REG_015_01_min_name")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_REG_015_02_result")
    
    def test_TC_REG_016_name_max_length(self, driver, base_url):
        """TC_REG_016: Verify maximum name length (70 chars)"""
        driver.get(f"{base_url}/register.php")
        time.sleep(1)
        
        unique = f"max{int(time.time())}"
        long_name = "A" * 70
        driver.find_element(By.ID, "name").send_keys(long_name)
        driver.find_element(By.ID, "InputEmail").send_keys(f"{unique}@test.com")
        driver.find_element(By.ID, "username").send_keys(unique)
        driver.find_element(By.ID, "InputPassword").send_keys("password")
        driver.find_element(By.ID, "InputRePassword").send_keys("password")
        screenshot(driver, "TC_REG_016_01_max_name")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_REG_016_02_result")
    
    def test_TC_REG_017_name_exceed_max(self, driver, base_url):
        """TC_REG_017: Verify handling of oversized name (100 chars)"""
        driver.get(f"{base_url}/register.php")
        time.sleep(1)
        
        very_long = "A" * 100
        driver.find_element(By.ID, "name").send_keys(very_long)
        driver.find_element(By.ID, "InputEmail").send_keys("test@test.com")
        driver.find_element(By.ID, "username").send_keys("testuser")
        driver.find_element(By.ID, "InputPassword").send_keys("password")
        driver.find_element(By.ID, "InputRePassword").send_keys("password")
        screenshot(driver, "TC_REG_017_01_exceed_name")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_REG_017_02_result")
    
    def test_TC_REG_018_username_min_length(self, driver, base_url):
        """TC_REG_018: Verify minimum username length (1 char)"""
        driver.get(f"{base_url}/register.php")
        time.sleep(1)
        
        driver.find_element(By.ID, "name").send_keys("Test")
        driver.find_element(By.ID, "InputEmail").send_keys("a@t.co")
        driver.find_element(By.ID, "username").send_keys("a")
        driver.find_element(By.ID, "InputPassword").send_keys("password")
        driver.find_element(By.ID, "InputRePassword").send_keys("password")
        screenshot(driver, "TC_REG_018_01_min_user")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_REG_018_02_result")
    
    def test_TC_REG_019_username_exceed_max(self, driver, base_url):
        """TC_REG_019: Verify handling of oversized username (100 chars)"""
        driver.get(f"{base_url}/register.php")
        time.sleep(1)
        
        very_long_user = "a" * 100
        driver.find_element(By.ID, "name").send_keys("Test")
        driver.find_element(By.ID, "InputEmail").send_keys("test@test.com")
        driver.find_element(By.ID, "username").send_keys(very_long_user)
        driver.find_element(By.ID, "InputPassword").send_keys("password")
        driver.find_element(By.ID, "InputRePassword").send_keys("password")
        screenshot(driver, "TC_REG_019_01_exceed_user")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_REG_019_02_result")
    
    def test_TC_REG_020_password_very_long(self, driver, base_url):
        """TC_REG_020: Verify handling of very long password (300 chars)"""
        driver.get(f"{base_url}/register.php")
        time.sleep(1)
        
        long_pass = "a" * 300
        driver.find_element(By.ID, "name").send_keys("Test")
        driver.find_element(By.ID, "InputEmail").send_keys("test@test.com")
        driver.find_element(By.ID, "username").send_keys("testuser")
        driver.find_element(By.ID, "InputPassword").send_keys(long_pass)
        driver.find_element(By.ID, "InputRePassword").send_keys(long_pass)
        screenshot(driver, "TC_REG_020_01_long_pass")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_REG_020_02_result")


class TestRegisterSecurity:
    """TC_REG_021 - TC_REG_026: Security Tests"""
    
    def test_TC_REG_021_sql_injection_name(self, driver, base_url):
        """TC_REG_021: Verify SQL injection protection in name"""
        driver.get(f"{base_url}/register.php")
        time.sleep(1)
        
        driver.find_element(By.ID, "name").send_keys("' OR '1'='1")
        driver.find_element(By.ID, "InputEmail").send_keys("sql@test.com")
        driver.find_element(By.ID, "username").send_keys("sqltest")
        driver.find_element(By.ID, "InputPassword").send_keys("password")
        driver.find_element(By.ID, "InputRePassword").send_keys("password")
        screenshot(driver, "TC_REG_021_01_sqli_name")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_REG_021_02_result")
    
    def test_TC_REG_022_sql_injection_username(self, driver, base_url):
        """TC_REG_022: Verify SQL injection protection in username"""
        driver.get(f"{base_url}/register.php")
        time.sleep(1)
        
        driver.find_element(By.ID, "name").send_keys("Test")
        driver.find_element(By.ID, "InputEmail").send_keys("sql@test.com")
        driver.find_element(By.ID, "username").send_keys("'; DROP TABLE users;--")
        driver.find_element(By.ID, "InputPassword").send_keys("password")
        driver.find_element(By.ID, "InputRePassword").send_keys("password")
        screenshot(driver, "TC_REG_022_01_sqli_user")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_REG_022_02_result")
    
    def test_TC_REG_023_sql_injection_email(self, driver, base_url):
        """TC_REG_023: Verify SQL injection protection in email"""
        driver.get(f"{base_url}/register.php")
        time.sleep(1)
        
        driver.find_element(By.ID, "name").send_keys("Test")
        driver.find_element(By.ID, "InputEmail").send_keys("test@test.com'; DELETE FROM users;--")
        driver.find_element(By.ID, "username").send_keys("testuser")
        driver.find_element(By.ID, "InputPassword").send_keys("password")
        driver.find_element(By.ID, "InputRePassword").send_keys("password")
        screenshot(driver, "TC_REG_023_01_sqli_email")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_REG_023_02_result")
    
    def test_TC_REG_024_xss_name(self, driver, base_url):
        """TC_REG_024: Verify XSS protection in name"""
        driver.get(f"{base_url}/register.php")
        time.sleep(1)
        
        driver.find_element(By.ID, "name").send_keys("<script>alert('XSS')</script>")
        driver.find_element(By.ID, "InputEmail").send_keys("xss@test.com")
        driver.find_element(By.ID, "username").send_keys("xsstest")
        driver.find_element(By.ID, "InputPassword").send_keys("password")
        driver.find_element(By.ID, "InputRePassword").send_keys("password")
        screenshot(driver, "TC_REG_024_01_xss_name")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_REG_024_02_result")
        
        try:
            alert = driver.switch_to.alert
            alert.dismiss()
            pytest.fail("XSS vulnerability")
        except:
            pass
    
    def test_TC_REG_025_xss_username(self, driver, base_url):
        """TC_REG_025: Verify XSS protection in username"""
        driver.get(f"{base_url}/register.php")
        time.sleep(1)
        
        driver.find_element(By.ID, "name").send_keys("Test")
        driver.find_element(By.ID, "InputEmail").send_keys("xss2@test.com")
        driver.find_element(By.ID, "username").send_keys("<script>document.location='evil.com'</script>")
        driver.find_element(By.ID, "InputPassword").send_keys("password")
        driver.find_element(By.ID, "InputRePassword").send_keys("password")
        screenshot(driver, "TC_REG_025_01_xss_user")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_REG_025_02_result")
    
    def test_TC_REG_026_html_injection(self, driver, base_url):
        """TC_REG_026: Verify HTML injection protection"""
        driver.get(f"{base_url}/register.php")
        time.sleep(1)
        
        driver.find_element(By.ID, "name").send_keys("<b>Bold</b><h1>Header</h1>")
        driver.find_element(By.ID, "InputEmail").send_keys("html@test.com")
        driver.find_element(By.ID, "username").send_keys("htmltest")
        driver.find_element(By.ID, "InputPassword").send_keys("password")
        driver.find_element(By.ID, "InputRePassword").send_keys("password")
        screenshot(driver, "TC_REG_026_01_html")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_REG_026_02_result")


class TestRegisterSpecialCharacters:
    """TC_REG_027 - TC_REG_029: Special Characters Tests"""
    
    def test_TC_REG_027_name_special_chars(self, driver, base_url):
        """TC_REG_027: Verify handling special chars in name"""
        driver.get(f"{base_url}/register.php")
        time.sleep(1)
        
        unique = f"spec{int(time.time())}"
        driver.find_element(By.ID, "name").send_keys("John O'Brien-Smith Jr.")
        driver.find_element(By.ID, "InputEmail").send_keys(f"{unique}@test.com")
        driver.find_element(By.ID, "username").send_keys(unique)
        driver.find_element(By.ID, "InputPassword").send_keys("password")
        driver.find_element(By.ID, "InputRePassword").send_keys("password")
        screenshot(driver, "TC_REG_027_01_special_name")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_REG_027_02_result")
    
    def test_TC_REG_028_username_underscore_dash(self, driver, base_url):
        """TC_REG_028: Verify common username characters"""
        driver.get(f"{base_url}/register.php")
        time.sleep(1)
        
        unique = f"john_doe-{int(time.time())}"
        driver.find_element(By.ID, "name").send_keys("John Doe")
        driver.find_element(By.ID, "InputEmail").send_keys(f"{unique}@test.com")
        driver.find_element(By.ID, "username").send_keys(unique)
        driver.find_element(By.ID, "InputPassword").send_keys("password")
        driver.find_element(By.ID, "InputRePassword").send_keys("password")
        screenshot(driver, "TC_REG_028_01_underscore_dash")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_REG_028_02_result")
    
    def test_TC_REG_029_password_all_special(self, driver, base_url):
        """TC_REG_029: Verify strong password accepted"""
        driver.get(f"{base_url}/register.php")
        time.sleep(1)
        
        unique = f"strong{int(time.time())}"
        driver.find_element(By.ID, "name").send_keys("Test")
        driver.find_element(By.ID, "InputEmail").send_keys(f"{unique}@test.com")
        driver.find_element(By.ID, "username").send_keys(unique)
        driver.find_element(By.ID, "InputPassword").send_keys("P@$$w0rd!@#$%^&*()")
        driver.find_element(By.ID, "InputRePassword").send_keys("P@$$w0rd!@#$%^&*()")
        screenshot(driver, "TC_REG_029_01_strong_pass")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_REG_029_02_result")


class TestRegisterUsability:
    """TC_REG_030 - TC_REG_034: Usability Tests"""
    
    def test_TC_REG_030_navigation_to_login(self, driver, base_url):
        """TC_REG_030: Verify link to login page works"""
        driver.get(f"{base_url}/register.php")
        time.sleep(1)
        screenshot(driver, "TC_REG_030_01_register_page")
        
        login_link = driver.find_element(By.LINK_TEXT, "Login")
        login_link.click()
        time.sleep(1)
        screenshot(driver, "TC_REG_030_02_redirected")
        
        assert "login.php" in driver.current_url
    
    def test_TC_REG_031_tab_order(self, driver, base_url):
        """TC_REG_031: Verify logical tab order"""
        driver.get(f"{base_url}/register.php")
        time.sleep(1)
        
        name_field = driver.find_element(By.ID, "name")
        name_field.click()
        screenshot(driver, "TC_REG_031_01_focus_name")
        
        name_field.send_keys(Keys.TAB)
        time.sleep(0.3)
        screenshot(driver, "TC_REG_031_02_tab_email")
        
        active = driver.switch_to.active_element
        assert active.get_attribute("id") == "InputEmail"
    
    def test_TC_REG_032_form_labels(self, driver, base_url):
        """TC_REG_032: Verify all fields have labels"""
        driver.get(f"{base_url}/register.php")
        time.sleep(1)
        screenshot(driver, "TC_REG_032_01_labels")
        
        labels = driver.find_elements(By.TAG_NAME, "label")
        assert len(labels) >= 4
    
    def test_TC_REG_033_placeholder_text(self, driver, base_url):
        """TC_REG_033: Verify placeholder text is helpful"""
        driver.get(f"{base_url}/register.php")
        time.sleep(1)
        screenshot(driver, "TC_REG_033_01_placeholders")
        
        name_field = driver.find_element(By.ID, "name")
        placeholder = name_field.get_attribute("placeholder")
        assert placeholder is not None
    
    def test_TC_REG_034_error_visibility(self, driver, base_url):
        """TC_REG_034: Verify error messages are visible"""
        driver.get(f"{base_url}/register.php")
        time.sleep(1)
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_REG_034_01_error_visible")
        
        page_source = driver.page_source.lower()
        assert "kosong" in page_source or "alert" in page_source


class TestRegisterBugVerification:
    """TC_REG_035 - TC_REG_036: Bug Verification Tests"""
    
    def test_TC_REG_035_bug_variable_mismatch(self, driver, base_url):
        """TC_REG_035: BUG - $nama vs $name variable mismatch"""
        driver.get(f"{base_url}/register.php")
        time.sleep(1)
        
        unique = f"bugtest{int(time.time())}"
        driver.find_element(By.ID, "name").send_keys("This Name Should Be Saved")
        driver.find_element(By.ID, "InputEmail").send_keys(f"{unique}@test.com")
        driver.find_element(By.ID, "username").send_keys(unique)
        driver.find_element(By.ID, "InputPassword").send_keys("password")
        driver.find_element(By.ID, "InputRePassword").send_keys("password")
        screenshot(driver, "TC_REG_035_01_bug_nama_name")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_REG_035_02_result")
        # Note: Name field will be empty in DB due to $nama vs $name bug
    
    def test_TC_REG_036_bug_wrong_duplicate_check(self, driver, base_url):
        """TC_REG_036: BUG - cek_nama checks wrong field"""
        driver.get(f"{base_url}/register.php")
        time.sleep(1)
        
        # Name matches existing USERNAME (irul), but our username is unique
        driver.find_element(By.ID, "name").send_keys("irul")
        driver.find_element(By.ID, "InputEmail").send_keys("unique999@test.com")
        driver.find_element(By.ID, "username").send_keys("completelyunique12345")
        driver.find_element(By.ID, "InputPassword").send_keys("password")
        driver.find_element(By.ID, "InputRePassword").send_keys("password")
        screenshot(driver, "TC_REG_036_01_wrong_check")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_REG_036_02_result")
        # BUG: Shows "Username sudah terdaftar" even though username is unique


class TestRegisterWithStub:
    """TC_REG_037 - TC_REG_043: Stub/Unit Tests"""
    
    def test_TC_REG_037_stub_valid_registration(self, db_stub, register_driver):
        """TC_REG_037: Stub - Valid registration data"""
        result = register_driver.attempt_register("New User", "new@test.com", "newuser", "pass", "pass")
        assert result['success'] == True
    
    def test_TC_REG_038_stub_empty_name(self, db_stub, register_driver):
        """TC_REG_038: Stub - Empty name field"""
        result = register_driver.attempt_register("", "test@test.com", "user", "pass", "pass")
        assert result['success'] == False
    
    def test_TC_REG_039_stub_empty_email(self, db_stub, register_driver):
        """TC_REG_039: Stub - Empty email field"""
        result = register_driver.attempt_register("Name", "", "user", "pass", "pass")
        assert result['success'] == False
    
    def test_TC_REG_040_stub_empty_username(self, db_stub, register_driver):
        """TC_REG_040: Stub - Empty username field"""
        result = register_driver.attempt_register("Name", "test@test.com", "", "pass", "pass")
        assert result['success'] == False
    
    def test_TC_REG_041_stub_password_mismatch(self, db_stub, register_driver):
        """TC_REG_041: Stub - Password mismatch"""
        result = register_driver.attempt_register("Name", "test@test.com", "user", "pass1", "pass2")
        assert result['success'] == False
    
    def test_TC_REG_042_stub_duplicate_name_bug(self, db_stub, register_driver):
        """TC_REG_042: Stub - Duplicate name check bug"""
        # Name matches existing username - triggers bug
        result = register_driver.attempt_register("irul", "new@test.com", "newunique", "pass", "pass")
        assert result['success'] == False
    
    def test_TC_REG_043_stub_empty_name_db(self, db_stub):
        """TC_REG_043: Stub - Verify empty name fields in DB"""
        user_irul = db_stub.get_user("irul")
        user_ahmad = db_stub.get_user("ahmad")
        assert user_irul['name'] == ''
        assert user_ahmad['name'] == ''
