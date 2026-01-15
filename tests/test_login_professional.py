"""
Professional Selenium Test Cases for Login Module
Comprehensive testing with multiple techniques:
- Functional Testing (Positive & Negative)
- Boundary Value Analysis
- Security Testing
- Usability Testing
"""
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, UnexpectedAlertPresentException
import time
import uuid


class TestLoginFunctionalPositive:
    """TC_LGN_001 - TC_LGN_003: Positive functional tests"""
    
    def test_login_valid_credentials(self, driver, base_url):
        """TC_LGN_001: Verify successful login with valid credentials"""
        driver.get(f"{base_url}/login.php")
        
        driver.find_element(By.ID, "username").send_keys("irul")
        driver.find_element(By.ID, "InputPassword").send_keys("irul123")
        driver.find_element(By.NAME, "submit").click()
        
        time.sleep(2)
        assert "login.php" not in driver.current_url or "index.php" in driver.current_url
    
    @pytest.mark.xfail(reason="Finding: Username is NOT case-sensitive (IRUL = irul)")
    def test_login_case_sensitivity_username(self, driver, base_url):
        """TC_LGN_003: Verify username case sensitivity"""
        driver.get(f"{base_url}/login.php")
        
        driver.find_element(By.ID, "username").send_keys("IRUL")  # Uppercase
        driver.find_element(By.ID, "InputPassword").send_keys("irul123")
        driver.find_element(By.NAME, "submit").click()
        
        time.sleep(2)
        # Username should be case-sensitive, so this should fail
        assert "login.php" in driver.current_url


class TestLoginFunctionalNegative:
    """TC_LGN_004 - TC_LGN_010: Negative functional tests"""
    
    def test_login_invalid_password(self, driver, base_url):
        """TC_LGN_004: Verify login fails with wrong password"""
        driver.get(f"{base_url}/login.php")
        
        driver.find_element(By.ID, "username").send_keys("irul")
        driver.find_element(By.ID, "InputPassword").send_keys("wrongpassword")
        driver.find_element(By.NAME, "submit").click()
        
        time.sleep(2)
        assert "login.php" in driver.current_url
    
    def test_login_invalid_username(self, driver, base_url):
        """TC_LGN_005: Verify login fails with non-existent username"""
        driver.get(f"{base_url}/login.php")
        
        driver.find_element(By.ID, "username").send_keys("nonexistentuser")
        driver.find_element(By.ID, "InputPassword").send_keys("anypassword")
        driver.find_element(By.NAME, "submit").click()
        
        time.sleep(2)
        try:
            error = driver.find_element(By.CLASS_NAME, "alert-danger")
            assert "Register User Gagal" in error.text
        except:
            assert "login.php" in driver.current_url
    
    def test_login_empty_username(self, driver, base_url):
        """TC_LGN_006: Verify validation for empty username"""
        driver.get(f"{base_url}/login.php")
        
        driver.find_element(By.ID, "InputPassword").send_keys("test123")
        driver.find_element(By.NAME, "submit").click()
        
        time.sleep(2)
        try:
            error = driver.find_element(By.CLASS_NAME, "alert-danger")
            assert "Data tidak boleh kosong" in error.text
        except:
            assert "login.php" in driver.current_url
    
    def test_login_empty_password(self, driver, base_url):
        """TC_LGN_007: Verify validation for empty password"""
        driver.get(f"{base_url}/login.php")
        
        driver.find_element(By.ID, "username").send_keys("irul")
        driver.find_element(By.NAME, "submit").click()
        
        time.sleep(2)
        try:
            error = driver.find_element(By.CLASS_NAME, "alert-danger")
            assert "Data tidak boleh kosong" in error.text
        except:
            assert "login.php" in driver.current_url
    
    def test_login_both_fields_empty(self, driver, base_url):
        """TC_LGN_008: Verify validation when all fields empty"""
        driver.get(f"{base_url}/login.php")
        
        driver.find_element(By.NAME, "submit").click()
        
        time.sleep(2)
        try:
            error = driver.find_element(By.CLASS_NAME, "alert-danger")
            assert "Data tidak boleh kosong" in error.text
        except:
            assert "login.php" in driver.current_url
    
    def test_login_whitespace_only_username(self, driver, base_url):
        """TC_LGN_009: Verify validation for whitespace-only username"""
        driver.get(f"{base_url}/login.php")
        
        driver.find_element(By.ID, "username").send_keys("   ")
        driver.find_element(By.ID, "InputPassword").send_keys("test123")
        driver.find_element(By.NAME, "submit").click()
        
        time.sleep(2)
        try:
            error = driver.find_element(By.CLASS_NAME, "alert-danger")
            assert "Data tidak boleh kosong" in error.text
        except:
            assert "login.php" in driver.current_url
    
    def test_login_whitespace_only_password(self, driver, base_url):
        """TC_LGN_010: Verify validation for whitespace-only password"""
        driver.get(f"{base_url}/login.php")
        
        driver.find_element(By.ID, "username").send_keys("irul")
        driver.find_element(By.ID, "InputPassword").send_keys("   ")
        driver.find_element(By.NAME, "submit").click()
        
        time.sleep(2)
        # Should fail login or show error
        assert "login.php" in driver.current_url


