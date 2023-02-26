import ast


def get_function_lengths(filename):
    with open(filename, 'r') as f:
        tree = ast.parse(f.read())

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            name = node.name
            lineno = node.lineno
            end_lineno = node.end_lineno
            length = end_lineno - lineno

            # Exclude docstrings from the calculation
            docstring_len = 0
            if node.body and isinstance(node.body[0], ast.Expr) and isinstance(node.body[0].value, ast.Str):
                docstring_len = node.body[0].end_lineno - node.body[0].lineno + 1
                length -= docstring_len

            print(f"Function '{name}' has {length} lines of code (excluding {docstring_len} lines of docstring).")


if __name__ == '__main__':
    filename = input("Enter the filename: ")
    get_function_lengths(filename)
