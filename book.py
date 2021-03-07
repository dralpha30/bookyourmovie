import math
import re

BASE_TICKET_PRICE = 200

class Show:
    global customers
    global booked_seats_number

    booked_seats_number = []
    customers = []

    def show_seats(self, row, seats):
        """
            This method will show us seats status in cinema hall.
            B- Booked
            S- Available
        """
        print("Cinema: ")

        col_string = ' '
        for i in range(1, seats + 1):
            col_string += ' ' + str(i)
        print(col_string)

        for i in range(1, row + 1):
            row_string = ''
            for j in range(1, seats + 1):
                ds = int(str(i) + str(j))
                if ds in booked_seats_number:
                    row_string += ' B'
                else:
                    row_string += ' S'

            print(str(i)+row_string)

    def buy_tickets(self, row, seats):
        ticket_price = 0

        s_row = int(input("Enter row number: "))
        s_col = int(input("Enter seat number: "))

        if s_row <= row and s_col <= seats:

            total_seats = row * seats

            if total_seats <= 60:
                ticket_price = 10
            else:
                ticket_price = 8
                front_rows = math.floor(row/2)
                if s_row <= front_rows:
                    ticket_price = 10

            seat_no = int(str(s_row) + str(s_col))

            print("Ticket cost:", ticket_price)
            prompt = input("Do you want to book the ticket? yes/no")
            ans = prompt.lower()
            if ans == "yes":
                data = {}
                name = input("Name: ")

                while True:
                    gender = input("Gender (male,female or transgender): ")
                    if gender.lower() not in ["male", "female", "transgender"]:
                        print("Invalid gender, gender can be male, female or transgender")
                        continue
                    break
                while True:
                    age = int(input("Age: "))

                    if age not in range(1, 111):
                        print("Invalid age, Please enter valid age between 1 - 111")
                        continue
                    break
                while True:
                    ph_no = (input("Phone Number: "))
                    x = re.match("[7-9][0-9]{9}", ph_no)
                    if not x:
                        print("invalid phone number! please enter 10 digit no starting with 7 , 8 or 9")
                        continue
                    break

                data["name"] = name
                data["gender"] = gender
                data["age"] = age
                data["ph_no"] = ph_no
                data["row"] = row
                data["ticket_price"] = ticket_price
                data["seat_no"] = seat_no
                customers.append(data)
                booked_seats_number.append(seat_no)
                print("Booked successfully!!")
                print("Thank you for booking")
                print(f"Your seat number is: ", seat_no)
            else:
                print("Thank You for visiting!!!")
        else:
            print("seat does not exist! enter a available seat no next time")

    def show_booked_tickets(self):
        """
            This function will print customers details based on user's choice i.e for all customers or
             for specific customer for given seat number
        """
        ans = input(
            "Do you want to see the information of all customers?(yes/no): ")
        ans = ans.lower()

        if ans == "yes":
            customer_number = 0
            for customer in customers:
                customer_number += 1
                print(str(customer_number) + ".)")
                print("Name:", customer.get("name"))
                print("Gender:", customer.get("gender"))
                print("Age:", customer.get("age"))
                print("Contact Number: ", customer.get("ph_no"))
                print("Seat Number:", customer.get("seat_no"))
                print("Ticket Price:", customer.get("ticket_price"))
        else:
            ans = input("Please enter a customer's seat number: ")
            ans = ans.lower()
            for customer in customers:
                if customer.get("seat_no") == int(ans):
                    print("Name:", customer.get("name"))
                    print("Gender:", customer.get("gender"))
                    print("Age:", customer.get("age"))
                    print("Contact Number: ", customer.get("ph_no"))
                    print("Seat Number:", customer.get("seat_no"))
                    print("Ticket Price:", customer.get("ticket_price"))
                    break

    def show_statistics(self, row, seats):
        """
            This function will print statistics such as total income, maximum possible income and also
            detail about normal and premium tickets.
        """

        print(f"Number of tickets sold: {len(booked_seats_number)}")

        total_seats = row * seats
        percentage_of_tickets_booked = (len(booked_seats_number) / total_seats) * 100
        print("Percentage of tickets sold", str(round(percentage_of_tickets_booked, 2)) + "%")

        res = [key.get("ticket_price") for key in customers]
        print("Current Income", str(sum(res)), "$")

        if total_seats <= 60:
            total_income = row * seats * 10
        else:
            front_rows = math.floor(row / 2)
            total_income = (front_rows * seats * 10) + ((row - front_rows) * seats * 8)

        print("total possible income:", str(total_income), "$")
