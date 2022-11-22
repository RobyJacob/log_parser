from app import app


def test_parse():
    with app.test_client() as test_client:
        import json
        import base64

        content_bytes = base64.encodebytes("[ 0]ENTER: /usr/local/src/pkg/apis/machineconfiguration.openshift.io/v1"
                                           "/register.go:28 0".encode())
        response = test_client.post("/parse", data=content_bytes)

        exp_result = {"results": [
            {
                "operation": "ENTER",
                "file_name": "/usr/local/src/pkg/apis/machineconfiguration.openshift.io/v1/register.go",
                "line_number": "28",
                "name": "anonymous"
            }
        ]}

        response_data = json.loads(response.data.decode())

        for result in response_data.get("results"):
            for k, v in result.items():
                assert v == exp_result.get("results")[0].get(k)


def test_parse_empty_data():
    with app.test_client() as test_client:
        response = test_client.post("/parse", data=b"")

        assert response.data == b'{"results":[]}\n'


def test_parse_valid_name_field():
    with app.test_client() as test_client:
        import json
        import base64

        content_bytes_valid1 = base64.encodebytes("[ 0]ENTER: /usr/local/src/pkg/apis/machineconfiguration.openshift.io/v1"
                                           "/register.go:28 addKnownTypes".encode())
        content_bytes_valid2 = base64.encodebytes(
            "[ 0]ENTER: /usr/local/src/pkg/apis/machineconfiguration.openshift.io/v1"
            "/register.go:28 addKnownTypes".encode())
        response1 = test_client.post("/parse", data=content_bytes_valid1)
        response2 = test_client.post("/parse", data=content_bytes_valid2)

        exp_result = {"results": [
            {
                "operation": "ENTER",
                "file_name": "/usr/local/src/pkg/apis/machineconfiguration.openshift.io/v1/register.go",
                "line_number": "28",
                "name": "addKnownTypes"
            }
        ]}

        response_data1 = json.loads(response1.data.decode())
        response_data2 = json.loads(response2.data.decode())

        for result in response_data1.get("results"):
            for k, v in result.items():
                assert v == exp_result.get("results")[0].get(k)

        for result in response_data2.get("results"):
            for k, v in result.items():
                assert v == exp_result.get("results")[0].get(k)


def test_parse_invalid_name_field():
    with app.test_client() as test_client:
        import json
        import base64

        content_bytes = base64.encodebytes("[ 0]ENTER: /usr/local/src/pkg/apis/machineconfiguration.openshift.io/v1"
                                           "/register.go:28 1addKnownTypes".encode())
        response = test_client.post("/parse", data=content_bytes)

        exp_result = {"results": [
            {
                "operation": "ENTER",
                "file_name": "/usr/local/src/pkg/apis/machineconfiguration.openshift.io/v1/register.go",
                "line_number": "28",
                "name": "anonymous"
            }
        ]}

        response_data = json.loads(response.data.decode())

        for result in response_data.get("results"):
            for k, v in result.items():
                assert v == exp_result.get("results")[0].get(k)
