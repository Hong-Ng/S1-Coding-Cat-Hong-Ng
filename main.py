import math

def CompoundInterestCalc(pa,ir,cpt,pt,ptu):
    pt = pt/ptu
    amount = pa*(1+(ir/(100*cpt)))**(cpt*pt)
    amount = round(amount,2)
    return amount

def SimpleInterestCalc(pa,ir,cpt,pt,ptu):
    pt = pt/ptu
    amount = pa + (((pa*(ir/cpt)*(pt*cpt))/100))
    amount = round(amount,2)
    return amount

def Mod1():
    print('==========Module 1==========')
    print('-----Simple Interest-----')
    pa = float(input("Enter the principal amount in $: "))
    ir = float(input('Enter the interest rate (enter 7% as 7): '))
    cpt = input('Enter the intrest rate time unit (Year, Quarter, Month, Week, Day): ')
    cpt = cpt.lower()
    cpt = TimePeriodYr[cpt]

    SimpleInterest["principal"] = pa
    SimpleInterest["interest"] = ir
    SimpleInterest['irt'] = cpt
    #Compound interest variables
    print('-----Compound Interest-----')
    pa = float(input("Enter the principal amount in $: "))
    ir = float(input('Enter the interest rate (enter 7% as 7): '))
    cpt = input('Enter the intrest rate time unit (Year, Quarter, Month, Week, Day, Custom): ')
    cpt = cpt.lower()
    if cpt == 'custom':
        cpt = int(input('Enter the number of compounding time periods per chosen time unit: '))
    else:
        cpt = TimePeriodYr[cpt]

    CompoundInterest["principal"] = pa
    CompoundInterest["interest"] = ir
    CompoundInterest['irt'] = cpt

    print("-----Future Projection Timeframes-----")
    pt = int(input('Enter the amount of time to project into the future: '))
    ptu = input('Enter the projection time unit (Year, Quarter, Month, Week, Day): ')
    ptu = ptu.lower()
    ptu = TimePeriodYr[ptu]
        
    try:
        SimpleInterest['amount'] = SimpleInterestCalc(SimpleInterest['principal'],SimpleInterest['interest'],SimpleInterest['irt'],pt,ptu)
    except OverflowError:
        print('An Overflow Error has occured. You will be sent back to the home screen, please try changing the inputs to ensure this does not happen again.')
        print('Please feel free to feedback by calling 000 and telling them the code word "Im dying".')
        CompoundInterest['amount'] = 'ERROR'
    try:
        CompoundInterest['amount'] = CompoundInterestCalc(CompoundInterest['principal'],CompoundInterest['interest'],CompoundInterest['irt'],pt,ptu)
    except OverflowError:
        print('An Overflow Error has occured. You will be sent back to the home screen, please try changing the inputs to ensure this does not happen again.')
        print('Please feel free to feedback by calling 000 and telling them the code word "Im dying".')
        CompoundInterest['amount'] = 'ERROR'


    print("========================================================= Perth Modern School Bank =========================================================")       


    print(f'----- {pt} {ptu}s later ------')
    print (f'Simple Interest Account Balance: {SimpleInterest["amount"]}')
    print(f'Compound Interest Account Balance: {CompoundInterest["amount"]}')
    
def Mod2():
    print("=====Module 2=====")
    pa = float(input("Enter the principal amount in $: "))
    ir = float(input('Enter the interest rate (enter 7% as 7): '))
    cpt = input('Enter the intrest rate time unit (Year, Quarter, Month, Week, Day, Custom): ')
    cpt = cpt.lower()
    time = cpt
    if cpt == 'custom':
        cpt = int(input('Enter the number of compounding time periods per chosen time unit: '))
    else:
        cpt = TimePeriodYr[cpt]
    ptu = input('Enter the projection time unit (Year, Quarter, Month, Week, Day): ')
    ptu = ptu.lower()
    ptu = TimePeriodYr[ptu]
    ta = float(input('Please enter your target amount: '))
    CompoundInterest["principal"] = pa
    CompoundInterest["interest"] = ir
    CompoundInterest['irt'] = cpt
    year = 1
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

TimePeriodYr = {
    'year': 1,
    'quarter': 4,
    'month': 12,
    'week': 52,
    'day': 365
}

TimePeriodsMth = {
    'week': 4,
    'day': 30
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
    menu = int(input())
    if menu == 0:
        print('Exit.exe Failed, Ending Program')
        break
    elif menu == 1:
        Mod1()
    elif menu == 2:
        Mod2()