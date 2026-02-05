# The application prompts the user to enter two numbers and select an arithmetic operation. It then displays the result and asks if the user wishes to perform another calculation.

# Input:
# Enter first number: 15
# Enter second number: 4
# Select operation (+, -, *, /): *

# Output:
# Calculating: 15 * 4
# Result: 60.0
# Would you like to perform another calculation? (y/n): n
# Goodbye!

# Input (Error Handling Case):
# Enter first number: 10
# Enter second number: 0
# Select operation (+, -, *, /): /

# Output:
# Error: Division by zero is not allowed.
# Please try again.

import gradio as gr  # type: ignore


def calculate(num_1, num_2, operation):
    operations = ["add", "subtract", "multiply", "divide"]
    # user_input_1 = input(f"Enter first number: ").strip().lower()
    # if not num_1.isdigit():
    #      return "Invalid entry!"

    # user_input_2 = input(f"Enter second number: ").strip().lower()
    # if not num_2.isdigit():
    #      return "Invalid entry!"

    # user_input_operation = input(f"Select operation: {', '.join(operations)} ").strip().lower()
    if operation not in operations:
        return "Invalid entry!"

    num1 = int(num_1)
    num2 = int(num_2)
    calculated_result = 0
    if operation == "multiply":
        calculated_result = num1 * num2
    elif operation == "add":
        calculated_result = num1 + num2
    elif operation == "subtract":
        calculated_result = num1 - num2
    else:
        if 0 == num2:
            return "Error: Division by zero is not allowed. /n Please try again."
        calculated_result = num1 / num2

    return calculated_result


demo = gr.Interface(
    fn=calculate,
    inputs=["slider", "slider", gr.Radio(["add", "subtract", "multiply", "divide"])],
    outputs=[gr.Textbox(label="Output")],
)


if __name__ == "__main__":
    demo.launch()