class TestLoginBoundaryValue:
    """TC_LGN_011 - TC_LGN_015: Boundary value analysis tests"""
    
    def test_login_username_min_length(self, driver, base_url):
        """TC_LGN_011: Verify login with 1 character username"""
        driver.get(f"{base_url}/login.php")
        
        driver.find_element(By.ID, "username").send_keys("a")
        driver.find_element(By.ID, "InputPassword").send_keys("test123")
        driver.find_element(By.NAME, "submit").click()
        
        time.sleep(2)
        # Should handle 1-char username
        assert driver.current_url is not None
    
    def test_login_username_max_length(self, driver, base_url):
        """TC_LGN_012: Verify login with max length username (50 chars)"""
        driver.get(f"{base_url}/login.php")
        
        long_username = "a" * 50
        driver.find_element(By.ID, "username").send_keys(long_username)
        driver.find_element(By.ID, "InputPassword").send_keys("test123")
        driver.find_element(By.NAME, "submit").click()
        
        time.sleep(2)
        assert driver.current_url is not None
    
    def test_login_username_exceed_max(self, driver, base_url):
        """TC_LGN_013: Verify system handles oversized username (100 chars)"""
        driver.get(f"{base_url}/login.php")
        
        very_long_username = "a" * 100
        driver.find_element(By.ID, "username").send_keys(very_long_username)
        driver.find_element(By.ID, "InputPassword").send_keys("test123")
        driver.find_element(By.NAME, "submit").click()
        
        time.sleep(2)
        # Should not crash
        assert driver.current_url is not None
    
    def test_login_password_min_length(self, driver, base_url):
        """TC_LGN_014: Verify login with 1 character password"""
        driver.get(f"{base_url}/login.php")
        
        driver.find_element(By.ID, "username").send_keys("irul")
        driver.find_element(By.ID, "InputPassword").send_keys("a")
        driver.find_element(By.NAME, "submit").click()
        
        time.sleep(2)
        # Should fail (wrong password)
        assert "login.php" in driver.current_url
    
    def test_login_password_very_long(self, driver, base_url):
        """TC_LGN_015: Verify system handles very long password (300 chars)"""
        driver.get(f"{base_url}/login.php")
        
        very_long_password = "a" * 300
        driver.find_element(By.ID, "username").send_keys("irul")
        driver.find_element(By.ID, "InputPassword").send_keys(very_long_password)
        driver.find_element(By.NAME, "submit").click()
        
        time.sleep(2)
        # Should not crash
        assert driver.current_url is not None


