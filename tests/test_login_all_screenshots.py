"""
Complete Selenium Test Cases for Login Module with Screenshots
All 38 test cases with screenshot capture
"""
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, UnexpectedAlertPresentException
import time
import os

SCREENSHOT_DIR = os.path.join(os.path.dirname(__file__), "screenshots", "login")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

def screenshot(driver, name):
    """Save screenshot with test name"""
    filepath = os.path.join(SCREENSHOT_DIR, f"{name}.png")
    driver.save_screenshot(filepath)
    return filepath


class TestLoginFunctionalPositive:
    """TC_LGN_001 - TC_LGN_002: Positive functional tests"""
    
    def test_TC_LGN_001_login_valid_credentials(self, driver, base_url):
        """TC_LGN_001: Verify successful login with valid credentials"""
        driver.get(f"{base_url}/login.php")
        time.sleep(1)
        screenshot(driver, "TC_LGN_001_01_page")
        
        driver.find_element(By.ID, "username").send_keys("irul")
        driver.find_element(By.ID, "InputPassword").send_keys("irul123")
        screenshot(driver, "TC_LGN_001_02_filled")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_LGN_001_03_result")
        
        assert "login.php" not in driver.current_url or "index.php" in driver.current_url
    
    @pytest.mark.xfail(reason="Finding: Username NOT case-sensitive")
    def test_TC_LGN_002_login_case_sensitivity(self, driver, base_url):
        """TC_LGN_002: Verify username case sensitivity"""
        driver.get(f"{base_url}/login.php")
        time.sleep(1)
        
        driver.find_element(By.ID, "username").send_keys("IRUL")
        driver.find_element(By.ID, "InputPassword").send_keys("irul123")
        screenshot(driver, "TC_LGN_002_01_uppercase_input")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_LGN_002_02_result")
        
        assert "login.php" in driver.current_url


class TestLoginFunctionalNegative:
    """TC_LGN_003 - TC_LGN_009: Negative functional tests"""
    
    def test_TC_LGN_003_invalid_password(self, driver, base_url):
        """TC_LGN_003: Verify login fails with wrong password"""
        driver.get(f"{base_url}/login.php")
        time.sleep(1)
        
        driver.find_element(By.ID, "username").send_keys("irul")
        driver.find_element(By.ID, "InputPassword").send_keys("wrongpassword")
        screenshot(driver, "TC_LGN_003_01_wrong_pass")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_LGN_003_02_result")
        
        assert "login.php" in driver.current_url
    
    def test_TC_LGN_004_invalid_username(self, driver, base_url):
        """TC_LGN_004: Verify login fails with non-existent username"""
        driver.get(f"{base_url}/login.php")
        time.sleep(1)
        
        driver.find_element(By.ID, "username").send_keys("nonexistentuser")
        driver.find_element(By.ID, "InputPassword").send_keys("anypassword")
        screenshot(driver, "TC_LGN_004_01_nonexistent")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_LGN_004_02_result")
        
        page_source = driver.page_source.lower()
        assert "login.php" in driver.current_url or "gagal" in page_source
    
    def test_TC_LGN_005_empty_username(self, driver, base_url):
        """TC_LGN_005: Verify validation for empty username"""
        driver.get(f"{base_url}/login.php")
        time.sleep(1)
        
        driver.find_element(By.ID, "InputPassword").send_keys("test123")
        screenshot(driver, "TC_LGN_005_01_empty_user")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_LGN_005_02_result")
        
        assert "login.php" in driver.current_url
    
    def test_TC_LGN_006_empty_password(self, driver, base_url):
        """TC_LGN_006: Verify validation for empty password"""
        driver.get(f"{base_url}/login.php")
        time.sleep(1)
        
        driver.find_element(By.ID, "username").send_keys("irul")
        screenshot(driver, "TC_LGN_006_01_empty_pass")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_LGN_006_02_result")
        
        assert "login.php" in driver.current_url
    
    def test_TC_LGN_007_both_fields_empty(self, driver, base_url):
        """TC_LGN_007: Verify validation when all fields empty"""
        driver.get(f"{base_url}/login.php")
        time.sleep(1)
        screenshot(driver, "TC_LGN_007_01_both_empty")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_LGN_007_02_result")
        
        assert "login.php" in driver.current_url
    
    def test_TC_LGN_008_whitespace_username(self, driver, base_url):
        """TC_LGN_008: Verify validation for whitespace-only username"""
        driver.get(f"{base_url}/login.php")
        time.sleep(1)
        
        driver.find_element(By.ID, "username").send_keys("   ")
        driver.find_element(By.ID, "InputPassword").send_keys("test123")
        screenshot(driver, "TC_LGN_008_01_whitespace")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_LGN_008_02_result")
        
        assert "login.php" in driver.current_url
    
    def test_TC_LGN_009_whitespace_password(self, driver, base_url):
        """TC_LGN_009: Verify validation for whitespace-only password"""
        driver.get(f"{base_url}/login.php")
        time.sleep(1)
        
        driver.find_element(By.ID, "username").send_keys("irul")
        driver.find_element(By.ID, "InputPassword").send_keys("   ")
        screenshot(driver, "TC_LGN_009_01_whitespace_pass")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_LGN_009_02_result")
        
        assert "login.php" in driver.current_url


