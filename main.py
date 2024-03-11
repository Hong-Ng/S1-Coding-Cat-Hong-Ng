def IntrestCalc(pa,ir,SIcpt,CIcpt,pt,ptu):
    SI = pa + (((pa*ir*pt)/100)*(pt*SIcpt))
    SI = round(SI,2)

    CI = pa*(1+(ir/(100*CIcpt)))**(CIcpt*pt)
    CI = round(CI,2)
    return SI, CI

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
SIcpt = input('Enter the intrest rate time unit (Year, Quater, Month, Week, Day): ')
SIcpt = SIcpt.lower()
SIcpt = TimePeriodYr[SIcpt]
print (SIcpt)

SimpleIntrest = IntrestCalc(pa,ir,SIcpt,CIcpt,pt,ptu)

#Compound interest variables
print('-----Compound Interest-----')
pa = float(input("Enter the principal amount in $: "))
ir = float(input('Enter the interest rate (enter 7% as 7): '))
CIcpt = input('Enter the intrest rate time unit (Year, Quater, Month, Week, Day): ')
CIcpt = CIcpt.lower()
CIcpt = TimePeriodYr[CIcpt]
print (CIcpt)

CompoundIntrest = IntrestCalc(pa,ir,SIcpt,CIcpt,pt,ptu)

print("-----Future Projection Timeframes-----")
pt = int(input('Enter the amount of time to project into the future: '))
ptu = 'year'


print(f'After {pt} {ptu} your Simple Interest account is at ${SimpleIntrest} and your Compound Interest account is at ${CompoundIntrest}')