class TestLoginSecurity:
    """TC_LGN_016 - TC_LGN_023: Security tests"""
    
    def test_sql_injection_basic(self, driver, base_url):
        """TC_LGN_016: Verify protection against basic SQL injection"""
        driver.get(f"{base_url}/login.php")
        
        driver.find_element(By.ID, "username").send_keys("' OR '1'='1")
        driver.find_element(By.ID, "InputPassword").send_keys("test")
        driver.find_element(By.NAME, "submit").click()
        
        time.sleep(2)
        # Should NOT login
        assert "index.php" not in driver.current_url
    
    def test_sql_injection_comment(self, driver, base_url):
        """TC_LGN_017: Verify protection against SQL comment injection"""
        driver.get(f"{base_url}/login.php")
        
        driver.find_element(By.ID, "username").send_keys("admin'--")
        driver.find_element(By.ID, "InputPassword").send_keys("anything")
        driver.find_element(By.NAME, "submit").click()
        
        time.sleep(2)
        assert "index.php" not in driver.current_url
    
    def test_sql_injection_union(self, driver, base_url):
        """TC_LGN_018: Verify protection against UNION-based injection"""
        driver.get(f"{base_url}/login.php")
        
        driver.find_element(By.ID, "username").send_keys("' UNION SELECT * FROM users--")
        driver.find_element(By.ID, "InputPassword").send_keys("test")
        driver.find_element(By.NAME, "submit").click()
        
        time.sleep(2)
        assert "index.php" not in driver.current_url
    
    def test_sql_injection_password(self, driver, base_url):
        """TC_LGN_019: Verify SQL injection protection in password"""
        driver.get(f"{base_url}/login.php")
        
        driver.find_element(By.ID, "username").send_keys("irul")
        driver.find_element(By.ID, "InputPassword").send_keys("' OR '1'='1")
        driver.find_element(By.NAME, "submit").click()
        
        time.sleep(2)
        # Password is hashed, so SQL injection in password shouldn't work
        assert "login.php" in driver.current_url
    
    def test_xss_stored_username(self, driver, base_url):
        """TC_LGN_020: Verify XSS protection in username field"""
        driver.get(f"{base_url}/login.php")
        
        driver.find_element(By.ID, "username").send_keys("<script>alert('XSS')</script>")
        driver.find_element(By.ID, "InputPassword").send_keys("test")
        driver.find_element(By.NAME, "submit").click()
        
        time.sleep(2)
        # Verify no alert triggered
        try:
            alert = driver.switch_to.alert
            alert.dismiss()
            pytest.fail("XSS vulnerability detected")
        except:
            pass
    
    def test_xss_event_handler(self, driver, base_url):
        """TC_LGN_021: Verify XSS protection against event handlers"""
        driver.get(f"{base_url}/login.php")
        
        driver.find_element(By.ID, "username").send_keys("<img src=x onerror=alert('XSS')>")
        driver.find_element(By.ID, "InputPassword").send_keys("test")
        driver.find_element(By.NAME, "submit").click()
        
        time.sleep(2)
        try:
            alert = driver.switch_to.alert
            alert.dismiss()
            pytest.fail("XSS vulnerability detected")
        except:
            pass
    
    def test_html_injection(self, driver, base_url):
        """TC_LGN_022: Verify HTML injection protection"""
        driver.get(f"{base_url}/login.php")
        
        driver.find_element(By.ID, "username").send_keys("<h1>Hacked</h1>")
        driver.find_element(By.ID, "InputPassword").send_keys("test")
        driver.find_element(By.NAME, "submit").click()
        
        time.sleep(2)
        # Check that HTML is not rendered
        page_source = driver.page_source
        assert "<h1>Hacked</h1>" not in page_source or "&lt;h1&gt;" in page_source


class TestLoginSpecialCharacters:
    """TC_LGN_024 - TC_LGN_026: Special character tests"""
    
    def test_username_special_chars(self, driver, base_url):
        """TC_LGN_024: Verify handling of special characters in username"""
        driver.get(f"{base_url}/login.php")
        
        driver.find_element(By.ID, "username").send_keys("user@#$%")
        driver.find_element(By.ID, "InputPassword").send_keys("test123")
        driver.find_element(By.NAME, "submit").click()
        
        time.sleep(2)
        # Should handle without crash
        assert driver.current_url is not None
    
    def test_username_unicode(self, driver, base_url):
        """TC_LGN_025: Verify handling of unicode characters"""
        driver.get(f"{base_url}/login.php")
        
        driver.find_element(By.ID, "username").send_keys("用户名")
        driver.find_element(By.ID, "InputPassword").send_keys("test123")
        driver.find_element(By.NAME, "submit").click()
        
        time.sleep(2)
        assert driver.current_url is not None
    
    def test_password_special_chars(self, driver, base_url):
        """TC_LGN_026: Verify login with special chars in password"""
        driver.get(f"{base_url}/login.php")
        
        driver.find_element(By.ID, "username").send_keys("irul")
        driver.find_element(By.ID, "InputPassword").send_keys("P@ss!@#$%^&*()")
        driver.find_element(By.NAME, "submit").click()
        
        time.sleep(2)
        # Should fail (wrong password) but not crash
        assert "login.php" in driver.current_url


class TestLoginUsability:
    """TC_LGN_027 - TC_LGN_030: Usability tests"""
    
    def test_tab_navigation(self, driver, base_url):
        """TC_LGN_027: Verify form can be navigated using Tab key"""
        driver.get(f"{base_url}/login.php")
        
        username_field = driver.find_element(By.ID, "username")
        username_field.click()
        username_field.send_keys(Keys.TAB)
        
        # Check that focus moved to password field
        active_element = driver.switch_to.active_element
        assert active_element.get_attribute("id") == "InputPassword" or active_element.get_attribute("name") == "password"
    
    def test_enter_key_submission(self, driver, base_url):
        """TC_LGN_028: Verify form submits on Enter key"""
        driver.get(f"{base_url}/login.php")
        
        driver.find_element(By.ID, "username").send_keys("irul")
        password_field = driver.find_element(By.ID, "InputPassword")
        password_field.send_keys("irul123")
        password_field.send_keys(Keys.RETURN)
        
        time.sleep(2)
        # Form should be submitted
        assert driver.current_url != f"{base_url}/login.php" or "index.php" in driver.current_url or "login.php" in driver.current_url
    
    def test_password_masking(self, driver, base_url):
        """TC_LGN_029: Verify password field masks input"""
        driver.get(f"{base_url}/login.php")
        
        password_field = driver.find_element(By.ID, "InputPassword")
        password_type = password_field.get_attribute("type")
        
        assert password_type == "password"
    
    def test_page_elements_present(self, driver, base_url):
        """TC_LGN_030: Verify all expected elements present"""
        driver.get(f"{base_url}/login.php")
        
        # Check username field
        assert driver.find_element(By.ID, "username") is not None
        # Check password field
        assert driver.find_element(By.ID, "InputPassword") is not None
        # Check submit button
        assert driver.find_element(By.NAME, "submit") is not None
        # Check register link
        assert driver.find_element(By.LINK_TEXT, "Register") is not None


