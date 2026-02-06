import math

def calculate_result():
    print("--- Arithmetic Calculator ---")
    
    # 1. Accept User Input (with error handling for non-numeric input)
    try:
        a = float(input("Enter value for a (divisor): "))
        b = float(input("Enter value for b (adder): "))
        c = float(input("Enter value for c (base): "))
        
        if a == 0:
            print("Error: Division by zero is not allowed.")
            return

        # 2. Perform Calculations
        # c^3 (c cubed)
        c_cubed = c ** 3
        
        # Square Root of c^3: (c^3)^(1/2)
        sqrt_c3 = c_cubed ** 0.5
        
        # Division: Square root divided by a
        div_result = sqrt_c3 / a
        
        # Multiplication: Result * 10
        mult_result = div_result * 10
        
        # Addition: Previous Step + b
        final_result = mult_result + b
        
        # 3. Generate HTML Output
        html_output = f"""
        <html>
        <head><title>Calculation Result</title></head>
        <body>
            <h1>Calculation Results</h1>
            <p><b>Inputs:</b> a={a}, b={b}, c={c}</p>
            <p>Formula: ((c^3)^0.5 / a) * 10 + b</p>
            <hr>
            <p><b>Final Result:</b> {final_result}</p>
        </body>
        </html>
        """
        print("\n--- HTML Output ---")
        print(html_output)

    except ValueError:
        print("Error: Please enter valid numerical values.")

if __name__ == "__main__":
    calculate_result()
