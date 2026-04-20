from flask import Blueprint, request, jsonify
from .services import StudentService, GradeService

bp = Blueprint("api", __name__, url_prefix="/api")


@bp.route("/students", methods=["GET"])
def get_students():
    return jsonify([s.to_dict() for s in StudentService.get_all_students()]), 200


@bp.route("/students", methods=["POST"])
def create_student():
    data = request.get_json()
    if not data: return jsonify({"error": "Request body tidak valid"}), 400
    s, err = StudentService.create_student(data.get("nim"), data.get("name"), data.get("email"))
    if err: return jsonify({"error": err}), 400
    return jsonify(s.to_dict()), 201


@bp.route("/students/<int:sid>", methods=["GET"])
def get_student(sid):
    s = StudentService.get_student(sid)
    if not s: return jsonify({"error": "Mahasiswa tidak ditemukan"}), 404
    return jsonify(s.to_dict()), 200


@bp.route("/students/<int:sid>", methods=["PUT"])
def update_student(sid):
    data = request.get_json()
    if not data: return jsonify({"error": "Request body tidak valid"}), 400
    s, err = StudentService.update_student(sid, data.get("name"), data.get("email"))
    if err: return jsonify({"error": err}), 400
    return jsonify(s.to_dict()), 200


@bp.route("/students/<int:sid>", methods=["DELETE"])
def delete_student(sid):
    ok, err = StudentService.delete_student(sid)
    if err: return jsonify({"error": err}), 404
    return jsonify({"message": "Mahasiswa berhasil dihapus"}), 200


@bp.route("/students/<int:sid>/grades", methods=["POST"])
def add_grade(sid):
    data = request.get_json()
    if not data: return jsonify({"error": "Request body tidak valid"}), 400
    g, err = GradeService.add_grade(sid, data.get("subject"), data.get("score"), data.get("credit"))
    if err: return jsonify({"error": err}), 400
    return jsonify(g.to_dict()), 201


@bp.route("/students/<int:sid>/grades", methods=["GET"])
def get_grades(sid):
    return jsonify([g.to_dict() for g in GradeService.get_student_grades(sid)]), 200


@bp.route("/students/<int:sid>/transcript", methods=["GET"])
def get_transcript(sid):
    t, err = GradeService.get_transcript(sid)
    if err: return jsonify({"error": err}), 404
    return jsonify(t), 200