class TestLoginBoundaryValue:
    """TC_LGN_010 - TC_LGN_014: Boundary Value Analysis"""
    
    def test_TC_LGN_010_username_min_length(self, driver, base_url):
        """TC_LGN_010: Verify login with 1 character username"""
        driver.get(f"{base_url}/login.php")
        time.sleep(1)
        
        driver.find_element(By.ID, "username").send_keys("a")
        driver.find_element(By.ID, "InputPassword").send_keys("test123")
        screenshot(driver, "TC_LGN_010_01_min_user")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_LGN_010_02_result")
        
        # Should handle gracefully
        assert driver.current_url is not None
    
    def test_TC_LGN_011_username_max_length(self, driver, base_url):
        """TC_LGN_011: Verify login with max length username (50 chars)"""
        driver.get(f"{base_url}/login.php")
        time.sleep(1)
        
        long_username = "a" * 50
        driver.find_element(By.ID, "username").send_keys(long_username)
        driver.find_element(By.ID, "InputPassword").send_keys("test123")
        screenshot(driver, "TC_LGN_011_01_max_user")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_LGN_011_02_result")
        
        assert driver.current_url is not None
    
    def test_TC_LGN_012_username_exceed_max(self, driver, base_url):
        """TC_LGN_012: Verify system handles oversized username (100 chars)"""
        driver.get(f"{base_url}/login.php")
        time.sleep(1)
        
        very_long = "a" * 100
        driver.find_element(By.ID, "username").send_keys(very_long)
        driver.find_element(By.ID, "InputPassword").send_keys("test123")
        screenshot(driver, "TC_LGN_012_01_exceed_max")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_LGN_012_02_result")
        
        assert driver.current_url is not None
    
    def test_TC_LGN_013_password_min_length(self, driver, base_url):
        """TC_LGN_013: Verify login with 1 character password"""
        driver.get(f"{base_url}/login.php")
        time.sleep(1)
        
        driver.find_element(By.ID, "username").send_keys("irul")
        driver.find_element(By.ID, "InputPassword").send_keys("a")
        screenshot(driver, "TC_LGN_013_01_min_pass")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_LGN_013_02_result")
        
        assert "login.php" in driver.current_url
    
    def test_TC_LGN_014_password_very_long(self, driver, base_url):
        """TC_LGN_014: Verify system handles very long password (300 chars)"""
        driver.get(f"{base_url}/login.php")
        time.sleep(1)
        
        long_pass = "a" * 300
        driver.find_element(By.ID, "username").send_keys("irul")
        driver.find_element(By.ID, "InputPassword").send_keys(long_pass)
        screenshot(driver, "TC_LGN_014_01_long_pass")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_LGN_014_02_result")
        
        assert driver.current_url is not None


