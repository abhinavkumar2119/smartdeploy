import app



def test_home():
    client = app.app.test_client()
    response = client.get('/')
    assert response.status_code == 200



def test_health():
    client = app.app.test_client()
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json['status'] == "OK"



def test_predict_valid():
    client = app.app.test_client()
    response = client.post('/predict', json={'input': 3})
    assert response.status_code == 200
    assert response.json['result'] == 6



def test_predict_invalid():
    client = app.app.test_client()
    response = client.post('/predict', json={})
    assert response.status_code == 400
