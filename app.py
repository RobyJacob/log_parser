from flask import Flask, request, make_response

from log_parser import Parser

app = Flask(__name__)


@app.route("/parse", methods=["POST"])
def parse():
    """
    Parse input byte string and extract relevant information
    :return: byte
    """
    data = request.data
    parser = Parser(data)
    parsed_data = parser.parse()

    return make_response(parsed_data)


@app.route("/health", methods=["GET"])
def check_health():
    """
    Health check endpoint, returns status 200 if app
    is reachable
    :return: str
    """
    return make_response("server is healthy")


if __name__ == "__main__":
    app.run(port=9999, host="0.0.0.0",
            debug=True, processes=3, threaded=False)
