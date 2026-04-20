from src.models import grade_letter, grade_point


def test_letter_A_top(): assert grade_letter(100) == "A"
def test_letter_A_boundary(): assert grade_letter(85) == "A"
def test_letter_B(): assert grade_letter(80) == "B"
def test_letter_B_boundary(): assert grade_letter(75) == "B"
def test_letter_C(): assert grade_letter(70) == "C"
def test_letter_C_boundary(): assert grade_letter(65) == "C"
def test_letter_D(): assert grade_letter(60) == "D"
def test_letter_D_boundary(): assert grade_letter(55) == "D"
def test_letter_E(): assert grade_letter(54) == "E"
def test_letter_E_zero(): assert grade_letter(0) == "E"
def test_point_A(): assert grade_point(90) == 4.0
def test_point_B(): assert grade_point(78) == 3.0
def test_point_C(): assert grade_point(68) == 2.0
def test_point_D(): assert grade_point(60) == 1.0
def test_point_E(): assert grade_point(40) == 0.0