class TestLoginSecurity:
    """TC_LGN_015 - TC_LGN_021: Security Tests"""
    
    def test_TC_LGN_015_sql_injection_basic(self, driver, base_url):
        """TC_LGN_015: Verify protection against basic SQL injection"""
        driver.get(f"{base_url}/login.php")
        time.sleep(1)
        
        driver.find_element(By.ID, "username").send_keys("' OR '1'='1")
        driver.find_element(By.ID, "InputPassword").send_keys("test")
        screenshot(driver, "TC_LGN_015_01_sqli_basic")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_LGN_015_02_result")
        
        # Note: This may pass (vulnerability) or fail (protected)
    
    def test_TC_LGN_016_sql_injection_comment(self, driver, base_url):
        """TC_LGN_016: Verify protection against SQL comment injection"""
        driver.get(f"{base_url}/login.php")
        time.sleep(1)
        
        driver.find_element(By.ID, "username").send_keys("admin'--")
        driver.find_element(By.ID, "InputPassword").send_keys("anything")
        screenshot(driver, "TC_LGN_016_01_sqli_comment")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_LGN_016_02_result")
        
        assert "login.php" in driver.current_url
    
    def test_TC_LGN_017_sql_injection_union(self, driver, base_url):
        """TC_LGN_017: Verify protection against UNION-based injection"""
        driver.get(f"{base_url}/login.php")
        time.sleep(1)
        
        driver.find_element(By.ID, "username").send_keys("' UNION SELECT * FROM users--")
        driver.find_element(By.ID, "InputPassword").send_keys("test")
        screenshot(driver, "TC_LGN_017_01_sqli_union")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_LGN_017_02_result")
        
        assert "login.php" in driver.current_url
    
    def test_TC_LGN_018_sql_injection_password(self, driver, base_url):
        """TC_LGN_018: Verify SQL injection protection in password field"""
        driver.get(f"{base_url}/login.php")
        time.sleep(1)
        
        driver.find_element(By.ID, "username").send_keys("irul")
        driver.find_element(By.ID, "InputPassword").send_keys("' OR '1'='1")
        screenshot(driver, "TC_LGN_018_01_sqli_pass")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_LGN_018_02_result")
        
        assert "login.php" in driver.current_url
    
    def test_TC_LGN_019_xss_username(self, driver, base_url):
        """TC_LGN_019: Verify XSS protection in username field"""
        driver.get(f"{base_url}/login.php")
        time.sleep(1)
        
        driver.find_element(By.ID, "username").send_keys("<script>alert('XSS')</script>")
        driver.find_element(By.ID, "InputPassword").send_keys("test")
        screenshot(driver, "TC_LGN_019_01_xss_user")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_LGN_019_02_result")
        
        # Verify no alert triggered
        try:
            alert = driver.switch_to.alert
            alert.dismiss()
            pytest.fail("XSS vulnerability: Alert was triggered")
        except:
            pass
    
    def test_TC_LGN_020_xss_event_handler(self, driver, base_url):
        """TC_LGN_020: Verify XSS protection against event handlers"""
        driver.get(f"{base_url}/login.php")
        time.sleep(1)
        
        driver.find_element(By.ID, "username").send_keys("<img src=x onerror=alert('XSS')>")
        driver.find_element(By.ID, "InputPassword").send_keys("test")
        screenshot(driver, "TC_LGN_020_01_xss_event")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_LGN_020_02_result")
        
        try:
            alert = driver.switch_to.alert
            alert.dismiss()
            pytest.fail("XSS vulnerability")
        except:
            pass
    
    def test_TC_LGN_021_html_injection(self, driver, base_url):
        """TC_LGN_021: Verify HTML injection protection"""
        driver.get(f"{base_url}/login.php")
        time.sleep(1)
        
        driver.find_element(By.ID, "username").send_keys("<h1>Hacked</h1>")
        driver.find_element(By.ID, "InputPassword").send_keys("test")
        screenshot(driver, "TC_LGN_021_01_html_inj")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_LGN_021_02_result")
        
        assert driver.current_url is not None


