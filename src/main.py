"""
AI Calculator Starter Script
Author: Donggeon Lim

This is the first prototype of the AI calculator.
It simulates how the final device will work:

1. Capture image (placeholder for camera)
2. Extract text (future OCR step)
3. Send problem to AI model
4. Print solution
"""

# Temporary placeholder math problem
def capture_problem():
    print("Simulating camera capture...")
    return "Solve: 2x + 5 = 13"

# Simulated AI solving function
def solve_with_ai(problem_text):
    print("Sending problem to AI model...")
    
    # This is a placeholder for future OpenAI API integration
    if "2x + 5 = 13" in problem_text:
        return "x = 4"
    
    return "Solution not implemented yet."

def main():
    print("=== AI Calculator Prototype ===")
    
    problem = capture_problem()
    print(f"Captured problem: {problem}")
    
    solution = solve_with_ai(problem)
    print(f"AI Solution: {solution}")

if __name__ == "__main__":
    main()
