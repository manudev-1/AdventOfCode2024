import itertools

def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i in range(1, len(numbers)):
        if operators[i-1] == '+':
            result += numbers[i]
        elif operators[i-1] == '*':
            result *= numbers[i]
    return result

def solve_equations(equations):
    total_calibration_result = 0

    for equation in equations:
        test_value, numbers = equation.split(':')
        test_value = int(test_value.strip())
        numbers = list(map(int, numbers.strip().split()))
        
        operator_combinations = itertools.product(['+', '*'], repeat=len(numbers) - 1)
        
        valid_equation = False
        for operators in operator_combinations:
            if evaluate_expression(numbers, operators) == test_value:
                valid_equation = True
                break

        if valid_equation:
            total_calibration_result += test_value

    return total_calibration_result

with open("C:/Users/manue/Desktop/AdventOfCode2024/day_7/input.txt") as f:
    lines = f.read().splitlines()

result = solve_equations(lines)
print(result)
