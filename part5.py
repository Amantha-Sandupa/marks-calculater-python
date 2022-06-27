# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.


# Student ID: w1839499

# Date: 2021/04/29


# add given data to the list following lists

pass_list = [120,100,100,80,60,40,20,20,20,0]
defer_list = [0,20,0,20,40,40,40,20,0,0]
fail_list = [0,0,20,20,20,40,60,80,100,120]

progress_count_list = 0  # this is for count the increment
module_trailer_count_list = 0
exclude_count_list = 0
do_not_progress_count_list = 0

x = 11
y = 0
while y<x:
    pass_credit = pass_list[y]
    defer_credit = defer_list[y]
    fail_credit = fail_list[y]

    if pass_credit == 120 and defer_credit == 0 and fail_credit == 0:
        print('Your Result - ', end='')
        print('Progress')
        progress_count_list = progress_count_list + 1

    elif pass_credit == 100 and defer_credit == 20 and fail_credit == 0:
        print('Your Result - ', end='')
        print('Progress (module trailer)')
        module_trailer_count_list = module_trailer_count_list + 1

    elif pass_credit == 100 and defer_credit == 0 and fail_credit == 20:
        print('Your Result - ', end='')
        print('Progress (module trailer)')
        module_trailer_count_list = module_trailer_count_list + 1

    elif fail_credit >= 80 and pass_credit <= 80:
        print('Your Result - ', end='')
        exclude_count_list += 1
        print('Exclude')

    elif pass_credit <= 80:
        print('Your Result - ', end='')
        print('Do not Progress – module retriever')
        do_not_progress_count_list = do_not_progress_count_list + 1
    y=y+1
# histogram

print("\nHorizontal Histogram")
print('Progress', progress_count_list, "                          - ", progress_count_list * "*")
print('Progress (module trailer)', module_trailer_count_list, "         - ", module_trailer_count_list * "*")
print('Do not Progress – module retriever', do_not_progress_count_list, "- ", do_not_progress_count_list * "*")
print('Exclude', exclude_count_list, "                           - ", exclude_count_list * "*")

# getting total outcomes
total_outcome = progress_count_list + module_trailer_count_list + do_not_progress_count_list + exclude_count_list

print("\n", total_outcome, " outcomes in total.")

