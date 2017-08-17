"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

def main():
    score = float(input("Enter score: "))
    print(score_calc(score))

def score_calc(score):
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score < 50:
        result = "Bad score"
    elif score < 90:
        result = "passable"
    else:
        result ="Excellent"
    return result

main()