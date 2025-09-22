class FlightNotFoundError(Exception):
    pass
class SeatsUnavailableError(Exception):
    pass
try:
    f= open('flights.txt', 'r')
   
    try:
       data = f.readlines()
       print("Details", data)

       flight_number = []
       available_seats = []
       price_per_ticket = []

       for item in data:
           new_item = item.split()
           flight_number.append(new_item[0])
           available_seats.append(new_item[1])
           price_per_ticket.append(new_item[2])
               
       print("Flight numbers =", flight_number)
       
       input_flight_number = input('Enter the flight number: ')

       index = -1
       found = False
       for f_number in flight_number:
           if f_number == input_flight_number:
               index = index + 1
               found = True
               break
           index = index + 1
           
       if found == False:
           raise FlightNotFoundError('The entered flight number does not exist')
       
       number_of_tickets = int(input('Number of tickets to book: '))
       if number_of_tickets <= 0:
           raise ZeroDivisionError("The entered number of ticket is not valid")

       available_tickets = int(available_seats[index])
       print("Available tickets =", available_tickets)

       if number_of_tickets > available_tickets:
           raise SeatsUnavailableError('The requested tickets exceed available seats')
       
       total_booking_cost = int(price_per_ticket[index]) * number_of_tickets
       discount_per_ticket = total_booking_cost / number_of_tickets

       print("*************************************************")
       print(f"Flight Number: {flight_number[index]}\nNo. of Tickets: {number_of_tickets}\nTotal booking cost: {total_booking_cost}\nDiscount per ticket: {discount_per_ticket}")
       print("*************************************************")

    except FlightNotFoundError as e:
        print("Exception Occurred: ", e)
    except SeatsUnavailableError as e:
        print("Exception Occurred: ", e)
    except ValueError as ve:
        print("Invalid input (like string instead of integer): ", ve)
    except ZeroDivisionError as e:
         print("User entered 0 tickets: ", e)
    finally:
         print("Session closed")
       
except FileNotFoundError:
    print("Flight details file not found")
except Exception as e:
    print("Generic Exception", e)
	
