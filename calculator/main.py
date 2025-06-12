# print(3 + 7 * 2) The result when the AI Agent tried to fix the problem.
# print((3 + 7) * 2) The result when the AI Agent tried to fix the problem again.
# - Calling function: write_file
#  - Calling function: run_python_file
#  - Calling function: write_file
#  - Calling function: run_python_file
# Final response:
# I have fixed the bug by adding parentheses to enforce the desired order of operations. 
# The corrected code `print((3 + 7) * 2)` now calculates `3 + 7` first, resulting in `10`. 
# Then, it multiplies `10` by `2`, which equals `20`.
# CLI prompt: python3 main.py “fix the bug: 3 + 7 * 2 shouldn't be 20”
# CLI prompt: python3 calculator/main.py “repair the bug: 3 + 7 * 2 shouldn't be 20”
# CLI prompt: python3 main.py "fix the calculator logic in calculator/main.py, 
# do not overwrite the entire file., 3 + 7 * 2 is not 20"

import sys
from pkg.calculator import Calculator
from pkg.render import render


def main():
    calculator = Calculator()
    if len(sys.argv) <= 1:
        print("Calculator App")
        print('Usage: python main.py "<expression>"')
        print('Example: python main.py "3 + 5"')
        return

    expression = " ".join(sys.argv[1:])
    try:
        result = calculator.evaluate(expression)
        to_print = render(expression, result)
        print(to_print)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()