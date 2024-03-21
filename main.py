import math

def CompoundInterestCalc(P,r,it,ct,k,t):
    i = (r/(it/ct))/100
    A = P*((1+i)**(k*t))
    A = round(A,2)
    return A

def SimpleInterestCalc(P,r,it,kt,t):
    i = r/100
    A = P*i*((kt/it)*t) + P
    return A

def Mod1():
    print('==========Module 1==========')
    print('-----Simple Interest-----')
    P = int(input('Enter starting amount: '))
    r = int(input('Enter interest rate: '))
    it = input('Enter the interest rate time unit: ')
    it = TimePeriod[it.lower()]

    SimpleInterest["principal"] = P
    SimpleInterest["interest"] = r
    SimpleInterest['irt'] = it
    #Compound interest variables 
    print('-----Compound Interest-----')
    P = int(input('Enter starting amount: '))
    r = int(input('Enter interest rate: '))
    it = input('Enter the interest rate time unit: ')
    it = TimePeriod[it.lower()]
    ct = input('Enter compounding time period: ')
    
    if ct == 'custom':
        ct = int(input('Enter the number of compounding periods per interest rate time unit: '))
        ct = it/ct
    else:
        ct = TimePeriod[ct.lower()]
        
    CompoundInterest["principal"] = P
    CompoundInterest["interest"] = r
    CompoundInterest['irt'] = it

    print("-----Future Projection Timeframes-----")
    t = int(input('Enter amount of time to project into the future: '))
    kt = input('Enter projection time unit: ')
    time = kt
    kt = TimePeriod[kt.lower()]
    k = kt/ct
        
    try: 
        SimpleInterest['amount'] = SimpleInterestCalc(SimpleInterest['principal'],SimpleInterest['interest'],SimpleInterest['irt'],kt,t)
    except OverflowError:
        print('An Overflow Error has occured. You will be sent back to the home screen, please try changing the inputs to ensure this does not happen again.')
        print('Please feel free to feedback by calling 000 and telling them the code word "Im dying".')
        SimpleInterest['amount'] = 'ERROR'
    try:
        CompoundInterest['amount'] = CompoundInterestCalc(CompoundInterest['principal'],CompoundInterest['interest'],CompoundInterest['irt'],ct,k,t)
    except OverflowError:
        print('An Overflow Error has occured. You will be sent back to the home screen, please try changing the inputs to ensure this does not happen again.')
        print('Please feel free to feedback by calling 000 and telling them the code word "Im dying".')
        CompoundInterest['amount'] = 'ERROR'


    print("========================================================= Perth Modern School Bank =========================================================")       


    print(f'----- {t} {time}s later ------')
    print (f'Simple Interest Account Balance: {SimpleInterest["amount"]}')
    print(f'Compound Interest Account Balance: {CompoundInterest["amount"]}')
    
def Mod2():
    print("=====Module 2=====")
    P = int(input('Enter starting amount: '))
    r = int(input('Enter interest rate: '))
    it = input('Enter the interest rate time unit: ')
    it = TimePeriod[it.lower()]
    ct = input('Enter compounding time period: ')
    time = ct
    ct = TimePeriod[ct.lower()]
    ta = float(input('Please enter your target amount: '))
    CompoundInterest["principal"] = P
    CompoundInterest["interest"] = r
    CompoundInterest['irt'] = it
    CompoundInterest['amount'] = CompoundInterest['principal']
    period = 1
    Projection = []
    while CompoundInterest['amount'] < ta:
        Projection.append(CompoundInterest['amount'])
        try:
            CompoundInterest['amount'] = CompoundInterestCalc(CompoundInterest['principal'],CompoundInterest['interest'],CompoundInterest['irt'],ct,period,1)
            period = period + 1
        except OverflowError:
            print('An Overflow Error has occured. You will be sent back to the home screen, please try changing the inputs to ensure this does not happen again.')
            print('Please feel free to feedback by calling 000 and telling them the code word "Im dying".')
            CompoundInterest['amount'] = 'ERROR'
            
    Projection.append(CompoundInterest['amount'])       
    print(f"After {period-1} compounding periods your account has reached ${CompoundInterest['amount']}") 
    print(f'Forward Projection: {Projection}')
    print(f'Time Taken: {period-1} compounding periods\n')

