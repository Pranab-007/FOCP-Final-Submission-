def calculate_total_price(number_of_pizza, tuesday, delivery, app_order):
    # constants for cost and discounts.......
    Cost_Of_Pizza = 12.00
    Delivery_Cost = 2.50
    Discount_on_Tuesdays = 0.50  # 50%
    Discount_using_App = 0.25  # 25%

    tuesday_price = 0

    total_price = number_of_pizza * Cost_Of_Pizza
    # Apply Tuesday Discount
    if tuesday:
        tuesday_price = total_price * (1 - Discount_on_Tuesdays)
    else:
        tuesday_price = total_price

    tuesday_discount = abs(total_price - tuesday_price)

    # Delivery costs £2.50, unless there are five or more pizzas in the order, in which case it is free.
    # There is no cost for collection.
    if number_of_pizza >= 5 and delivery:
        delivery_price = tuesday_price #No delivery charge
    elif not delivery:
        delivery_price = tuesday_price
    else:
        delivery_price = tuesday_price + 2.5

    delivery_discount = abs(delivery_price - tuesday_price)

    # A discount of 25% of the total price if the customer uses BPP app
    if app_order:
        app_price = delivery_price * (1 - Discount_using_App)
    else:
        app_price = delivery_price

    app_discount = abs(app_price - delivery_price)

    total_price = app_price

    return total_price, tuesday_discount, delivery_discount, app_discount

def display_pizza_menu():

    print ("\nWelcome to Beckett Pizza Plaza!")
    print("\nSAVOR THE MOMENT WITH OUR DELICIOUS PIZZAS FOR JUST £12!! ")   #MENU
    print("\n============PIZZA MENU==========")
    print("1. Margherita")
    print("2. Pepperoni")
    print("3. Veggie Supreme")
    print("4. Chicken Supreme")
    print("5. Paneer Pizza")
    print("6. Mix Pizza")
    print("7. Momo Pizza")

def get_pizza_choice():
    while True:
        try:
            pizza_choice = int(input("Choose a pizza (enter the number): "))
            if 1 <= pizza_choice <=7:
                return pizza_choice
            else:
                print("Invalid Input. Please enter a valid pizza number!")

        except ValueError:
            print("Invalid Input! Please enter a number. ")


def main():
    display_pizza_menu()
    pizza_choice = get_pizza_choice()

    print("---------------------------------------------")
    print("BPP PIZZA CALCULATOR".center(45))
    print("===============================".center(45))
    while True:
        try:
            number_of_pizza = int(input("Number of Pizza :  "))  # Get the number of pizzas from the user, ensure it's a positive number
            if number_of_pizza > 0:
                break
            else:
                print("Invalid input. Please enter Positive Integer!")
        except:
            print("Invalid Input !!!!")

    while True:
        tuesday = input("Is it Tuesday? (yes/no):  ").lower().strip()  #check if its Tuesday
        if tuesday in ('yes', 'y'):
            tuesday = True
            break
        elif tuesday in ('no', 'n'):
            tuesday = False
            break
        else:
            print("Invalid input. Please enter 'yes','y' or 'no','n'.")

    while True:
        delivery = input("Do you want to Deliver the order? (yes/no):  ").lower().strip() 
        if delivery in ('yes','y'):                           #use strip to remove leading/traililng whitespace
            delivery = True
            break
        elif delivery in ('no','n'):
            delivery = False
            break
        else:
            print("Invalid input. Please enter 'yes','y' or 'no','n'.")

    while True:
        app_order = input("Is the order done using BPP app? (yes/no):  ").lower().strip()   #check if the order is placed using the BPP app
        if app_order in ('yes', 'y'):
            app_order = True
            break
        elif app_order in ('no', 'n'):
            app_order = False
            break
        else:
            print("Invalid input. Please enter 'yes','y' or 'no','n'.")

    # calculate total order price using the provided function
    total_price, tuesday_discount, delivery_discount, app_discount = calculate_total_price(number_of_pizza, tuesday, delivery, app_order)

    # display individual calculations
    print("\n================== YOUR BILL ==================")
    print(f"Cost of {number_of_pizza} Pizza(s): £{number_of_pizza * 12.00:.2f}") #cost of pizza
    if tuesday:
        print(f"Tuesday Discount (50%): -£{tuesday_discount:.2f}")    
    else:
        print("No Tuesday Discount applied.")

    if delivery and number_of_pizza < 5:
        print(f"Delivery Cost: +£{delivery_discount}")
    elif delivery and number_of_pizza >= 5:
        print("Free Delivery (order has 5 or more pizzas).")
    else:
        print("No Delivery Cost (customer opted for pickup).")

    if app_order:
        print(f"App Discount (25%): -£{app_discount:.2f}")

    # Displaying the total price of the order with two decimal places
    print("\nYour Total Price is: £{:.2f}".format(total_price)) 

    print("==========================================")

if __name__ == "__main__":
    main()


