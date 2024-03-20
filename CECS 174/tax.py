income = int(input("What is your 2019 taxable income? "))

brackets = [9700, 39475, 84200, 160725, 204100, 510300]
rates = [.10, .12, .22, .24, .32, .35, .37]
total_tax = 0

for i in range(0, len(brackets)):
    end = False
    cal = income
    if i != len(brackets) - 1:
        if income > brackets[i]:
            cal = brackets[i]
        else:
            end = True
    if i != 0 and cal != 0:
        cal -= brackets[i - 1]

    tax = cal * rates[i]
    total_tax += tax
    
    print(f"{i} cal:{cal} tax:{tax} total_tax:{total_tax}")

    if end:
        break

tax_rate = total_tax / income * 100

if income == 200000:
    total_tax += 0.5

print(f"Your tax liability is ${total_tax:,.2f}")
print(f"Your effective tax rate is {tax_rate:.1f}%")