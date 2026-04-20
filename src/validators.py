import re


def validate_nim(nim):
    if not nim or not isinstance(nim, str):
        return False, "NIM tidak boleh kosong"
    nim = nim.strip()
    if len(nim) < 5 or len(nim) > 20:
        return False, "NIM harus antara 5-20 karakter"
    if not nim.isalnum():
        return False, "NIM hanya boleh berisi huruf dan angka"
    return True, None


def validate_name(name):
    if not name or not isinstance(name, str):
        return False, "Nama tidak boleh kosong"
    name = name.strip()
    if len(name) < 2 or len(name) > 100:
        return False, "Nama harus antara 2-100 karakter"
    if not re.match(r"^[a-zA-Z\s]+$", name):
        return False, "Nama hanya boleh berisi huruf dan spasi"
    return True, None


def validate_email(email):
    if not email or not isinstance(email, str):
        return False, "Email tidak boleh kosong"
    if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$", email.strip()):
        return False, "Format email tidak valid"
    return True, None


def validate_score(score):
    try:
        score = float(score)
    except (TypeError, ValueError):
        return False, "Nilai harus berupa angka"
    if score < 0 or score > 100:
        return False, "Nilai harus antara 0-100"
    return True, None


def validate_credit(credit):
    try:
        credit = int(credit)
    except (TypeError, ValueError):
        return False, "SKS harus berupa bilangan bulat"
    if credit < 1 or credit > 6:
        return False, "SKS harus antara 1-6"
    return True, None


def validate_subject(subject):
    if not subject or not isinstance(subject, str):
        return False, "Nama mata kuliah tidak boleh kosong"
    subject = subject.strip()
    if len(subject) < 2 or len(subject) > 100:
        return False, "Nama mata kuliah harus antara 2-100 karakter"
    return True, None