def Mod3():
    print('=====Module 3=====')
    print('ACCOUNT 1')
    P = int(input('Enter starting amount: '))
    r = int(input('Enter interest rate: '))
    it = input('Enter the interest rate time unit: ')
    it = TimePeriod[it.lower()]
    ct = input('Enter compounding time period: ')
    time = ct
    ct = TimePeriod[ct.lower()]
    CompoundInterest["principal"] = P
    CompoundInterest["interest"] = r
    CompoundInterest['irt'] = it
    CompoundInterest['amount'] = CompoundInterest['principal']

    print(f"-----Future Projection Timeframe for Account 1-----")
    t = int(input('Enter amount of time to project into the future: '))
    kt = input('Enter projection time unit: ')
    time = kt
    kt = TimePeriod[kt.lower()]
    k = kt/ct
    Projection = []
    try:
        CompoundInterest['amount'] = CompoundInterestCalc(CompoundInterest['principal'],CompoundInterest['interest'],CompoundInterest['irt'],ct,k,t)
    except OverflowError:
        print('An Overflow Error has occured. You will be sent back to the home screen, please try changing the inputs to ensure this does not happen again.')
        print('Please feel free to feedback by calling 000 and telling them the code word "Im dying".')
        CompoundInterest['amount'] = 'ERROR'
##############################################################
    print('ACCOUNT 2')
    P = int(input('Enter starting amount: '))
    r = int(input('Enter interest rate: '))
    it = input('Enter the interest rate time unit: ')
    it = TimePeriod[it.lower()]
    ct = input('Enter compounding time period: ')
    time = ct
    ct = TimePeriod[ct.lower()]
    CompoundInterest2["principal"] = P
    CompoundInterest2["interest"] = r
    CompoundInterest2['irt'] = it
    CompoundInterest2['amount'] = CompoundInterest['principal']
    CompoundInterest2["principal"] = P
    CompoundInterest2["interest"] = r
    CompoundInterest2['irt'] = it

    print(f"-----Future Projection Timeframe for Account 2-----")
    t = int(input('Enter amount of time to project into the future: '))
    kt = input('Enter projection time unit: ')
    time = kt
    kt = TimePeriod[kt.lower()]
    k = kt/ct
    Projection = []
    try:
        CompoundInterest2['amount'] = CompoundInterestCalc(CompoundInterest2['principal'],CompoundInterest2['interest'],CompoundInterest2['irt'],ct,k,t)
    except OverflowError:
        print('An Overflow Error has occured. You will be sent back to the home screen, please try changing the inputs to ensure this does not happen again.')
        print('Please feel free to feedback by calling 000 and telling them the code word "Im dying".')
        CompoundInterest2['amount'] = 'ERROR'
    
    print('===== Results =====')
    print(f'Account 1 Balance: {CompoundInterest["amount"]}')
    print(f'Account 2 Balance: {CompoundInterest2["amount"]}')

