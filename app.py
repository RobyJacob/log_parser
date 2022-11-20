from flask import Flask, request, make_response

from log_parser import Parser

app = Flask(__name__)


@app.route("/parse", methods=["POST"])
def parse():
    data = request.data
    parser = Parser(data)
    parsed_data = parser.parse()

    return make_response(parsed_data)


@app.route("/health", methods=["GET"])
def check_health():
    return make_response("server is healthy")


if __name__ == "__main__":
    app.run(port=9999, debug=True, threaded=True)
