from src.services import StudentService, GradeService


def test_create_student_success(app):
    s, err = StudentService.create_student("12345", "Budi", "budi@mail.com")
    assert err is None and s.nim == "12345"

def test_create_duplicate_nim(app):
    StudentService.create_student("12345", "Budi", "budi@mail.com")
    _, err = StudentService.create_student("12345", "Ani", "ani@mail.com")
    assert err is not None

def test_create_duplicate_email(app):
    StudentService.create_student("12345", "Budi", "budi@mail.com")
    _, err = StudentService.create_student("99999", "Ani", "budi@mail.com")
    assert err is not None

def test_create_invalid_nim(app):
    _, err = StudentService.create_student("", "Budi", "b@mail.com")
    assert err is not None

def test_create_invalid_email(app):
    _, err = StudentService.create_student("12345", "Budi", "bukan-email")
    assert err is not None

def test_get_all_empty(app):
    assert StudentService.get_all_students() == []

def test_get_all_multiple(app):
    StudentService.create_student("11111", "Andi", "a@mail.com")
    StudentService.create_student("22222", "Budi", "b@mail.com")
    assert len(StudentService.get_all_students()) == 2

def test_get_student_found(app):
    s, _ = StudentService.create_student("12345", "Budi", "b@mail.com")
    assert StudentService.get_student(s.id).nim == "12345"

def test_get_student_not_found(app):
    assert StudentService.get_student(9999) is None

def test_update_name(app):
    s, _ = StudentService.create_student("12345", "Budi", "b@mail.com")
    u, err = StudentService.update_student(s.id, name="Budi Santoso")
    assert err is None and u.name == "Budi Santoso"

def test_update_not_found(app):
    _, err = StudentService.update_student(9999, name="X")
    assert err is not None

def test_delete_success(app):
    s, _ = StudentService.create_student("12345", "Budi", "b@mail.com")
    ok, err = StudentService.delete_student(s.id)
    assert ok and err is None

def test_delete_not_found(app):
    ok, err = StudentService.delete_student(9999)
    assert not ok and err is not None

def test_add_grade_success(app):
    s, _ = StudentService.create_student("12345", "Budi", "b@mail.com")
    g, err = GradeService.add_grade(s.id, "Matematika", 85, 3)
    assert err is None and g.score == 85.0

def test_add_grade_invalid_score(app):
    s, _ = StudentService.create_student("12345", "Budi", "b@mail.com")
    _, err = GradeService.add_grade(s.id, "Matematika", 150, 3)
    assert err is not None

def test_add_grade_no_student(app):
    _, err = GradeService.add_grade(9999, "Matematika", 85, 3)
    assert err is not None

def test_gpa_weighted(app):
    s, _ = StudentService.create_student("12345", "Budi", "b@mail.com")
    GradeService.add_grade(s.id, "Matematika", 90, 3)
    GradeService.add_grade(s.id, "Fisika", 75, 3)
    assert GradeService.calculate_gpa(s.id) == 3.5

def test_gpa_no_grades(app):
    s, _ = StudentService.create_student("12345", "Budi", "b@mail.com")
    assert GradeService.calculate_gpa(s.id) == 0.0

def test_transcript_success(app):
    s, _ = StudentService.create_student("12345", "Budi", "b@mail.com")
    GradeService.add_grade(s.id, "Matematika", 90, 3)
    t, err = GradeService.get_transcript(s.id)
    assert err is None and t["total_credits"] == 3

def test_transcript_not_found(app):
    t, err = GradeService.get_transcript(9999)
    assert t is None and err is not None
