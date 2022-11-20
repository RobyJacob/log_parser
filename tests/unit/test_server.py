from app import app


def test_server_running():
    with app.test_client() as test_client:
        response = test_client.get("/health")

        assert response.status_code == 200
        assert response.data == b"server is healthy"
