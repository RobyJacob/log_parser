import base64
import re


class Parser:
    def __init__(self, byte_string):
        self.content_byte = byte_string

    def parse(self):
        """
        1. Decode byte string
        2. Filter irrelevant data using regex
        3. Extract relevant information
        :return: Dict
        """
        content_str = base64.decodebytes(self.content_byte).decode()
        contents = re.findall("\[\s\d\](.*)", content_str)
        filtered_contents = list(map(lambda content: content.split(),
                                     contents))
        parsed_contents = {"results": []}

        for content in filtered_contents:
            operation = content[0][:-1]
            file_name, line_number = content[1].split(":")
            name = "anonymous" if content[2] == "0" else content[2]

            parsed_content = {
                "operation": operation,
                "file_name": file_name,
                "line_number": line_number,
                "name": name
            }
            parsed_contents.get("results").append(parsed_content)

        return parsed_contents
