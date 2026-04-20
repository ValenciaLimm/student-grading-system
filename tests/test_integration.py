def _create(client, nim="12345", name="Budi Santoso", email="budi@mail.com"):
    return client.post("/api/students", json={"nim": nim, "name": name, "email": email})


def test_create_and_get(client):
    res = _create(client)
    assert res.status_code == 201
    sid = res.get_json()["id"]
    res = client.get(f"/api/students/{sid}")
    assert res.status_code == 200 and res.get_json()["nim"] == "12345"

def test_list_all(client):
    _create(client, "A0001", "Dewi", "dewi@mail.com")
    _create(client, "A0002", "Eko", "eko@mail.com")
    res = client.get("/api/students")
    assert res.status_code == 200 and len(res.get_json()) == 2

def test_update(client):
    sid = _create(client).get_json()["id"]
    res = client.put(f"/api/students/{sid}", json={"name": "Budi Santoso Nugroho"})
    assert res.status_code == 200 and res.get_json()["name"] == "Budi Santoso Nugroho"

def test_delete(client):
    sid = _create(client).get_json()["id"]
    assert client.delete(f"/api/students/{sid}").status_code == 200
    assert client.get(f"/api/students/{sid}").status_code == 404

def test_transcript_flow(client):
    sid = _create(client).get_json()["id"]
    client.post(f"/api/students/{sid}/grades", json={"subject": "Kalkulus", "score": 90, "credit": 4})
    client.post(f"/api/students/{sid}/grades", json={"subject": "Fisika", "score": 75, "credit": 2})
    res = client.get(f"/api/students/{sid}/transcript")
    body = res.get_json()
    assert res.status_code == 200 and body["total_credits"] == 6 and body["gpa"] == 3.67

def test_invalid_input_400(client):
    res = client.post("/api/students", json={"nim": "", "name": "X", "email": "t@mail.com"})
    assert res.status_code == 400

def test_invalid_score_400(client):
    sid = _create(client).get_json()["id"]
    res = client.post(f"/api/students/{sid}/grades",
                      json={"subject": "Kimia", "score": 150, "credit": 3})
    assert res.status_code == 400

def test_transcript_404(client):
    assert client.get("/api/students/9999/transcript").status_code == 404
