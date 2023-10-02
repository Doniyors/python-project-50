from gendiff.json_diff import compare_json_dicts, json, format_diff


def generate_diff(file1_path, file2_path):
    with open(file1_path, "r") as file1, open(file2_path, "r") as file2:
        data1 = json.load(file1)
        data2 = json.load(file2)

    diff = compare_json_dicts(data1, data2)
    return format_diff(diff)
