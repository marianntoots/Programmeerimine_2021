from datetime import datetime, timedelta

date_format = "%d.%m.%Y"

print("Laenukalkulaator")


amount = None
while amount is None:
    try:
        amount = int(input("laenusumma (täisarv): "))
        if amount <= 0:
            print("Sisestatud väärtus peab olema suurem kui 0")
            amount = None
    except ValueError:
        print("Kontrolli sisestatud väärtust")

laenuperiood_aastates = None
while laenuperiood_aastates is None:
    try:
        laenuperiood_aastates = int(input("laenuperiood aastates (täisarv): "))
        if laenuperiood_aastates <= 0:
            print("Sisestatud väärtus peab olema suurem kui 0")
            laenuperiood_aastates = None
    except ValueError:
        print("Kontrolli sisestatud väärtust")

intressi_protsent = None
while intressi_protsent is None:
    try:
        intressi_protsent = float(input("intressi protsent (ujukomaarv): "))
        if intressi_protsent < 0:
            print("Sisestatud intressi protsent peab olema positiivne")
    except ValueError:
        print("Kontrolli sisestatud väärtust")

maksegraafik = None
while maksegraafik not in ("a", "p"):
    maksegraafik = input("tagasimaksegraafiku tüüp  a) annuiteet; p) võrdsed põhiosad: ")
    if maksegraafik not in ("a", "p"):
        print("Kontrolli sisestatud väärtust (a või p)")

start_date = None
while start_date is None:
    start_date_str = input("maksete alguskuupäev (pp.kk.aaaa): ")
    try:
        start_date = datetime.strptime(start_date_str, date_format)
    except ValueError:
        print("Sisesta kuupäevad õiges vormingus")

amount_left = amount
payment_date = start_date
print("Maksekuupäev\tJääk\t\tPõhiosa tagasimakse\tIntressimakse\tKokku")

payment_i = 0
total_payment_per_month = 0
main_payment = 0
if maksegraafik == "a":
    total_payment_per_month = amount/(
            (1 - 1/(1+intressi_protsent/100/12)**(laenuperiood_aastates*12))/(intressi_protsent/100/12)
    )
else:
    main_payment = amount / (12 * laenuperiood_aastates)
while amount_left > 0.001:
    payment_month = start_date.month + payment_i
    payment_year = start_date.year + (payment_month - 1) // 12
    payment_month = (payment_month - 1) % 12 + 1
    days_in_month = (datetime(payment_year + (payment_month // 12), payment_month % 12 + 1, 1) -
                     datetime(payment_year, payment_month, 1)).days
    payment_day = min(days_in_month, start_date.day)
    payment_date = datetime(payment_year, payment_month, payment_day)

    interest_payment = amount_left * (intressi_protsent / 100 / 12)
    if maksegraafik == "a":
        main_payment = total_payment_per_month - interest_payment
    else:
        total_payment_per_month = main_payment + interest_payment
    print("{}\t{:9.2f}\t{:.2f}\t\t\t{:.2f}\t\t{:.2f}".format(
        payment_date.strftime(date_format),
        amount_left,
        main_payment,
        interest_payment,
        total_payment_per_month
    ))
    amount_left -= main_payment
    payment_i += 1
