# Variable type hint
age: int = 25
# Function type hints
def greeting(name: str) -> str:
    return f"Hello, {name}!"
# Usage
print(greeting("Alice"))

def sum(a : int, b : int) -> int:
    c = a + b
    return f"Sum os {a} and {b} is: {c} "

print(sum(5, 6))