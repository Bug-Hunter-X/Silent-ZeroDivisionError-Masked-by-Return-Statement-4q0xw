# Silent ZeroDivisionError in Python

This repository demonstrates a subtle bug in Python where a `ZeroDivisionError` is masked by an early `return` statement within a function.  The unexpected behavior can make debugging difficult.

## Bug Description
The `bug.py` file contains a function that attempts to handle a potential `ZeroDivisionError`. However, the way it's handled causes the error to go unnoticed, leading to incorrect results. The solution is to properly handle or propagate the exception rather than silently ignoring it. 

## How to Reproduce
1. Clone this repository.
2. Run `bug.py`.
3. Observe the unexpected output and the lack of any error messages despite the division by zero.  Compare this to the behavior of the `function_that_raises_zerodivisionerror` function. 

## Solution
The `bugSolution.py` file demonstrates the corrected code. It explicitly handles the `ZeroDivisionError` using a `try-except` block, allowing for proper error reporting and handling.