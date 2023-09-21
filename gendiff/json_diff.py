import json


def compare_json_dicts(dict1, dict2):
    diff = {}
    keys1 = set(dict1.keys())
    keys2 = set(dict2.keys())
    if keys1 != keys2:
        return False
    for key in keys1 - keys2:
        diff[key] = {"-": dict1[key]}
    for key in keys2 - keys1:
        diff[key] = {"+": dict2[key]}

    for key in keys1 & keys2:
        if dict1[key] != dict2[key]:
            diff[key] = {"-": dict1[key], "+": dict2[key]}
        elif dict1[key] == dict2[key]:
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
