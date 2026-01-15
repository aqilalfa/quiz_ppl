## Quiz Pengujian Piranti Lunak 

Diperlukan Stub untuk menguji modul

# Modul #

- Login
- Register

# Requirement #

- PHP
- MySQL

# Installasi #

- Clone atau download repository ini ke folder htdocs di komputer
- Import file sql database yang berada pada folder db

---

# Testing Documentation

## Deskripsi
Proyek ini berisi modul Login dan Register dengan testing menggunakan Selenium WebDriver dan Pytest.
**Total: 81 Test Cases** (38 Login + 43 Register)

## Struktur Proyek

```
quiz-pengupil/
├── .github/
│   └── workflows/
│       └── selenium-tests.yml          # CI/CD Pipeline GitHub Actions
├── db/
│   └── quiz_pengupil.sql               # Database schema
├── tests/
│   ├── conftest.py                     # Pytest fixtures dan Stub/Driver
│   ├── generate_complete_testcase.py   # Script generate test case xlsx
│   ├── requirements.txt                # Dependencies untuk testing
│   ├── test_login_professional.py      # 38 Test cases untuk modul login
│   ├── test_register_professional.py   # 43 Test cases untuk modul register
│   └── TestCase_Complete_81_Tests.xlsx # Dokumen test case lengkap
├── koneksi.php                         # Database connection
├── login.php                           # Modul Login
├── register.php                        # Modul Register
├── style.css                           # Styling
├── pytest.ini                          # Pytest configuration
└── README.md                           # Dokumentasi ini
```

## Test Results Summary

| Module | Total Tests | Passed | Failed | Pass Rate |
|--------|-------------|--------|--------|-----------|
| Login  | 38          | 36     | 2      | 94.7%     |
| Register | 43        | 43     | 0      | 100%      |
| **TOTAL** | **81**   | **79** | **2**  | **97.5%** |

### Failed Tests (Security Findings)
| TC_ID | Test Name | Issue |
|-------|-----------|-------|
| TC_LGN_002 | test_login_case_sensitivity_username | Username NOT case-sensitive |
| TC_LGN_015 | test_sql_injection_basic | SQL Injection vulnerability detected |

## Test Categories

| Category | Login | Register | Total |
|----------|-------|----------|-------|
| Functional - Positive | 2 | 2 | 4 |
| Functional - Negative | 7 | 6 | 13 |
| Boundary Value | 5 | 6 | 11 |
| Security | 7 | 6 | 13 |
| Special Characters | 3 | 3 | 6 |
| Usability | 4 | 5 | 9 |
| Validation | 0 | 5 | 5 |
| Database Edge Cases | 2 | 0 | 2 |
| Session | 1 | 0 | 1 |
| Bug Verification | 0 | 2 | 2 |
| Unit Test - Stub | 7 | 7 | 14 |

## Stub dan Driver

### DatabaseStub
Stub untuk mensimulasikan database tanpa koneksi real. Digunakan untuk unit testing.

```python
class DatabaseStub:
    def get_user(self, username)
    def user_exists(self, field, value)
    def add_user(self, username, name, email, password_hash)
```

### LoginDriver
Test Driver untuk modul Login.

```python
class LoginDriver:
    def attempt_login(self, username, password)
    def is_logged_in()
    def logout()
```

### RegisterDriver
Test Driver untuk modul Register.

```python
class RegisterDriver:
    def attempt_register(self, name, email, username, password, repassword)
    def validate_registration(self, name, email, username, password, repassword)
    def is_registered(self, username)
```

## Cara Menjalankan Test

### Prerequisites
1. Python 3.8+
2. Chrome Browser
3. PHP 7.4+ dengan MySQL
4. Laragon (recommended) atau XAMPP

### Install Dependencies
```bash
pip install -r tests/requirements.txt
```

### Setup Database
```bash
# Import database menggunakan MySQL client atau phpMyAdmin
mysql -u root -p < db/quiz_pengupil.sql
```

### Jalankan PHP Server
```bash
php -S localhost:8000
```

### Jalankan Semua Test (81 tests)
```bash
set BASE_URL=http://localhost:8000
pytest tests/test_login_professional.py tests/test_register_professional.py -v
```

### Jalankan Test dengan Stub/Driver saja (Unit Tests)
```bash
pytest tests/test_login_professional.py::TestLoginWithStubProfessional tests/test_register_professional.py::TestRegisterWithStubProfessional -v
```

### Generate Test Report HTML
```bash
pytest tests/test_login_professional.py tests/test_register_professional.py -v --html=test-report.html --self-contained-html
```

## CI/CD Pipeline (GitHub Actions)

Pipeline akan berjalan otomatis saat:
- Push ke branch `main` atau `master`
- Pull request ke branch `main` atau `master`

### Pipeline Steps:
1. **Checkout repository**
2. **Setup PHP 8.2** dengan extensions mysqli, pdo_mysql
3. **Setup Python 3.11**
4. **Setup Chrome & ChromeDriver**
5. **Start MySQL service** (Docker)
6. **Import database**
7. **Start PHP built-in server**
8. **Run Stub/Driver Tests** (Unit Tests)
9. **Run Selenium Tests** (Integration Tests)
10. **Upload test report** sebagai artifact

### CI/CD Status Badge
```markdown
[![Selenium Tests](https://github.com/aqilalfa/quiz_ppl/actions/workflows/selenium-tests.yml/badge.svg)](https://github.com/aqilalfa/quiz_ppl/actions/workflows/selenium-tests.yml)
```

## Known Bugs dalam Source Code

1. **register.php line 34**: Variabel `$nama` tidak terdefinisi, seharusnya `$name`
   ```php
   // Bug:
   $query = "INSERT INTO users (username,name,email, password ) VALUES ('$username','$nama','$email','$pass')";
   // Seharusnya:
   $query = "INSERT INTO users (username,name,email, password ) VALUES ('$username','$name','$email','$pass')";
   ```

2. **register.php cek_nama()**: Function memeriksa field 'name' bukan 'username' untuk duplicate check

3. **Database**: Field `name` pada user `irul` dan `ahmad` kosong (intentional untuk testing bug #1)

4. **login.php**: SQL Injection vulnerability pada field username (ditemukan oleh test TC_LGN_015)

5. **login.php**: Username tidak case-sensitive (ditemukan oleh test TC_LGN_002)

## Repository Link

**GitHub Repository**: https://github.com/aqilalfa/quiz_ppl

## Author
PPL Semester 7 - POLTEK SSN
