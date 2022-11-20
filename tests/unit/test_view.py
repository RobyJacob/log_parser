import base64

from app import app


def test_parse():
    with app.test_client() as test_client:
        import json

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

