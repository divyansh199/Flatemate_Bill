from flat import Bill, Flatmate
from reports import Pdfreport

amount = float(input("Enter the amount you want to pay: "))
period = input("what is the bill period? E.g: december 2020 ")

name1 = input("What is your name? ")
day_in_house1 = int(input(f"How many days do {name1} stay in house? "))

name2 = input("What is name of other flatemate? ")
day_in_house2 = int(input(f"How many days do {name2} stay in house? "))


the_bill = Bill(amount, period)

flatmate1 = Flatmate(name1, day_in_house1)
faltmate2 = Flatmate(name2, day_in_house2)

print(flatmate1.pays(the_bill,faltmate2))
print(faltmate2.pays(the_bill,flatmate1))

pdf_report = Pdfreport(f'{the_bill.period}.pdf')
pdf_report.generate(flatmate1,faltmate2,the_bill )


