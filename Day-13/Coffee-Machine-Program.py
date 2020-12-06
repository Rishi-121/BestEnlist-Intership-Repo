# Coffee Machine Problem


class coffeMachine:

    # Initialize the Coffee Supplies
    def __init__(self, water, milk, coffee, money):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.money = money

    # Check whether the resources are available or not
    def checkResources(self, choice, requirements):
        self.choice = choice
        self.requirements = requirements
        if self.choice == "expresso":
            if self.water - self.requirements[0] < 0:
                print("Sorry! there is not enough water")
            elif self.milk - self.requirements[1] < 0:
                print("Sorry! there is not enough milk")
            elif self.coffee - self.requirements[2] < 0:
                print("Sorry! there is not enough coffee")
            elif self.money - self.requirements[3] < 0:
                print("Sorry! there is not enough money")
            else:
                return True

    # Process the payment
    def processCoins(self):
        self.payment = input(
            "Enter payment here. Accepted coins ( quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01 ): ").split(",")
        self.allCoins = {}
        for i in self.payment:
            i = i.split(" ")
            self.allCoins[i[1]] = int(i[0])

        # Default Coin Values
        self.quarters = 4
        self.dimes = 2
        self.nickles = 1
        self.pennies = 1

        self.totalAmount = 0
        self.coins = list(self.allCoins.keys())

        # Calculate the total payment
        for coin in self.coins:
            if coin == "quarters":
                self.totalAmount += self.allCoins[coin]*self.quarters
            elif coin == "dimes":
                self.totalAmount += self.allCoins[coin]*self.dimes
            elif coin == "nickles":
                self.totalAmount += self.allCoins[coin]*self.nickles
            elif coin == "pennies":
                self.totalAmount += self.allCoins[coin]*self.pennies

        self.checkTransaction()

    # Check whether the transaction is successful or not
    def checkTransaction(self):
        if self.totalAmount < self.requirements[3]:
            print("Sorry that's not enough money. Money refunded.")
            return None
        elif self.requirements[3] < self.totalAmount:
            self.money += self.requirements[3]
            self.change = round(self.totalAmount - self.requirements[3], 2)
            print(f"Here is ${self.change} dollars in change.")
        else:
            self.money += self.totalAmount
        self.totalAmount = 0

        self.prepareCoffee()
    # To prepare the customer's coffee

    def prepareCoffee(self):
        self.water -= self.requirements[0]
        self.milk -= self.requirements[1]
        self.coffee -= self.requirements[2]
        print(f"Here is your {self.choice}. Enjoy!")

    # To generate the report
    def printReport(self):
        print(f"Water: {self.water}ml")
        print(f"Milk: {self.milk}ml")
        print(f"Coffee: {self.coffee}g")
        print(f"Money: ${self.money}")


# Driver Code
customer = coffeMachine(400, 540, 120, 550)

choice = ''

# Requirements for each coffee (Water, Milk, Coffee, Money)
expresso = [250, 0, 16, 4]
latte = [350, 75, 20, 7]
cappuccino = [350, 75, 20, 7]

while choice != "off":

    choice = input("“​What would you like? (espresso/latte/cappuccino): ")
    if choice == "expresso":
        if customer.checkResources(choice, expresso):
            customer.processCoins()
    elif choice == "latte":
        if customer.checkResources(choice, latte):
            customer.processCoins()
    elif choice == "cappuccino":
        if customer.checkResources(choice, cappuccino):
            customer.processCoins()
    elif choice == "report":
        customer.printReport()
