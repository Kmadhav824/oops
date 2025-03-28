account={'name':'Rama','accno':1001,'balance':20000,'transaction':[]}
while True:
    print('1. Check Balance')
    print('2. Deposit')
    print('3. Withdraw')
    print('4. Transaction')
    print('5. Exit')
    choice=int(input('Enter your choice: '))

    match choice:
        case 1:
            print(f'Your account number is {account["accno"]} and your balace is {account["balance"]}')
        case 2:
            deposit=float(input('Enter the amount to deposit: '))
            account['balance']+=deposit
            account['transaction'].append(f'{deposit} deposited')
            print(f'deposit of {deposit} is successful . Your current balance is {account["balance"]}')
        case 3:
            withdraw=float(input('Enter the amount to withdraw: '))
            if(withdraw>account['balance']):
                print('Insufficient balance')
            else:
                    account['balance']-=withdraw
                    print(f'withdrawal of {withdraw} is successful and your current balance is {account["balance"]}')
                    account['transaction'].append(f'{withdraw} withdrawn')
        case 4:
              print('You have the following transacitons')
              for i in range(len(account['transaction'])):
                  print(account['transaction'][i])
        case 5:
              break
            

