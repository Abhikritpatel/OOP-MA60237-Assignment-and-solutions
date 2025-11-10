class Room:
    def __init__(self,room_number,capacity):
        self.room_number=room_number
        self.is_occupied=False
        self.guest_name=None
        self.capacity=capacity


    def check_vacancy(self):
        return not self.is_occupied
    

    def check_in(self,guest_name):
        if self.check_vacancy():
            self.is_occupied=True
            self.guest_name=guest_name
            print(f"Guest {guest_name} checked into room {self.room_number}")
        else:
            print(f"Room {self.room_number} is already occupied by {self.guest_name}")

    
    def check_out(self):
       if not self.check_vacancy():
           guest=self.guest_name
           self.is_occupied=False
           self.guest_name=None
           print(f"Guest {guest} checked out from room {self.room_number}")
       else:
           print(f"Room {self.room_number} is already vacant")

    def details(self):
        status="Occupied" if self.is_occupied else "Vacant"
        guest_info=f", Guest: {self.guest_name}" if self.is_occupied else ""
        print(f"Room {self.room_number} - Capacity: {self.capacity}, Status: {status}{guest_info}")



class Hotel:
    def __init__(self,name):
        self.name=name
        self.rooms=[]

     #method for adding rooms
    def add_room(self,room):
        self.rooms.append(room)
        print(f"Room {room.room_number} added to hotel {self.name}")

    #method for displaying rooms
    def display_rooms(self):
        for room in self.rooms:
            room.details()

    
    def find_room(self,room_number):
        for room in self.rooms:
            if room.room_number==room_number:
                return room
        return None 
    
    #method for removing rooms
    def remove_room(self,room_number):
        room_to_remove=self.find_room(room_number)
        if room_to_remove:
            self.rooms.remove(room_to_remove)
            print(f"Room {room_number} removed from the hotel {self.name}")
        else:
            print(f"Room {room_number} not found in the hotel {self.name}")



    def hotel_check_in(self,room_number,guest_name):
        room=self.find_room(room_number)
        if room:
            room.check_in(guest_name)
        else:
            print(f"Room {room_number} not found in the hotel {self.name}")

    
    def hotel_check_out(self,room_number):
        room=self.find_room(room_number)

        if room:
            room.check_out()
        else:
            print(f"Room {room_number} not found in the hotel {self.name}")
        
    def display_rooms(self):
        print(f"Rooms in hotel {self.name}:")
        for room in self.rooms:
            room.details()

    def display_vacant_rooms(self):
        print(f"Vacant rooms in hotel {self.name}:")
        found=False
        for room in self.rooms:
            if room.check_vacancy():
                room.details()
                found=True
        if not found:
            print("No vacant rooms available.")

    
    def display_occupied_rooms(self):
        print(f"Occupied rooms in hotel {self.name}:")
        found=False
        for room in self.rooms:
            if not room.check_vacancy():
                room.details()
                found=True
        if not found:
            print("No occupied rooms.")
    

if __name__=="__main__":
        grand_hotel = Hotel("The Grand Hotel")
    
        r101 = Room("101", 2)  
        r102 = Room("102", 2)  
        r201 = Room("201", 4)  
        
        print("--- Setting up Hotel ---")
        grand_hotel.add_room(r101)
        grand_hotel.add_room(r102)
        grand_hotel.add_room(r201)
        
        grand_hotel.display_rooms()
        
      
        print("\n--- Checking in Guests ---")
        grand_hotel.hotel_check_in("101", "Alice")
        grand_hotel.hotel_check_in("201", "The Johnson Family")
        
       
        print("\n--- Attempting Double-Booking ---")
        grand_hotel.hotel_check_in("101", "Bob") 
        
        
        grand_hotel.display_vacant_rooms()
        grand_hotel.display_occupied_rooms()
        
       
        print("\n--- Checking out Guest ---")
        grand_hotel.hotel_check_out("101")
        
        
        print("\n--- Attempting Bad Check-out ---")
        grand_hotel.hotel_check_out("101") 
        
        grand_hotel.display_rooms()