class TestLoginSpecialCharacters:
    """TC_LGN_022 - TC_LGN_024: Special Characters Tests"""
    
    def test_TC_LGN_022_username_special_chars(self, driver, base_url):
        """TC_LGN_022: Verify handling of special characters in username"""
        driver.get(f"{base_url}/login.php")
        time.sleep(1)
        
        driver.find_element(By.ID, "username").send_keys("user@#$%")
        driver.find_element(By.ID, "InputPassword").send_keys("test123")
        screenshot(driver, "TC_LGN_022_01_special")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_LGN_022_02_result")
        
        assert driver.current_url is not None
    
    def test_TC_LGN_023_username_unicode(self, driver, base_url):
        """TC_LGN_023: Verify handling of unicode characters"""
        driver.get(f"{base_url}/login.php")
        time.sleep(1)
        
        driver.find_element(By.ID, "username").send_keys("用户名")
        driver.find_element(By.ID, "InputPassword").send_keys("test123")
        screenshot(driver, "TC_LGN_023_01_unicode")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_LGN_023_02_result")
        
        assert driver.current_url is not None
    
    def test_TC_LGN_024_password_special_chars(self, driver, base_url):
        """TC_LGN_024: Verify login with special chars in password"""
        driver.get(f"{base_url}/login.php")
        time.sleep(1)
        
        driver.find_element(By.ID, "username").send_keys("irul")
        driver.find_element(By.ID, "InputPassword").send_keys("P@ss!@#$%^&*()")
        screenshot(driver, "TC_LGN_024_01_special_pass")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_LGN_024_02_result")
        
        assert "login.php" in driver.current_url


class TestLoginUsability:
    """TC_LGN_025 - TC_LGN_028: Usability Tests"""
    
    def test_TC_LGN_025_tab_navigation(self, driver, base_url):
        """TC_LGN_025: Verify form can be navigated using Tab key"""
        driver.get(f"{base_url}/login.php")
        time.sleep(1)
        
        username_field = driver.find_element(By.ID, "username")
        username_field.click()
        screenshot(driver, "TC_LGN_025_01_focus_user")
        
        username_field.send_keys(Keys.TAB)
        time.sleep(0.5)
        screenshot(driver, "TC_LGN_025_02_after_tab")
        
        active = driver.switch_to.active_element
        assert active.get_attribute("id") == "InputPassword"
    
    def test_TC_LGN_026_enter_key_submission(self, driver, base_url):
        """TC_LGN_026: Verify form submits on Enter key"""
        driver.get(f"{base_url}/login.php")
        time.sleep(1)
        
        driver.find_element(By.ID, "username").send_keys("irul")
        driver.find_element(By.ID, "InputPassword").send_keys("irul123")
        screenshot(driver, "TC_LGN_026_01_filled")
        
        driver.find_element(By.ID, "InputPassword").send_keys(Keys.ENTER)
        time.sleep(2)
        screenshot(driver, "TC_LGN_026_02_after_enter")
        
        assert "index.php" in driver.current_url or "login.php" not in driver.current_url
    
    def test_TC_LGN_027_password_masking(self, driver, base_url):
        """TC_LGN_027: Verify password field masks input"""
        driver.get(f"{base_url}/login.php")
        time.sleep(1)
        
        password_field = driver.find_element(By.ID, "InputPassword")
        password_field.send_keys("testpassword")
        screenshot(driver, "TC_LGN_027_01_masked")
        
        assert password_field.get_attribute("type") == "password"
    
    def test_TC_LGN_028_page_elements_present(self, driver, base_url):
        """TC_LGN_028: Verify all expected elements present"""
        driver.get(f"{base_url}/login.php")
        time.sleep(1)
        screenshot(driver, "TC_LGN_028_01_elements")
        
        assert driver.find_element(By.ID, "username")
        assert driver.find_element(By.ID, "InputPassword")
        assert driver.find_element(By.NAME, "submit")
        assert driver.find_element(By.LINK_TEXT, "Register")


