# Jury Stability Test
This code apply jury stability test in a polynomial of order N.

This code wasdeveloped using Python and your basics data structures.

I slice the code in three functions:
1 - collect_data:
using a loop while, the function get a polynominal degree and coefficients of polynomial.

2 - FinalResult:
Show the final result, where K contain double lines, each line contain your polynominal coefficients and your respective "J" coefficient.

3 - paresValues:
This is a main function.
Creat a dictionaty for each two lines, the first line contain the polynominal coefficients and second line is your inverse.
Each dictionary is append in dictionary_list.
For each two lines, calculate a "J coefficient" for stability test and append in a j_coefficient_list.
If any Stop criterious is true, the code break and show a final table.