def Mod4():
    print("=====Module 4=====")
    P = int(input('Enter starting amount: '))
    r = int(input('Enter interest rate: '))
    it = input('Enter the interest rate time unit: ')
    it = TimePeriod[it.lower()]
    ct = input('Enter compounding time period: ')
    ct = TimePeriod[ct.lower()]
    CompoundInterest["principal"] = P
    CompoundInterest["interest"] = r
    CompoundInterest['irt'] = it
    CompoundInterest['amount'] = CompoundInterest['principal']
    period = 1
    Projection = []
    ta = float(input('Please enter your target amount: '))
    if ta == 0:
        t = int(input('In that case,Enter amount of time to project into the future: '))
        kt = input('Enter projection time unit: ')
        deposit = int(input('Enter the regular deposit per compounding period: '))
        kt = TimePeriod[kt.lower()]
        k = kt/ct
        while period <= (t*k):
            Projection.append(CompoundInterest['amount'])
            try:
                CompoundInterest['amount'] = CompoundInterestCalc(CompoundInterest['amount'],CompoundInterest['interest'],CompoundInterest['irt'],ct,1,1)
                period = period + 1
                CompoundInterest['amount'] = CompoundInterest['amount'] + deposit
            except OverflowError:
                print('An Overflow Error has occured. You will be sent back to the home screen, please try changing the inputs to ensure this does not happen again.')
                print('Please feel free to feedback by calling 000 and telling them the code word "Im dying".')
                CompoundInterest['amount'] = 'ERROR'
    else:
        deposit = int(input('Enter the regular deposit per compounding period: '))
        while CompoundInterest['amount'] < ta:
            Projection.append(CompoundInterest['amount'])
            try:
                CompoundInterest['amount'] = CompoundInterestCalc(CompoundInterest['amount'],CompoundInterest['interest'],CompoundInterest['irt'],ct,1,1)
                period = period + 1 
                CompoundInterest['amount'] = CompoundInterest['amount'] + deposit
                print(CompoundInterest['amount'])
            except OverflowError:
                print('An Overflow Error has occured. You will be sent back to the home screen, please try changing the inputs to ensure this does not happen again.')
                print('Please feel free to feedback by calling 000 and telling them the code word "Im dying".')
                CompoundInterest['amount'] = 'ERROR'
            
    Projection.append(CompoundInterest['amount'])       
    print(f"After {period-1} compounding periods your account has reached ${CompoundInterest['amount']}") 
    print(f'Forward Projection: {Projection}')
    print(f'Time Taken: {period-1} compounding periods\n')

def Mod5():
    P = 1000
    print('Starting Amount: $1000')
    r = 100
    it = 'year'
    print('Interest Rate: 100% per annum')
    it = TimePeriod[it.lower()]
    ct = input('Enter compounding time period (quarter,month,week,day,hour,10min): ')
    time = ct
    ct = TimePeriod[ct.lower()]
    CompoundInterest["principal"] = P
    CompoundInterest["interest"] = r
    CompoundInterest['irt'] = it
    CompoundInterest['amount'] = CompoundInterest['principal']
    kt = TimePeriod['year']
    k = kt/ct
    try:
        CompoundInterest['amount'] = CompoundInterestCalc(CompoundInterest['principal'],CompoundInterest['interest'],CompoundInterest['irt'],ct,k,1)
    except OverflowError:
        print('An Overflow Error has occured. You will be sent back to the home screen, please try changing the inputs to ensure this does not happen again.')
        print('Please feel free to feedback by calling 000 and telling them the code word "Im dying".')
        CompoundInterest['amount'] = 'ERROR'
    print('===== 1 Year Later =====')
    print(f'Amount Owed: {CompoundInterest["amount"]}\n')
    
SimpleInterest = {
    
}
CompoundInterest = {
    
}
CompoundInterest2= {
    
}
TimePeriod = {
    'year': 365,
    'quarter': 91.25,
    'month': 30.4167,
    'week': 7,
    'day': 1,
    'hour': 1/24,
    '10min': 1/(24*6),
    '1min': 1/(24*60),
    '1sec': 1/(24*60*60)
} 

print('==============================')
print('==========Welcome to==========')
print('===========The Bank===========')
print('============Of Mod============')
print('==============================')
while True:
    print('Welcome to the Bank Of Mod, what would you like to do (Type "1" for Comparing Simple and Compound Interest)')
    print('1: Comparing Compound and Simple Interest accounts')
    print('2: Time for a Compound Account to reach a target')
    print('3: Comparing 2 Compound Accounts')
    print('4: Regular Deposit Modeling')
    print('5: Simulate Increase in Compounding Frequency')
    print('0: Exit')
    menu = int(input('Type 1, 2, 3, 4 or 5 to activate the corrresponding program. Type 0 to end the program: '))
    if menu == 0:
        print('Exit.exe Failed, Ending Program')
        break
    elif menu == 1:
        print()
        Mod1()
    elif menu == 2:
        print()
        Mod2()
    elif menu == 3:
        print()
        Mod3()
    elif menu == 4:
        print()
        Mod4()
    elif menu == 5:
        print()
        Mod5()