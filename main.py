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
    pa = float(input("Enter the principal amount in $: "))
    ir = float(input('Enter the interest rate (enter 7% as 7): '))
    irt = 1
    ta = float(input('Please enter your target amount: '))
    CompoundInterest["principal"] = pa
    CompoundInterest["interest"] = ir
    CompoundInterest['irt'] = irt
    ptu = 'year'
    time = ptu
    ptu = 1
    while year <= ta:
        try:
            CompoundInterest['amount'] = round(CompoundInterestCalc(CompoundInterest['principal'],CompoundInterest['interest'],CompoundInterest['irt'],year,ptu),2)
            year = year + 1
            Projection["Year", year] = CompoundInterest['amount']
        except OverflowError:
            print('An Overflow Error has occured. You will be sent back to the home screen, please try changing the inputs to ensure this does not happen again.')
            print('Please feel free to feedback by calling 000 and telling them the code word "Im dying".')
            CompoundInterest['amount'] = 'ERROR'
            
    print(f"After {year} year(s) you're account has reached ${CompoundInterest['amount']}") 
    print(f'Forward Projection: {Projection}')
    print(f'Time Taken: {year} {time}')

SimpleInterest = {
    
}

CompoundInterest = {
    
}

Projection = {
    
}

TimePeriod = {
    'yearly': 365,
    'quarterly': 91.25,
    'monthly': 30.4167,
    'weekly': 7,
    'daily': 1
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
    print('0: Exit')
    menu = int(input('Type 1 or 2 to activate the corrresponding program. Type 0 to end the program: '))
    if menu == 0:
        print('Exit.exe Failed, Ending Program')
        break
    elif menu == 1:
        Mod1()
    elif menu == 2:
        Mod2()