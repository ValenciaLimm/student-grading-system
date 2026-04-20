# Student Grading System

![CI](https://github.com/ValenciaLimm/student-grading-system/actions/workflows/ci.yml/badge.svg)
![Coverage](https://img.shields.io/badge/coverage-93%25-brightgreen.svg)

REST API manajemen nilai mahasiswa - Final Project Software Testing.

## Fitur Utama

1. Manajemen Mahasiswa (CRUD) - /api/students
2. Manajemen Nilai - /api/students/<id>/grades
3. Transkrip dan IPK - /api/students/<id>/transcript

## Cara Menjalankan Aplikasi

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python main.py

Server berjalan di http://localhost:5000

## Cara Menjalankan Test

    pytest
    pytest --cov=src --cov-report=term-missing
    pytest --cov=src --cov-report=html

## Strategi Pengujian

- Unit Tests (65): test_validators.py, test_models.py, test_services.py
- Integration Tests (8): test_integration.py
- Coverage: 93% (target minimum 60%)

## Pipeline CI/CD

GitHub Actions otomatis pada push dan PR:
checkout -> setup Python -> install deps -> build -> unit tests -> integration tests -> coverage report -> upload artifact.

## Tech Stack

Python 3.11, Flask 3.0, SQLAlchemy 2.0, SQLite, Pytest 8.2, GitHub Actions
