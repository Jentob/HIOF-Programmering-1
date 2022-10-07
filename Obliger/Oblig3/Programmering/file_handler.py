import json

def write_file(list, file):
    open(file, "w").write(json.dumps(list))

def read_file(file):
    return json.loads(open(file).read())
