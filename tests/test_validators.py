from src.validators import (validate_nim, validate_name, validate_email,
                             validate_score, validate_credit, validate_subject)


def test_nim_valid_numeric():
    ok, _ = validate_nim("12345"); assert ok

def test_nim_valid_alphanumeric():
    ok, _ = validate_nim("ABC12345"); assert ok

def test_nim_too_short():
    ok, msg = validate_nim("123"); assert not ok and "5-20" in msg

def test_nim_too_long():
    ok, _ = validate_nim("A" * 21); assert not ok

def test_nim_has_dash():
    ok, _ = validate_nim("123-456"); assert not ok

def test_nim_empty():
    ok, _ = validate_nim(""); assert not ok

def test_nim_none():
    ok, _ = validate_nim(None); assert not ok

def test_name_valid_full():
    ok, _ = validate_name("Budi Santoso"); assert ok

def test_name_valid_single():
    ok, _ = validate_name("Budi"); assert ok

def test_name_too_short():
    ok, _ = validate_name("A"); assert not ok

def test_name_has_number():
    ok, _ = validate_name("Budi123"); assert not ok

def test_name_empty():
    ok, _ = validate_name(""); assert not ok

def test_email_valid():
    ok, _ = validate_email("budi@mail.com"); assert ok

def test_email_valid_subdomain():
    ok, _ = validate_email("budi@mail.univ.ac.id"); assert ok

def test_email_missing_at():
    ok, _ = validate_email("budimail.com"); assert not ok

def test_email_empty():
    ok, _ = validate_email(""); assert not ok

def test_score_valid():
    ok, _ = validate_score(85.5); assert ok

def test_score_zero():
    ok, _ = validate_score(0); assert ok

def test_score_hundred():
    ok, _ = validate_score(100); assert ok

def test_score_above_100():
    ok, _ = validate_score(101); assert not ok

def test_score_negative():
    ok, _ = validate_score(-1); assert not ok

def test_score_non_numeric():
    ok, _ = validate_score("bagus"); assert not ok

def test_credit_valid():
    ok, _ = validate_credit(3); assert ok

def test_credit_one():
    ok, _ = validate_credit(1); assert ok

def test_credit_six():
    ok, _ = validate_credit(6); assert ok

def test_credit_zero():
    ok, _ = validate_credit(0); assert not ok

def test_credit_above_six():
    ok, _ = validate_credit(7); assert not ok

def test_credit_non_integer():
    ok, _ = validate_credit("abc"); assert not ok

def test_subject_valid():
    ok, _ = validate_subject("Algoritma"); assert ok

def test_subject_empty():
    ok, _ = validate_subject(""); assert not ok

def test_subject_none():
    ok, _ = validate_subject(None); assert not ok
