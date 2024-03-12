def CompoundInterestCalc(pa,ir,cpt,pt,ptu):

    amount = pa*(1+(ir/(100*cpt)))**(cpt*pt)
    amount = round(amount,2)
    return amount

def SimpleInterestCalc(pa,ir,cpt,pt,ptu):
    
    amount = pa + (((pa*(ir/cpt)*(pt*cpt))/100))
    amount = round(amount,2)
    return amount

SimpleInterest = {
    
}

CompoundInterest = {
    
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

# simple interest variables
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
cpt = input('Enter the intrest rate time unit (Year, Quarter, Month, Week, Day): ')
cpt = cpt.lower()
cpt = TimePeriodYr[cpt]

CompoundInterest["principal"] = pa
CompoundInterest["interest"] = ir
CompoundInterest['irt'] = cpt

print("-----Future Projection Timeframes-----")
pt = int(input('Enter the amount of time to project into the future: '))
ptu = 'year'

SimpleInterest['amount'] = SimpleInterestCalc(SimpleInterest['principal'],SimpleInterest['interest'],SimpleInterest['irt'],pt,ptu)

CompoundInterest['amount'] = CompoundInterestCalc(CompoundInterest['principal'],CompoundInterest['interest'],CompoundInterest['irt'],pt,ptu)


print("========================================================= Perth Modern School Bank =========================================================")       


print(f'----- {pt} {ptu}s later ------')
print (f'Simple Interest Account Balance: {SimpleInterest["amount"]}')
print(f'Compound Interest Account Balance: {CompoundInterest["amount"]}')