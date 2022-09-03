# KillerSudokuSolver
killer sudoku solver

# Note: Using solver will make you lose your enjoyment of sudoku !!!

![example.png]("example.png")

1. Modified the rules.tsv
    * No overlapped rules support
    * row & colum, sum
    * e.g., [1,1] + [1,2] = 8 
    * 11,12,8
    * Currently rules.csv corresponds to example.png
2. Check that rules are correct: python checkRules.py
3. Run solver: python killerSudokuSolver.py

Thoughts:

The principle behind the design of the script is simple. It just specifies a lot of rules, including that rows and columns cannot be repeated, the sum is 45, that each cell is excluded from possible numbers, etc.

It feels like writing this script is like playing with Lego. I had fun putting it together, excitedly took a picture  when it was finished and showed it to my friends, and then threw it in the corner. I don't feel like I've had as much fun so far as I did when I first played killer sudoku :(.

So, use this script with caution. Cheers.
