import CustomerClass as cust

def main():

    customer_name = input("What is your name? ")
    customer_address = input("What is your address? ")
    customer_phone = input("What is your phone number? ")

    customer1 = cust.Customer(customer_name,customer_address,customer_phone)

    print("Name:          ", customer1.get_name())
    print("Address:       ", customer1.get_address())
    print("Phone Number:  ", customer1.get_phone())


main()