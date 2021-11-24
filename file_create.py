import json
import slutuppdragv1

class CJSON:

    def create_file():
        with open("data_file.json", "w") as write_file:
            json.dump(slutuppdragv1(), write_file)