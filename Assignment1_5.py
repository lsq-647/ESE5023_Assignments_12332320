# 5. Dynamic programming
# 5.1
def Find_expression(target):
    solutions = []

    def backtrack(expression, current_sum, next_digit, sign):
        if next_digit > 9:
            if current_sum == target:
                solutions.append(expression)
            return

        # Join next_digit with the previous digit to form a bigger number
        num = int(str(next_digit-1) + str(next_digit))
        next_digit += 1

        # Case 1: Add the number to the current sum
        backtrack(expression + '+' + str(num), current_sum + num, next_digit, '+')

        # Case 2: Subtract the number from the current sum
        backtrack(expression + '-' + str(num), current_sum - num, next_digit, '-')

    backtrack('1', 1, 2, '+')

    # Print all the solutions
    for solution in solutions:
        print(solution + '=' + str(target))

    return solutions


# Find all solutions for the expression to evaluate to 50
Find_expression(50)

#5.2
import matplotlib.pyplot as plt

def Count_solutions():
    Total_solutions = []

    for i in range(1, 101):
        solutions = Find_expression(i)
        count = len(solutions)
        Total_solutions.append(count)

    # Plotting the Total_solutions list
    numbers = list(range(1, 101))
    plt.plot(numbers, Total_solutions)
    plt.xlabel('Number')
    plt.ylabel('Total Solutions')
    plt.title('Count of Suitable Solutions for each Number')
    plt.show()

    min_solutions = min(Total_solutions)
    max_solutions = max(Total_solutions)
    min_number = numbers[Total_solutions.index(min_solutions)]
    max_number = numbers[Total_solutions.index(max_solutions)]

    print(f"Number(s) yielding the minimum solutions: {min_number}")
    print(f"Number(s) yielding the maximum solutions: {max_number}")

# Count solutions and plot the Total_solutions list
Count_solutions()