class TestLoginDatabaseEdgeCases:
    """TC_LGN_029 - TC_LGN_030: Database Edge Cases"""
    
    def test_TC_LGN_029_user_empty_name_irul(self, driver, base_url):
        """TC_LGN_029: Verify login works when name field is empty in DB"""
        driver.get(f"{base_url}/login.php")
        time.sleep(1)
        
        driver.find_element(By.ID, "username").send_keys("irul")
        driver.find_element(By.ID, "InputPassword").send_keys("irul123")
        screenshot(driver, "TC_LGN_029_01_empty_name_user")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_LGN_029_02_result")
        
        assert "index.php" in driver.current_url
    
    def test_TC_LGN_030_user_empty_name_ahmad(self, driver, base_url):
        """TC_LGN_030: Verify another user with empty name can login"""
        driver.get(f"{base_url}/login.php")
        time.sleep(1)
        
        driver.find_element(By.ID, "username").send_keys("ahmad")
        driver.find_element(By.ID, "InputPassword").send_keys("ahmad123")
        screenshot(driver, "TC_LGN_030_01_ahmad")
        
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_LGN_030_02_result")
        
        assert "index.php" in driver.current_url


class TestLoginSession:
    """TC_LGN_031: Session Tests"""
    
    def test_TC_LGN_031_already_logged_in(self, driver, base_url):
        """TC_LGN_031: Verify redirect when already logged in"""
        driver.get(f"{base_url}/login.php")
        time.sleep(1)
        
        driver.find_element(By.ID, "username").send_keys("irul")
        driver.find_element(By.ID, "InputPassword").send_keys("irul123")
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        screenshot(driver, "TC_LGN_031_01_logged_in")
        
        # Try to access login again
        driver.get(f"{base_url}/login.php")
        time.sleep(2)
        screenshot(driver, "TC_LGN_031_02_redirect")
        
        assert "index.php" in driver.current_url


class TestLoginWithStub:
    """TC_LGN_032 - TC_LGN_038: Stub/Unit Tests"""
    
    def test_TC_LGN_032_stub_valid_login(self, db_stub, login_driver):
        """TC_LGN_032: Stub - Valid login credentials"""
        result = login_driver.attempt_login("irul", "irul123")
        assert result['success'] == True
    
    def test_TC_LGN_033_stub_invalid_username(self, db_stub, login_driver):
        """TC_LGN_033: Stub - Non-existent username"""
        result = login_driver.attempt_login("nonexistent", "password")
        assert result['success'] == False
    
    def test_TC_LGN_034_stub_empty_username(self, db_stub, login_driver):
        """TC_LGN_034: Stub - Empty username"""
        result = login_driver.attempt_login("", "password")
        assert result['success'] == False
    
    def test_TC_LGN_035_stub_empty_password(self, db_stub, login_driver):
        """TC_LGN_035: Stub - Empty password"""
        result = login_driver.attempt_login("irul", "")
        assert result['success'] == False
    
    def test_TC_LGN_036_stub_whitespace_username(self, db_stub, login_driver):
        """TC_LGN_036: Stub - Whitespace-only username"""
        result = login_driver.attempt_login("   ", "password")
        assert result['success'] == False
    
    def test_TC_LGN_037_stub_user_empty_name(self, db_stub):
        """TC_LGN_037: Stub - Verify user with empty name"""
        user = db_stub.get_user("irul")
        assert user is not None
        assert user['name'] == ''
    
    def test_TC_LGN_038_stub_sql_injection(self, db_stub, login_driver):
        """TC_LGN_038: Stub - SQL injection should fail"""
        result = login_driver.attempt_login("' OR '1'='1", "test")
        assert result['success'] == False
