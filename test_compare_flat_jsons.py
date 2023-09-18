from gendiff.json_diff import compare_json_dicts


def test_equal_jsons():
    json1 = {"name": "Alice", "age": 30, "city": "New York"}
    json2 = {"name": "Alice", "age": 30, "city": "New York"}
    result = compare_json_dicts(json1, json2)
    expected_diff = {'age': {'=': 30}, 'city': {'=': 'New York'}, 'name': {'=': 'Alice'}}
    assert result == expected_diff


def test_unequal_jsons():
    json1 = {"name": "Alice", "age": 30, "city": "New York"}
    json2 = {"name": "Bob", "age": 25, "city": "Los Angeles"}
    result = compare_json_dicts(json1, json2)
    expected_diff = {'city': {'-': 'New York', '+': 'Los Angeles'}, 'name': {'-': 'Alice', '+': 'Bob'}, 'age': {'-': 30, '+': 25}}
    assert result == expected_diff


def test_partial_match():
    json1 = {"name": "Alice", "age": 30, "city": "New York"}
    json2 = {"name": "Alice", "age": 30, "city": "Душанбе"}
    result = compare_json_dicts(json1, json2)
    expected_diff = {'city': {'-': 'New York', '+': 'Душанбе'}, 'name': {'=': 'Alice'}, 'age': {'=': 30}}
    assert result == expected_diff
