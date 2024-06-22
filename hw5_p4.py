#H24126094 統計116 李繕安
import re

def evaluate_expression(expression):
    try:
        # Check for unsupported characters
        if not re.match(r'^[0-9+\-*/\s()]+$', expression):
            raise ValueError("Unsupported character error: The expression contains invalid characters.")
        
        # Check for unbalanced parentheses
        if expression.count('(') != expression.count(')'):
            raise ValueError("Unbalanced parentheses error: Number of opening and closing parentheses is not equal.")

        # Evaluate the expression
        result = eval(expression)
        return result

    except ZeroDivisionError:
        return "Division by zero error: Division by zero in the expression."
    except SyntaxError:
        return "Operand error: Missing an operand before or after an operator."
    except ValueError as ve:
        return str(ve)
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    print("Enter arithmetic expressions to evaluate them. Type 'q' to quit.")

    while True:
        expression = input("Enter expression: ").strip()
        
        if expression.lower() == 'q':
            print("Exiting the program. Goodbye!")
            break
        
        result = evaluate_expression(expression)
        print("Result:", result)

if __name__ == "__main__":
    main()