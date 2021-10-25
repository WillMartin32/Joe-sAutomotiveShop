import CustomerClass as cust
import CarClass as car
import ServiceQuoteClass as ser

def main():

    customer_name = input("What is your name? ")
    customer_address = input("What is your address? ")
    customer_phone = input("What is your phone number? ")
    print()

    customer1 = cust.Customer(customer_name,customer_address,customer_phone)

    car_make = input("What is the make of your car? ")
    car_model = input("What is the model of your car? ")
    car_year = input("What is the year of your car? ")
    print()

    customer1_car1 = car.Car(car_make,car_model,car_year)

    part_service = input("What is the cost of the parts? ")
    labor_service = input("What is the cost of labor? ")
 #   tax_rate = input("What is the tax rate? (Ex. .20) ")
    print()

    customer1_service1 = ser.ServiceQuote(part_service,labor_service)

 #   tax = str(customer1_service1.get_sales_tax)

 #   customer1_service1 = ser.ServiceQuote(part_service,labor_service,tax)
    tax = customer1_service1.get_sales_tax
    tax = .20*float(tax)


    print("Customer:")
    print("-Name:          ", customer1.get_name())
    print("-Address:       ", customer1.get_address())
    print("-Phone Number:  ", customer1.get_phone())
    print()

    print("Car:")
    print("-Make:          ", customer1_car1.get_make())
    print("-Model:         ", customer1_car1.get_model())
    print("-Year:          ", customer1_car1.get_year())
    print()

    print("Cost:")
    print("Part(s) Cost:   ", customer1_service1.get_parts_charges())
    print("Labor Cost:     ", customer1_service1.get_labor_charges())
    print("Sales Tax:      ", tax)
    print("Total Cost:     ", customer1_service1.get_total_charges(tax))
    print()

   # tax = customer1_service1.get_sales_tax
   # print(customer1_service1.get_total_charges())


main()