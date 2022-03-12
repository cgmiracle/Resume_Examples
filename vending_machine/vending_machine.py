inserted_cash = []
class vending_machine:
    #p = vending_machine(1)
    def __init__(self, cash):
        while True:
            try:
                self.cash = float(input("Please insert cash: $"))
            except ValueError: 
                print('Please insert a valid dollar amount.')
                continue
            if self.cash > 20:
                print("We do no take more than $20 at a time.")
                continue
            else:
                break
                
        
    def cash_convert(self):
            global inserted_cash
            cash = float(self.cash) * 100
            inserted_cash = cash
            #print(inserted_cash)
            p.select_drink()
    
    def select_drink(self):
        drink_cost = {
    "water" : 150,
    "soda" : 200,
    "juice" : 250,
    "energy drink" : 300
}
        
        print(f'You have ${(inserted_cash * .01)}0')
        print("Menu:")
        print("Water : $1.50")
        print("Soda : $2.00")
        print("Juice : $2.50")
        print("Energy Drink : $3.00")
        global drink_selection
        drink_selection = input("Please select a drink:")
        global selection_cost
        sanatize_input = drink_selection.lower()
        if sanatize_input in drink_cost:
            selection_cost = drink_cost.get(sanatize_input)
        else:
            print("Please enter a drink from the menu.")
            p.select_drink()
        #selection_cost = drink_cost.get(sanatize_input)
        p.transaction()
        
        
    def transaction(self):
        global inserted_cash
        if int(inserted_cash) < selection_cost:
            print('You do not have enough for this item.')
            more_cash = input('Please insert more cash:')
            inserted_cash = (float(more_cash) * 100) + inserted_cash
            p.select_drink()
        else:
            change = int(inserted_cash) - int(selection_cost)
            change = int(change) * .01
            if change >= 1.5:
                another_drink = input(f'You still have ${change}0 remaining. Would you like another drink? [Y/N]')
                if another_drink.upper() == 'Y':
                        inserted_cash = (change * 100)
                        p.select_drink()
                else: print(f"Thank you, your change is ${change}0, enjoy your {drink_selection}!")
            else:
                print(f"Thank you, your change is ${change}0, enjoy your {drink_selection}!")

p = vending_machine(1)
p
p.cash_convert()
