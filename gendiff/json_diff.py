import json


def compare_json_dicts(dict1, dict2):
    diff = {}
    keys1 = set(dict1.keys())
    keys2 = set(dict2.keys())


    diff.update(get_added_removed_keys(dict1, dict2))
    diff.update(get_modified_keys(dict1, dict2))

    return diff

def get_added_removed_keys(dict1, dict2):
    diff = {}
    for key in dict1.keys() - dict2.keys():
        diff[key] = {"-": dict1[key]}
    for key in dict2.keys() - dict1.keys():
        diff[key] = {"+": dict2[key]}
    return diff

def get_modified_keys(dict1, dict2):
    diff = {}
    for key in dict1.keys() & dict2.keys():
        if dict1[key] != dict2[key] :
            diff[key] = {"-": dict1[key], "+": dict2[key]}
        else:
            diff[key] = {"=": dict1[key]}
    return diff


def format_diff(diff):
    lines = []
    for key, changes in sorted(diff.items()):
        if "-" in changes:
            lines.append(f"- {key}: {changes['-']}")
        if "+" in changes:
            lines.append(f"+ {key}: {changes['+']}")
        if '=' in changes:
            lines.append(f"  {key}: {changes['=']}")
    return "{\n" + "\n".join(lines) + "\n}"


file1 = {
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": False
  }
file2 = {
    "timeout": 20,
    "verbose": True,
    "host": "hexlet.io"
  }
print(compare_json_dicts(file1, file2))
print(format_diff(compare_json_dicts(file1, file2)))


def generate_diff(file1_path, file2_path):
    with open(file1_path, "r") as file1, open(file2_path, "r") as file2:
        data1 = json.load(file1)
        data2 = json.load(file2)

    diff = compare_json_dicts(data1, data2)
    return format_diff(diff)