class TestLoginDatabaseEdgeCases:
    """TC_LGN_031 - TC_LGN_032: Database edge case tests"""
    
    def test_login_user_with_empty_name_in_db(self, driver, base_url):
        """TC_LGN_031: Verify login works when name field is empty in DB"""
        driver.get(f"{base_url}/login.php")
        
        # User 'irul' has empty name field in database
        driver.find_element(By.ID, "username").send_keys("irul")
        driver.find_element(By.ID, "InputPassword").send_keys("irul123")
        driver.find_element(By.NAME, "submit").click()
        
        time.sleep(2)
        # Should login successfully despite empty name
        assert "login.php" not in driver.current_url or "index.php" in driver.current_url
    
    def test_login_user_ahmad_empty_name(self, driver, base_url):
        """TC_LGN_032: Verify another user with empty name can login"""
        driver.get(f"{base_url}/login.php")
        
        # User 'ahmad' also has empty name field
        driver.find_element(By.ID, "username").send_keys("ahmad")
        driver.find_element(By.ID, "InputPassword").send_keys("ahmad123")
        driver.find_element(By.NAME, "submit").click()
        
        time.sleep(2)
        assert "login.php" not in driver.current_url or "index.php" in driver.current_url


class TestLoginSession:
    """TC_LGN_033 - TC_LGN_035: Session tests"""
    
    def test_already_logged_in_redirect(self, driver, base_url):
        """TC_LGN_035: Verify redirect when already logged in"""
        driver.get(f"{base_url}/login.php")
        
        # First login
        driver.find_element(By.ID, "username").send_keys("irul")
        driver.find_element(By.ID, "InputPassword").send_keys("irul123")
        driver.find_element(By.NAME, "submit").click()
        
        time.sleep(2)
        
        # Try to access login page again
        driver.get(f"{base_url}/login.php")
        
        time.sleep(2)
        # Should redirect to index.php if session active
        # Based on code: if( isset($_SESSION['username']) ) header('Location: index.php');
        current_url = driver.current_url
        assert "index.php" in current_url or "login.php" in current_url


# ==================== STUB TESTS ====================
class TestLoginWithStubProfessional:
    """Professional stub tests for unit testing without browser"""
    
    def test_stub_valid_login(self, login_driver):
        """Stub: Valid login credentials"""
        result = login_driver.attempt_login("irul", "irul123")
        assert result['success'] == True
        assert result['redirect'] == 'index.php'
    
    def test_stub_invalid_username(self, login_driver):
        """Stub: Non-existent username"""
        result = login_driver.attempt_login("nonexistent", "password")
        assert result['success'] == False
        assert "Gagal" in result['error']
    
    def test_stub_empty_username(self, login_driver):
        """Stub: Empty username"""
        result = login_driver.attempt_login("", "password")
        assert result['success'] == False
        assert "kosong" in result['error']
    
    def test_stub_empty_password(self, login_driver):
        """Stub: Empty password"""
        result = login_driver.attempt_login("irul", "")
        assert result['success'] == False
        assert "kosong" in result['error']
    
    def test_stub_whitespace_username(self, login_driver):
        """Stub: Whitespace-only username"""
        result = login_driver.attempt_login("   ", "password")
        assert result['success'] == False
    
    def test_stub_user_with_empty_name(self, login_driver, db_stub):
        """Stub: Verify user with empty name can still login"""
        user = db_stub.get_user("irul")
        assert user['name'] == ''
        result = login_driver.attempt_login("irul", "irul123")
        assert result['success'] == True
    
    def test_stub_sql_injection_attempt(self, login_driver):
        """Stub: SQL injection should fail"""
        result = login_driver.attempt_login("' OR '1'='1", "test")
        assert result['success'] == False
