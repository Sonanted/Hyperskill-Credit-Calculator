import argparse
import math


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--type')
    parser.add_argument('--principal', type=float)
    parser.add_argument('--payment', type=float)
    parser.add_argument('--periods', type=int)
    parser.add_argument('--interest', type=float)
    arguments = parser.parse_args()
    return arguments


def count_none(array):
    none = 0
    for element in array:
        if element is None:
            none += 1
    return none


def differentiated_payments(name):
    i = name.interest / 1200
    total = 0
    for month in range(name.periods):
        d = name.principal / name.periods + i * (name.principal - name.principal * month / name.periods)
        total += math.ceil(d)
        print(f'Month {month + 1}: paid out {math.ceil(d)}')
    print(f'Overpayment = {round(total - name.principal)}')


def annuity_payment(name):
    i = name.interest / 1200
    payment = name.principal * i * (1 + i) ** name.periods / ((1 + i) ** name.periods - 1)
    total = math.ceil(payment) * name.periods
    print(f'Your annuity payment = {math.ceil(payment)}!')
    print(f'Overpayment = {round(total - name.principal)}')


def annuity_principal(name):
    i = name.interest / 1200
    principal = name.payment / ((i * (1 + i) ** name.periods) / ((1 + i) ** name.periods - 1))
    total = name.payment * name.periods
    print(f'Your credit principal = {math.floor(principal)}')
    print(f'Overpayment = {math.ceil(total - principal)}')


def count_of_months(name):
    i = name.interest / 1200
    months = math.ceil(math.log(name.payment / (name.payment - i * name.principal), i + 1))
    total = name.payment * months
    if months % 12 == 0:
        if months // 12 == 1:
            print(f'You need {months // 12} year to repay this credit!')
        else:
            print(f'You need {months // 12} years to repay this credit!')
    elif months // 12 == 0:
        if months % 12 == 1:
            print(f'You need {months % 12} month to repay this credit!')
        else:
            print(f'You need {months % 12} months to repay this credit!')
    else:
        if months // 12 == 1 and months % 12 == 1:
            print(f'You need {months // 12} year and {months % 12} month to repay this credit!')
        elif months // 12 == 1 and months % 12 != 1:
            print(f'You need {months // 12} year and {months % 12} months to repay this credit!')
        elif months // 12 != 1 and months % 12 == 1:
            print(f'You need {months // 12} years and {months % 12} month to repay this credit!')
        else:
            print(f'You need {months // 12} years and {months % 12} months to repay this credit!')
    print(f'Overpayment = {round(total - name.principal)}')


args = parse()
elements = [args.type, args.principal, args.payment, args.periods, args.interest]
none_elements = count_none(elements)
if none_elements >= 2:
    print('Incorrect parameters')
elif args.periods is not None and args.periods <= 0:
    print('Incorrect parameters')
elif args.payment is not None and args.payment <= 0:
    print('Incorrect parameters')
elif args.principal is not None and args.principal <= 0:
    print('Incorrect parameters')
elif args.interest is not None and args.interest <= 0:
    print('Incorrect parameters')
else:
    if args.type == 'diff':
        if args.principal is None:
            pass
        if args.payment is None:
            differentiated_payments(args)
    elif args.type == 'annuity':
        if args.payment is None:
            annuity_payment(args)
        if args.principal is None:
            annuity_principal(args)
        if args.periods is None:
            count_of_months(args)
    else:
        print('Incorrect parameters')
