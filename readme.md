# Quiz Pengujian Piranti Lunak

## Modul
- Login
- Register

## Requirements
- PHP 7.4+
- MySQL

## Instalasi
1. Clone repository
2. Import `db/quiz_pengupil.sql` ke MySQL
3. Jalankan `php -S localhost:8000`

---

## Testing

### Test Cases: 81 Total
- **Login**: 38 tests
- **Register**: 43 tests

### Menjalankan Test
```bash
# Install dependencies
pip install -r tests/requirements.txt

# Jalankan PHP server
php -S localhost:8000

# Jalankan semua test
set BASE_URL=http://localhost:8000
pytest tests/ -v
```

### CI/CD
GitHub Actions otomatis menjalankan test saat push/PR ke `main`.

## Repository
https://github.com/aqilalfa/quiz_ppl
