import time
print("predict progression outcomes calculater")
#getting inputs from the user
pass_credit = int(input("Please enter your credits at pass - "))
defer_credit = int(input("Please enter your credits at defer - "))
fail_credit = int(input("Please enter your credits at fail - "))
       
    
    ## calculation


if pass_credit == 120 and defer_credit == 00 and fail_credit == 0 :
    print('Your Result - ',end ='')
    time.sleep(1)
    print('Progress')
elif pass_credit == 100 and defer_credit == 20 and fail_credit == 0 :
    print('Your Result - ',end ='')
    time.sleep(1)
    print ('Progress (module trailer)')
elif pass_credit == 100 and defer_credit == 0 and fail_credit == 20 :
    print('Your Result - ',end ='')
    time.sleep(1)
    print('Progress (module trailer)')
elif fail_credit>= 80 and pass_credit<=80 :
    print('Your Result - ',end ='')
    time.sleep(1)
    print ('Exclude')
elif pass_credit<= 80:
    print('Your Result - ',end ='')
    time.sleep(1)
    print ('Do not Progress – module retriever')


