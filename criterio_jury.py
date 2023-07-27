def paresValues(k, polynomial_degree, polynomial):
    num_coefficients = polynomial_degree + 1
    dictionary_list = []
    j_coefficient_list = []
    line1 = polynomial
    line2 = polynomial[::-1]

    for x in range(num_coefficients):
        # Building the first dictionary/K
        if x == 0:
            dic = {
                "key1": line1,
                "key2": line2
            }
            # Add the dictionary to the list
            dictionary_list.append(dic)
            # Calculate the j-coefficient for the first dictionary/K
            try:
                j_coeff = line2[0] / line1[0]
            except ZeroDivisionError:
                print("Unstable System - Division by Zero!")
                break
                return dictionary_list, j_coefficient_list

            j_coefficient_list.append(abs(j_coeff))
        else:
            previous_line1 = dictionary_list[x - 1]["key1"]
            previous_line2 = dictionary_list[x - 1]["key2"]
            try:
                j_coeff = previous_line2[0] / previous_line1[0]
                line_1 = [previous_line1[i] - previous_line2[i] * j_coeff for i in range(len(previous_line1))]
            except ZeroDivisionError:
                print("Unstable System - Division by Zero!")
                break
                return dictionary_list, j_coefficient_list

            if line_1[-1] == 0:
                line_1.pop()
            line_2 = line_1[::-1]

            line_1_rounded = [round(value, 4) for value in line_1]
            line_2_rounded = [round(value, 4) for value in line_2]
            try:
                current_j_coeff = round(line_2_rounded[0] / line_1_rounded[0], 4)
                j_coefficient_list.append(abs(current_j_coeff))
            except ZeroDivisionError:
                print("Unstable System - Division by Zero!")
                break
                return dictionary_list, j_coefficient_list

            previous_line1 = line_1_rounded
            previous_line2 = line_2_rounded

            dic = {
                "key1": line_1_rounded,
                "key2": line_2_rounded
            }
            dictionary_list.append(dic)

            zero_count = 0
            for value in line_1_rounded:
                if value == 0:
                    zero_count += 1
            if zero_count == len(line_1_rounded):
                print("Unstable System - Zero Table! \n")
                break

        last_j_coefficient = j_coefficient_list[-1]
        if last_j_coefficient > 1:
            print(f"Unstable System - |J| = {last_j_coefficient} > 1 \n")
            break
    else:
        print(f"Stable System - |J| - {j_coefficient_list} < 1 \n")

    return dictionary_list, j_coefficient_list

# Data collection
def collect_data(polynomial_degree):
    num_coefficients = polynomial_degree + 1
    k = polynomial_degree
    count = 0
    polynomial = []
    while num_coefficients > count:
        coefficients = float(input("Enter coefficients: "))
        polynomial.append(coefficients)
        count += 1

    return polynomial, k

polynomial_degree = int(input("What is the polynomial degree? "))
polynomial, k = collect_data(polynomial_degree)
print(f"The coefficients are: {polynomial}, polynomial degree: {k} \n")

# Drawing the table
def FinalResult(dictionary_list, j_coefficient_list):
    for i, (dic, j_coeff) in enumerate(zip(dictionary_list, j_coefficient_list)):
        print(f"K {i }:")
        print(f"Line {2 * i + 1}: {dic['key1']}")
        print(f"Line {2 * i + 2}: {dic['key2']}")
        print(f"J-Coefficient {i}: {j_coeff}\n")

# Implementing the function and displaying the table
dictionary_list, j_coefficient_list = paresValues(k, polynomial_degree, polynomial)
FinalResult(dictionary_list, j_coefficient_list)
