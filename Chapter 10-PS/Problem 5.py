class Train:
    def __init__(self, name, seats, fare):
        self.name = name
        self.seats = seats
        self.fare = fare

    def book_ticket(self):
        if self.seats > 0:
            self.seats -= 1
            print("Booked.")
        else:
            print("Sold out.")

    def get_status(self):
        return self.seats

    def get_fare(self):
        return self.fare

print("Welcome to the Train Booking System!")
train = Train("Express 101", 10, 500)
print(f"Train Name: {train.name}")
print(f"Available Seats: {train.get_status()}")
print(f"Ticket Fare: {train.get_fare()}")