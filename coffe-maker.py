quarter = 0.25
nickel= 0.05
penny= 0.01
dime= 0.10
cost_of_cappuccino = 3
cost_of_latte = 2.5
cost_of_expresso = 1.5
t= 1

resources ={
    'milk': 500,
    'water': 500,
    'coffee' : 200,
}


def modify(choice,milk,water,coffee):
    if choice == 'cappuccino':
        resources['milk'] = milk-100
        resources['coffee'] = coffee-24
        resources['water'] = water-250
    if choice == 'latte':
        resources['milk'] = milk - 150
        resources['coffee'] = coffee - 24
        resources['water'] = water - 200
    if choice == 'expresso':
        resources['coffee'] = coffee -18
        resources['water'] = water - 100


def report():
    return f'{resources["milk"]}ml milk and {resources["water"]}ml water and {resources["coffee"]}grams coffee'


def is_available(choice):
    if choice == 'cappuccino':
        if resources['milk']-100>=0 and resources['water']-250>=0 and resources['coffee']-24>=0:
            return 1
        else:
            return 0
    elif choice == 'latte':
        if resources['milk']-150>=0 and resources['water']-200>=0 and resources['coffee']-24>=0:
            return 1
        else:
            return 0
    elif choice == 'expresso':
        if resources['milk']-0>=0 and resources['water']-100>=0 and resources['coffee']-18>=0:
            return 1
        else:
            return 0


def is_sufficient(q,d,n,p,choice):
    total = q*0.25 + d*0.1 + n*0.05 + p*0.01
    if choice == 'cappuccino':
        if total > cost_of_cappuccino:
            print(f'Your change is {total- cost_of_cappuccino}')
            print(f'You can have your {choice}')
            return 1
        elif total == cost_of_cappuccino:
            print(f'You can have your {choice}')
            return 1
        else:
            print('amount you entered is low your amount is refunded ')
            return 0
    if choice == 'latte':
        if total > cost_of_latte:
            print(f'Your change is {total - cost_of_latte}')
            print(f'You can have your {choice}')
            return 1
        elif total == cost_of_latte:
            print(f'You can have your {choice}')
            return 1
        else:
            print('amount you entered is low your amount is refunded ')
            return 0
    if choice == 'expresso':
        if total > cost_of_expresso:
            print(f'Your change is {total - cost_of_expresso}')
            print(f'You can have your {choice}')
            return 1
        elif total == cost_of_expresso:
            print(f'You can have your {choice}')
            return 1
        else:
            print('amount you entered is low your amount is refunded ')
            return 0


def coffee_maker():
    choice = input('enter the type of coffee you want(expresso,latte,cappuccino): ')
    if choice == 'report':
        print(report())
        return t
    check = is_available(choice)
    if check:
        print('insert coins')
        q = float(input('enter no of quarter: '))
        d = float(input('enter no of dime: '))
        n = float(input('enter no of nickel : '))
        p = float(input('enter no of pennies : '))
        check2 = is_sufficient(q,d,n,p,choice)
        if check2:
            modify(choice,resources['milk'],resources['water'],resources['coffee'])
            return t
    else:
        print(f'{choice} is not available')
        return t-1


while t:
  t = coffee_maker()
