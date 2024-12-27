def function_with_uncommon_error_solution(x):
    try:
        if x == 0:
            return 0
        return 1 / x
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None  # Or raise the exception

def function_that_raises_zerodivisionerror(x):
    return 1 / x

# Example usage:
result = function_with_uncommon_error_solution(0)
print(result)  # Output: 0
result2 = function_with_uncommon_error_solution(1)
print(result2) # Output: 1.0
result3 = function_with_uncommon_error_solution(0.0)
print(result3) #Output: None
result4 = function_that_raises_zerodivisionerror(0)
print(result4) #Raises ZeroDivisionError, as expected.