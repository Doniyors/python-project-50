import json


def compare_json_dicts(dict1, dict2):
    diff = {}
    keys1 = set(dict1.keys())
    keys2 = set(dict2.keys())

    if keys1 != keys2:
        return False

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
        if dict1[key] != dict2[key]:
            diff[key] = {"-": dict1[key], "+": dict2[key]}
        else:
            diff[key] = {"=": dict1[key]}
    return diff


json1 = {"name": "Alice", "age": 30, "city": "New York"}
json2 = {"name": "Bob", "age": 25, "city": "Los Angeles"}


def format_diff(diff):
    lines = []
    for key, changes in sorted(diff.items()):
        line = []
        if "-" in changes:
            line.append(f"- {key}: {changes['-']}")
        if "+" in changes:
            line.append(f"+ {key}: {changes['+']}")
        if "=" in changes:
            line.append(f"  {key}: {changes['=']}")
        lines.append("  ".join(line))
    return "{\n" + "\n".join(lines) + "\n}"


e = compare_json_dicts(json1, json2)
print(e)


def generate_diff(file1_path, file2_path):
    with open(file1_path, "r") as file1, open(file2_path, "r") as file2:
        data1 = json.load(file1)
        data2 = json.load(file2)

    diff = compare_json_dicts(data1, data2)
    return format_diff(diff)
