from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_calculate_deposit_v1():
    response = client.post("/deposit/calculation", json={"date": "31.01.2021",
                                                         "periods": 3,
                                                         "amount": 10000,
                                                         "rate": 6})
    assert response.status_code == 200
    assert response.json() == {"31.01.2021": 10050, "28.02.2021": 10100.25, "31.03.2021": 10150.75}


def test_calculate_deposit_v2():
    response = client.post("/deposit/calculation", json={"date": "31.01.2021",
                                                         "periods": 7,
                                                         "amount": 10000,
                                                         "rate": 6})
    assert response.status_code == 200
    assert response.json() == {"31.01.2021": 10050, "28.02.2021": 10100.25, "31.03.2021": 10150.75,
                               "30.04.2021": 10201.5, "31.05.2021": 10252.51, "30.06.2021": 10303.77,
                               "31.07.2021": 10355.29}


def test_bad_date_day():
    response = client.post("/deposit/calculation", json={"date": "34.01.2021",
                                                         "periods": 3,
                                                         "amount": 10000,
                                                         "rate": 6})
    assert response.status_code == 400
    assert response.json() == {"detail": "Incorrect date day"}


def test_bad_date_month():
    response = client.post("/deposit/calculation", json={"date": "31.13.2021",
                                                         "periods": 3,
                                                         "amount": 10000,
                                                         "rate": 6})
    assert response.status_code == 400
    assert response.json() == {"detail": "Incorrect date month"}


def test_bad_date_year():
    response = client.post("/deposit/calculation", json={"date": "31.12.0",
                                                         "periods": 3,
                                                         "amount": 10000,
                                                         "rate": 6})
    assert response.status_code == 400
    assert response.json() == {"detail": "Incorrect date year"}


def test_bad_periods():
    response = client.post("/deposit/calculation", json={"date": "31.12.2021",
                                                         "periods": 100,
                                                         "amount": 10000,
                                                         "rate": 6})
    assert response.status_code == 400
    assert response.json() == {"detail": "Incorrect periods. Periods must be in range 1 - 60"}


def test_bad_amount():
    response = client.post("/deposit/calculation", json={"date": "31.12.2021",
                                                         "periods": 3,
                                                         "amount": 1000,
                                                         "rate": 6})
    assert response.status_code == 400
    assert response.json() == {"detail": "Incorrect amount. Amount must be in range 10 000 - 3 000 000"}


def test_bad_rate():
    response = client.post("/deposit/calculation", json={"date": "31.12.2021",
                                                         "periods": 3,
                                                         "amount": 10000,
                                                         "rate": 10})
    assert response.status_code == 400
    assert response.json() == {"detail": "Incorrect rate. Rate must be in range 1 - 8"}
