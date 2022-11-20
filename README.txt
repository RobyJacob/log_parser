A simple API to parse relevant information from
input file containing CI logs.

HOW TO RUN
==========
1. clone repository
2. cd into cloned repository
2. execute docker build -t <some tag> .
3. execute docker run -d -p 9999:9999 <img name>

ENDPOINTS
=========
1. GET /health
    Health check endpoint
    Eg: curl -X GET http://localhost:9999/health
2. POST /parse
    Parse relevant information
    Eg: curl -X POST -H 'Content-Type:application/json' -d "$(cat logs/test1.log | base64)" http://localhost:9999/parse
