from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    nim = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    grades = db.relationship("Grade", backref="student", lazy=True, cascade="all, delete-orphan")

    def to_dict(self):
        return {"id": self.id, "nim": self.nim, "name": self.name, "email": self.email}


class Grade(db.Model):
    __tablename__ = "grades"
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("students.id"), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    score = db.Column(db.Float, nullable=False)
    credit = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {"id": self.id, "student_id": self.student_id, "subject": self.subject,
                "score": self.score, "credit": self.credit,
                "grade_letter": grade_letter(self.score),
                "grade_point": grade_point(self.score)}


def grade_letter(score):
    if score >= 85: return "A"
    if score >= 75: return "B"
    if score >= 65: return "C"
    if score >= 55: return "D"
    return "E"


def grade_point(score):
    if score >= 85: return 4.0
    if score >= 75: return 3.0
    if score >= 65: return 2.0
    if score >= 55: return 1.0
    return 0.0
