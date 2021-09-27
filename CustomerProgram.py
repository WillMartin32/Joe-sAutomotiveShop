import CustomerClass as cust
import CarClass as car

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

    print("Customer:")
    print("-Name:          ", customer1.get_name())
    print("-Address:       ", customer1.get_address())
    print("-Phone Number:  ", customer1.get_phone())
    print()

    print("Car:")
    print("-Make:          ", customer1_car1.get_make())
    print("-Model:         ", customer1_car1.get_model())
    print("-Year:          ", customer1_car1.get_year())


main()