import time

print("predict progression outcomes calculater")
#while done is fales this
done = False
while not done:
    try:# counting the increment
        pass_credit = int(input("Please enter your credits at pass - "))
        if pass_credit % 20 != 0 or pass_credit > 120:
            print("Out of range")
            continue
        defer_credit = int(input("Please enter your credits at defer - "))
        if defer_credit % 20 != 0 or defer_credit > 120:
            print("Out of range")
            continue
        fail_credit = int(input("Please enter your credits at fail - "))
        if fail_credit % 20 != 0 or fail_credit > 120:
            print("Out of range")
            continue
        if pass_credit + defer_credit + fail_credit > 120:
            print('Total incorrect')
            continue
    except ValueError:
        print("Intiger Requered")
        continue
    break

    
    ## calculation


if pass_credit == 120 and defer_credit == 0 and fail_credit == 0 :
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



