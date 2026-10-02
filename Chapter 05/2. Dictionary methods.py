marks = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78
}

print(marks.keys())  # Output: dict_keys(['Alice', 'Bob', 'Charlie'])
print(marks.values())  # Output: dict_values([85, 90, 78])
print(marks.items())  # Output: dict_items([('Alice', 85), ('Bob', 90), ('Charlie', 78)])
marks.update({"David": 92})
print(marks)  # Output: {'Alice': 85, 'Bob': 90, 'Charlie': 78, 'David': 92}

print(marks.get("Eve", "Not Found"))  # Output: Not Found
print(marks.pop("Charlie"))  # Output: 78