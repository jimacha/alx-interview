# main.py

from importlib.machinery import SourceFileLoader

pascal_triangle = SourceFileLoader("pascal_triangle", "./0-pascal_triangle.py").load_module()

def print_triangle(triangle):
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    print_triangle(pascal_triangle.pascal_triangle(5))

