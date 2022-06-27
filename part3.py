print("Welcome to the Credit Calculator ")

progress_count = 0  # counting the increment
module_trailer_count = 0  # counting the increment
exclude_count = 0  # counting the increment
do_not_progress_count = 0  # counting the increment

done = False
while not done:
    try:
        # input credits from the user
        pass_credit = int(input("Please enter your credits at pass - "))
        if pass_credit % 20 != 0 or pass_credit > 120:
            print("Out of range")
            continue

        if pass_credit < 0:
            print("Input must be greater than 0")
            continue

        defer_credit = int(input("Please enter your credits at defer - "))
        if defer_credit % 20 != 0 or defer_credit > 120:
            print("Out of range")
            continue

        if defer_credit < 0:
            print("Input must be greater than 0")
            continue

        fail_credit = int(input("Please enter your credits at fail - "))
        if fail_credit % 20 != 0 or fail_credit > 120:
            print("Out of range")
            continue

        if fail_credit < 0:
            print("Input must be greater than 0")
            continue

        if pass_credit + defer_credit + fail_credit > 120:
            print('Total incorrect')
            continue

    except ValueError:
        print("Intiger Requered")
        continue


    # calculation

    if pass_credit == 120 and defer_credit == 0 and fail_credit == 0:
        print('Your Result - ', end='')
        print('Progress')
        progress_count = progress_count + 1

    elif pass_credit == 100 and defer_credit == 20 and fail_credit == 0:
        print('Your Result - ', end='')
        print('Progress (module trailer)')
        module_trailer_count = module_trailer_count + 1

    elif pass_credit == 100 and defer_credit == 0 and fail_credit == 20:
        print('Your Result - ', end='')
        print('Progress (module trailer)')
        module_trailer_count = module_trailer_count + 1

    elif fail_credit >= 80 and pass_credit <= 80:
        print('Your Result - ', end='')
        exclude_count += 1
        print('Exclude')

    elif pass_credit <= 80:
        print('Your Result - ', end='')
        print('Do not Progress – module retriever')
        do_not_progress_count = do_not_progress_count + 1

    # this is a exception handling
    elif pass_credit < 0 or defer_credit < 0 or fail_credit < 0:
        print("Inputs must be greater than 0")

    # loop of continue

    continue_var = input("Enter Y to continue Q to quit - ")
    while continue_var != "Y" or "y" or 'Q' or "q":
        if continue_var == "Y" or continue_var == "y":
            done = False
            break

        elif continue_var == "q" or continue_var == "Q":
            done = True
            break

        else:
            print("Input Error")
            continue_var = input("Enter Y to continue Q to quit - ")

# histogram

print("\nHorizontal Histogram")
print('Progress', progress_count, "                          - ", progress_count * "*")
print('Progress (module trailer)', module_trailer_count, "         - ", module_trailer_count * "*")
print('Do not Progress – module retriever', do_not_progress_count, "- ", do_not_progress_count * "*")
print('Exclude', exclude_count, "                           - ", exclude_count * "*")

# getting total outcomes
total_outcome = progress_count + module_trailer_count + do_not_progress_count + exclude_count

print("\n", total_outcome, " outcomes in total.")
