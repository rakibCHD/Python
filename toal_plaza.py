import time
import math
import os

plaza_name = "Podda Setu Toll Plaza"
date = ""
collector_name = ""
shift_id = ""
vehicle_class = ""

base_fare = 0
shift_charge = 0
vat = 0
payable_amount = 0

bike_count = cng_count = private_car_count = micro_bus_count = mini_bus_count = bus_count = truck_count = 0
total_collected = 0

def user_login():
    global collector_name
    user_id = input("Enter your User ID: ")
    password = input("Enter your Password: ")

    if user_id == "rakib" and password == "rakib":
        collector_name = user_id
        print("Login successful.")
        clear_console()
        display()
    else:
        print("Invalid UserID or password!!")
        user_login()

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def date_time():
    global date, shift_id, shift_charge
    current_time = time.localtime()
    date = time.strftime("%d-%m-%Y", current_time)
    current_hour = current_time.tm_hour

    if 6 <= current_hour < 14:
        shift_id = "Morning"
        shift_charge = 7
    elif 14 <= current_hour < 22:
        shift_id = "Evening"
        shift_charge = 7
    else:
        shift_id = "Night"
        shift_charge = 5

def display():
    date_time()
    print(f"{plaza_name}\n        Date: {date}")
    print("--------------------------------")
    print(f"Collector Name: {collector_name}")
    print(f"Shift Id: {shift_id}")
    print("--------------------------------")
    vehicle_list()

def vehicle_list():
    print("\nVehicle List          fare(BDT)")
    print("1. Bike                 20 tk")
    print("2. CNG Auto Rickshaw    40 tk")
    print("3. Private Car          50 tk")
    print("4. Micro Bus            60 tk")
    print("5. Mini Bus             70 tk")
    print("6. Bus                 120 tk")
    print("7. Truck               150 tk")
    print("--------------------------------")
    set_vehicle()

def set_vehicle():
    global vehicle_class, base_fare, bike_count, cng_count, private_car_count, micro_bus_count, mini_bus_count, bus_count, truck_count
    choice = int(input("Select a vehicle: "))

    if choice == 1:
        vehicle_class = "Bike"
        base_fare = 20
        bike_count += 1
        print("Bike selected.")
    elif choice == 2:
        vehicle_class = "CNG Auto Rickshaw"
        base_fare = 40
        cng_count += 1
        print("CNG Auto Rickshaw selected.")
    elif choice == 3:
        vehicle_class = "Private Car"
        base_fare = 50
        private_car_count += 1
        print("Private Car selected.")
    elif choice == 4:
        vehicle_class = "Micro Bus"
        base_fare = 60
        micro_bus_count += 1
        print("Micro Bus selected.")
    elif choice == 5:
        vehicle_class = "Mini Bus"
        base_fare = 70
        mini_bus_count += 1
        print("Mini Bus selected.")
    elif choice == 6:
        vehicle_class = "Bus"
        base_fare = 120
        bus_count += 1
        print("Bus selected.")
    elif choice == 7:
        vehicle_class = "Truck"
        base_fare = 150
        truck_count += 1
        print("Truck selected.")
    else:
        print("\nInvalid Vehicle!!")
        set_vehicle()
    print_token()

def print_token():
    print("\nPress 'P' to print token: ")
    print_choice = input().strip()

    if print_choice.lower() == 'p':
        clear_console()
        calculate_toll()
        token()
    else:
        print_token()

def calculate_toll():
    global vat, payable_amount, total_collected
    vat = base_fare * 0.05
    payable_amount = round(base_fare + shift_charge + vat)
    total_collected += payable_amount

def token():
    print("\n-------------Token-------------")
    print("-------------------------------")
    print(f"\n{plaza_name}")
    print(f"        Date: {date}")
    print("--------------------------------")
    print(f"  Collector Name: {collector_name}")
    print(f"  Shift ID: {shift_id}")
    print(f"  Vehicle Class: {vehicle_class}")
    print("  Fare: ")
    print(f"      Base fare   :  {base_fare} tk")
    print(f"      Shift charge:   {shift_charge} tk")
    print(f"      Vat (5%)    : {vat:.1f} tk")
    print("--------------------------------")
    print(f"  Payable (round) : {payable_amount} Taka")
    print("  Thank you, have a nice trip.")
    toll_continue()

def toll_continue():
    print("\nContinue [Y/N]: ")
    con = input().strip()

    if con.lower() == 'y':
        clear_console()
        display()
    elif con.lower() == 'n':
        logout()
    else:
        toll_continue()

def logout():
    print("\nPress 'L' to LogOut: ")
    press = input().strip()

    if press.lower() == 'l':
        clear_console()
        summary_report()
    else:
        logout()

def summary_report():
    print("\n--------------Summary Report-------------")
    print("------------------------------------------")
    print(f"\n{plaza_name}")
    print(f"        Date: {date}")
    print("--------------------------------")
    print(f"  Collector Name: {collector_name}")
    print(f"  Shift ID: {shift_id}")
    print("  Summary: ")
    print(f"       Bike                 : {bike_count}")
    print(f"       CNG Auto Rickshaw    : {cng_count}")
    print(f"       Private Car          : {private_car_count}")
    print(f"       Micro Bus            : {micro_bus_count}")
    print(f"       Mini Bus             : {mini_bus_count}")
    print(f"       Bus                  : {bus_count}")
    print(f"       Truck                : {truck_count}")
    print("--------------------------------")
    print(f"Total Collected amount: {total_collected} Taka")

if __name__ == "__main__":
    user_login()
