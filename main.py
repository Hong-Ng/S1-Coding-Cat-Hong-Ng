# simple intrest variables
pa = int(input("Enter the principal amount in $: "))
ir = int(input('Enter the intrest rate (enter 7% as 7): '))
irt = 'year'
#Compound interest variables
cpt = 'year' 
pt = int(input('Enter the amount of time to project into the future: '))
ptu = 'year'

SI = pa + ((pa*ir*pt)/100)
SI = round(SI,2)

CI = pa*(1+(ir/100))**pt
CI = round(CI,2)

print(f'After {pt} years your Simple Intrest account is at ${SI} and your Compound Intrest account is at ${CI}')