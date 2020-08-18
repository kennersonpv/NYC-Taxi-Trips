import json

class ImportFile:

    def __init__(self, table):
        self.table = table

    def importJson(self, file):
        for line in file.readlines():
            try:
                self.table.append(json.loads(line))
            except ValueError:
                continue
        return self.table