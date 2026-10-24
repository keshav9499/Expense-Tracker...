# Expense tracker Project
expenselist=[]# list of Expense dictionary...
print("welcome to Expense tracker")
while True:
    print("=======MENU=======")
    print(" 1. ===ADD EXPENSE===")
    print(" 2. ===VIEW ALL EXPENSE===")
    print(" 3. ===VIEW TOTAL EXPENSE===")
    print(" 4. ===EXIT===")

    choice =int(input("=====Please enter your choice: "))

      #IF(CHOICE==1):
      #ELIF(CHOICE==2):
      #ELIF(CHOICE==3):
      #ELIF(CHOICE==4):
      #ELSE("WRONG TRY AGAIN"):
#ADD EXPENSE 
    if(choice ==1):
            date=input("ON WHICH DATE  DID YOU MAKE EXPENSE:")
            category=input("WHICH TYPE OF EXPENSE LIKE travel, food, payments, rents other expense:")
            description=input("YOU CAN TYPE ABOUT YOUR EXPENSE:")
            amount=float(input("ENTER YOUR EXPENSE:"))
     
            expense={
                  "date":date,
                  "category":category,
                  "description":description,
                  "amount":amount,
                   
            }
            expenselist.append(expense)
            print("done bro, expense added succesfully")
            
# VIEW ALL EXPENSE
    if(choice ==2):
            if len(expenselist) ==0:
                  print("THERE IS NO EXPENSE WERE ADDED")
            else:
                  print("YOUR EXPENSE WAS")
            count=1
            for eachExpense in expenselist:
                  print(F" all expense{count}-> , {eachExpense['date']},{eachExpense['category']},{eachExpense['description']},{eachExpense['amount']}")
            count= count+1
# VIEW TOTAL EXPENSE
    elif choice == 3:
        total = 0
        for eachExpense in expenselist:
            total = total + eachExpense['amount']
        print(f"TOTAL EXPENSE SO FAR: {total}")

    # EXIT
    elif choice == 4:
        print("Thank you for using Expense Tracker! Bye bro!")
        break 
        # to break the loop

    else:
        print("WRONG TRY AGAIN")
