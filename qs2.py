from datetime import datetime,timedelta

class flight:
    def __init__(self,flight_number,destination,departure_time,arrival_time):
        self.__flight_number=flight_number
        self.__destination=destination
        self.__departure_time=departure_time
        self.__arrival_time=arrival_time
    
    
    #private method to determine if the flight is upcoming

    def __is_upcoming(self):
        current_time=datetime.now()
        # Remove strptime since self.__departure_time is already a datetime object
        return self.__departure_time > current_time
    
    ## Public getter methods
    def get_flight_number(self):
        return self.__flight_number
    
    def is_upcoming(self):
        return self.__is_upcoming()

    def get_destination(self):
        return self.__destination

    #public method to update departure time,arrival time

    def update_departure_time(self,new):
        self.__departure_time=new
        print(f"{self.__flight_number} departure time updated to {new}")

    def update_arrival_time(self,new):
        self.__arrival_time=new
        print(f"{self.__flight_number} arrival time updated to {new}")


    def display_info(self):
        print(f"Flight number: {self.get_flight_number()}")
        print(f"Destination: {self.get_destination()}")
        print(f"Departure time: {self.__departure_time}")
        print(f"Arrival time: {self.__arrival_time}")
        status="Upcoming" if self.is_upcoming() else "Departed"
        print(f"Status: {status}")


class Airport():
        def __init__(self,airport_name):
            self.__airport_name=airport_name
            self.__flights=[]

        #private method to find flight by flight number

        def __find_flight(self,flight_number):
            for flight in self.__flights:
                if flight.get_flight_number()==flight_number:
                    return flight
            return None



        # public method to add flight
        def add_flight(self,flight):
            if self.__find_flight(flight.get_flight_number()) is None:
                self.__flights.append(flight)
                print(f"Flight {flight.get_flight_number()} added to {self.__airport_name}")


        #public method to remove flight
        def remove_flight(self,flight):
            existing_flight=self.__find_flight(flight.get_flight_number())
            if existing_flight is not None:
                self.__flights.remove(existing_flight)
                print(f"Flight{flight.get_flight_number()} removed from {self.__airport_name}")
            
        
        #public method to display upcoming flights
        def display_upcoming_flights(self):
            print(f"upcoming flights at {self.__airport_name}")
            found=False
            for flight in self.__flights:
                if flight.is_upcoming():
                    flight.display_info()
                    found=True

            if not found:
                print("No upcoming flights.")

        #public method to display completed flights
        def display_completed_flights(self):
            print(f"completed flights at {self.__airport_name}")
            found=False
            for flight in self.__flights:
                if not flight.is_upcoming():
                    flight.display_info()
                    found=True
            
            if not found:
                print("No completed flights.")

        #public method to display all flight details
        def display_all_flights(self):
            print(f"All flights at {self.__airport_name}")
            if not self.__flights:
                print("No flights available.")
            for flight in self.__flights:
                flight.display_info()

    
if __name__=="__main__":
    now = datetime.now()
    f1=flight("A123","Delhi",now+timedelta(hours=2),now+timedelta(hours=5))
    f2=flight("B456","Mumbai",now-timedelta(hours=3),now-timedelta(hours=0, minutes=30))
    f3 = flight("LH300", "Berlin", now + timedelta(days=1), now + timedelta(days=1, hours=8))

    airport1=Airport("Indira Gandhi International Airport")
    airport1.add_flight(f1)
    airport1.add_flight(f2)
    airport1.add_flight(f3)

    airport1.display_all_flights()
    airport1.display_upcoming_flights()
    airport1.display_completed_flights()

    # 4. Update a flight using its public "setter" method
    print("\n--- Updating Flight B456 ---")
    f2.update_departure_time(now - timedelta(hours=4)) # Update a private attribute
    airport1.display_all_flights() # Show the change

    # 5. Remove a flight using the airport's public method
    print("\n--- Removing Flight A123 ---")
    airport1.remove_flight(f1)  # Pass the flight object, not the string
    airport1.display_all_flights()