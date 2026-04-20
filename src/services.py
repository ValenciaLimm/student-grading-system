from .models import db, Student, Grade, grade_point
from .validators import (validate_nim, validate_name, validate_email,
                          validate_score, validate_credit, validate_subject)


class StudentService:
    @staticmethod
    def create_student(nim, name, email):
        for fn, val in [(validate_nim, nim), (validate_name, name), (validate_email, email)]:
            ok, msg = fn(val)
            if not ok: return None, msg
        if Student.query.filter_by(nim=nim.strip()).first():
            return None, "NIM sudah terdaftar"
        if Student.query.filter_by(email=email.strip()).first():
            return None, "Email sudah terdaftar"
        s = Student(nim=nim.strip(), name=name.strip(), email=email.strip())
        db.session.add(s); db.session.commit()
        return s, None

    @staticmethod
    def get_all_students():
        return Student.query.all()

    @staticmethod
    def get_student(sid):
        return db.session.get(Student, sid)

    @staticmethod
    def update_student(sid, name=None, email=None):
        s = db.session.get(Student, sid)
        if not s: return None, "Mahasiswa tidak ditemukan"
        if name:
            ok, msg = validate_name(name)
            if not ok: return None, msg
            s.name = name.strip()
        if email:
            ok, msg = validate_email(email)
            if not ok: return None, msg
            ex = Student.query.filter_by(email=email.strip()).first()
            if ex and ex.id != sid:
                return None, "Email sudah digunakan mahasiswa lain"
            s.email = email.strip()
        db.session.commit()
        return s, None

    @staticmethod
    def delete_student(sid):
        s = db.session.get(Student, sid)
        if not s: return False, "Mahasiswa tidak ditemukan"
        db.session.delete(s); db.session.commit()
        return True, None


class GradeService:
    @staticmethod
    def add_grade(sid, subject, score, credit):
        s = db.session.get(Student, sid)
        if not s: return None, "Mahasiswa tidak ditemukan"
        for fn, val in [(validate_subject, subject), (validate_score, score), (validate_credit, credit)]:
            ok, msg = fn(val)
            if not ok: return None, msg
        g = Grade(student_id=sid, subject=subject.strip(), score=float(score), credit=int(credit))
        db.session.add(g); db.session.commit()
        return g, None

    @staticmethod
    def get_student_grades(sid):
        return Grade.query.filter_by(student_id=sid).all()

    @staticmethod
    def calculate_gpa(sid):
        grades = Grade.query.filter_by(student_id=sid).all()
        if not grades: return 0.0
        total_points = sum(grade_point(g.score) * g.credit for g in grades)
        total_credits = sum(g.credit for g in grades)
        if total_credits == 0: return 0.0
        return round(total_points / total_credits, 2)

    @staticmethod
    def get_transcript(sid):
        s = db.session.get(Student, sid)
        if not s: return None, "Mahasiswa tidak ditemukan"
        grades = Grade.query.filter_by(student_id=sid).all()
        return {"student": s.to_dict(),
                "grades": [g.to_dict() for g in grades],
                "gpa": GradeService.calculate_gpa(sid),
                "total_credits": sum(g.credit for g in grades)}, None
