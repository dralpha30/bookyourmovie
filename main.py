from book import Show

global row
global seats

row = int(input("Enter the number of rows: "))

seats = int(input("Enter the number of seats in each row: "))

while True:
    print("*** welcome to bookyourmovie.com ***")
    selection = input("1. show seats\n2. Buy tickets\n3. View statistics\n4. Show booked tickets customer info\n"
                      "0. Exit\n\n")

    obj = Show()
    if selection == "1":
        obj.show_seats(row, seats)
    elif selection == "2":
        obj.buy_tickets(row, seats)
    elif selection == "3":
        obj.show_statistics(row, seats)
    elif selection == "4":
        obj.show_booked_tickets()
    elif selection == "0":
        break

