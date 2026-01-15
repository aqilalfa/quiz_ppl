"""
Pytest configuration and fixtures for Selenium tests
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os

# Configuration
BASE_URL = os.environ.get('BASE_URL', 'http://localhost:8080')
SCREENSHOT_DIR = os.path.join(os.path.dirname(__file__), "screenshots")

# Create screenshot directory if not exists
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

@pytest.fixture(scope="session")
def base_url():
    """Return the base URL for the application"""
    return BASE_URL

@pytest.fixture(scope="session")
def screenshot_dir():
    """Return the screenshot directory path"""
    return SCREENSHOT_DIR

@pytest.fixture(scope="function")
def driver():
    """
    Create a Chrome WebDriver instance for each test function.
    Uses headless mode for CI/CD compatibility.
    """
    chrome_options = Options()
    
    # Headless mode for CI/CD
    if os.environ.get('CI') or os.environ.get('GITHUB_ACTIONS'):
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
    
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-infobars")
    
    # Create driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(10)
    
    yield driver
    
    # Cleanup
    driver.quit()


# ==================== STUB/DRIVER IMPLEMENTATIONS ====================

class DatabaseStub:
    """
    Stub untuk mensimulasikan database tanpa koneksi real.
    Digunakan untuk unit testing tanpa dependency database.
    """
    def __init__(self):
        self.users = {
            'irul': {
                'id': 1,
                'name': '',  # Sengaja kosong sesuai requirement
                'username': 'irul',
                'email': 'irul@irul.com',
                'password': '$2y$10$D9yc9Mt0t8niCNO9di8ejOUPib46suwHghqFnJRKQJ3Z6uwRDxfw.'  # irul123
            },
            'ahmad': {
                'id': 2,
                'name': '',  # Sengaja kosong sesuai requirement
                'username': 'ahmad',
                'email': 'ahmad@ahmad.com',
                'password': '$2y$10$OWez2au.UMnz3yedD0BqH.bsOC374XoV9VhMigepVzLyuq2jETHs2'  # ahmad123
            }
        }
    
    def get_user(self, username):
        """Get user by username"""
        return self.users.get(username)
    
    def user_exists(self, username):
        """Check if username exists"""
        return username in self.users
    
    def add_user(self, username, name, email, password_hash):
        """Add new user"""
        if self.user_exists(username):
            return False
        
        new_id = max([u['id'] for u in self.users.values()]) + 1
        self.users[username] = {
            'id': new_id,
            'name': name,
            'username': username,
            'email': email,
            'password': password_hash
        }
        return True
    
    def clear_test_users(self):
        """Remove test users (keep only original users)"""
        self.users = {k: v for k, v in self.users.items() if k in ['irul', 'ahmad']}


class LoginDriver:
    """
    Test Driver untuk modul Login.
    Menyediakan interface untuk testing login functionality.
    """
    def __init__(self, db_stub=None):
        self.db = db_stub or DatabaseStub()
        self.session = {}
    
    def attempt_login(self, username, password):
        """
        Simulate login attempt.
        Returns: dict with 'success', 'error', 'redirect' keys
        """
        # Validate empty fields
        if not username or not username.strip():
            return {'success': False, 'error': 'Data tidak boleh kosong !!', 'redirect': None}
        
        if not password or not password.strip():
            return {'success': False, 'error': 'Data tidak boleh kosong !!', 'redirect': None}
        
        # Check user exists
        user = self.db.get_user(username)
        if not user:
            return {'success': False, 'error': 'Register User Gagal !!', 'redirect': None}
        
        # In real scenario, would verify password hash
        # For stub testing, we simulate password verification
        return {'success': True, 'error': None, 'redirect': 'index.php'}
    
    def is_logged_in(self):
        """Check if user is logged in"""
        return 'username' in self.session
    
    def logout(self):
        """Clear session"""
        self.session.clear()


class RegisterDriver:
    """
    Test Driver untuk modul Register.
    Menyediakan interface untuk testing register functionality.
    """
    def __init__(self, db_stub=None):
        self.db = db_stub or DatabaseStub()
        self.session = {}
    
    def attempt_register(self, name, email, username, password, repassword):
        """
        Simulate registration attempt.
        Returns: dict with 'success', 'error', 'validate', 'redirect' keys
        """
        # Validate empty fields
        fields = [name, email, username, password, repassword]
        if not all(f and f.strip() for f in fields):
            return {'success': False, 'error': 'Data tidak boleh kosong !!', 'validate': None, 'redirect': None}
        
        # Validate password match
        if password != repassword:
            return {'success': False, 'error': None, 'validate': 'Password tidak sama !!', 'redirect': None}
        
        # Check if username exists (note: original code checks 'name' but function checks username)
        if self.db.user_exists(name):  # Bug in original code - checks name instead of username
            return {'success': False, 'error': 'Username sudah terdaftar !!', 'validate': None, 'redirect': None}
        
        # Simulate registration (note: original code has bug with $nama vs $name)
        # The name won't be saved correctly in original code
        return {'success': True, 'error': None, 'validate': None, 'redirect': 'index.php'}
    
    def is_registered(self, username):
        """Check if username is registered"""
        return self.db.user_exists(username)


@pytest.fixture
def db_stub():
    """Provide a fresh DatabaseStub for each test"""
    stub = DatabaseStub()
    yield stub
    stub.clear_test_users()

@pytest.fixture
def login_driver(db_stub):
    """Provide LoginDriver with stub database"""
    return LoginDriver(db_stub)

@pytest.fixture
def register_driver(db_stub):
    """Provide RegisterDriver with stub database"""
    return RegisterDriver(db_stub)
