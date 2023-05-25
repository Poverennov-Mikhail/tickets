count_tickets = int(input("Введите количество билетов: "))
prise = int()
for i in range(count_tickets):
    age_visitor = int(input("Введите возраст " + str(i+1)+" посетителя: "))
    if age_visitor in range(18,26):
         prise +=990
    if age_visitor > 25:
        prise += 1390
if count_tickets > 3:
    prise -= int(prise*0.1)
print("сумма к оплате: " + str(prise))