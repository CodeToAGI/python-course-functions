# ============================================================
# CodeToAGI — Episode 7: Functions
# GitHub : https://github.com/CodeToAGI/python-course
# ============================================================
# Try the challenge yourself FIRST before looking at this!
# Challenge: Build a Temperature Converter
# ============================================================

# Part 1: BMI Calculator (shown in video)
def calculate_bmi(weight, height):
    """Calculate Body Mass Index."""
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def get_category(bmi):
    """Return BMI category string."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25.0:
        return "Normal"
    elif bmi < 30.0:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("\n" + "="*36)
    print("  CodeToAGI — BMI Calculator")
    print("="*36)
    w = float(input("  Enter weight in kg: "))
    h = float(input("  Enter height in m:  "))
    bmi = calculate_bmi(w, h)
    cat = get_category(bmi)
    print(f"\n  BMI    : {bmi}")
    print(f"  Status : {cat}\n")

# Part 2: Temperature Converter (your challenge!)
def celsius_to_fahrenheit(celsius):
    return round(celsius * 1.8 + 32, 2)

def fahrenheit_to_celsius(fahrenheit):
    return round((fahrenheit - 32) / 1.8, 2)

def temp_converter():
    print("\n" + "="*36)
    print("  Temperature Converter")
    print("="*36)
    c = float(input("  Enter temperature in Celsius: "))
    f = celsius_to_fahrenheit(c)
    print(f"  {c}°C  =  {f}°F")
    back = fahrenheit_to_celsius(f)
    print(f"  {f}°F  =  {back}°C\n")

# Run both projects
if __name__ == "__main__":
    main()
    temp_converter()
