class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number:
                if not room.is_taken and room.capacity >= people:
                    room.is_taken = True
                    room.guests += people
                    self.guests += people

    def free_room(self, room_number):
        for room in self.rooms:
            if room_number == room_number:
                room.is_taken = False
                self.guests -= room.guests
                room.guests = 0

    def status(self):
        free_rooms = [str(r.number) for r in self.rooms if not r.is_taken]
        taken_rooms = [str(r.number) for r in self.rooms if r.is_taken]
        part_1 = f"Hotel {self.name} has {self.guests} total guests\n"
        part_2 = "Free rooms: " + ", ".join(free_rooms) + "\n"
        part_3 = "Taken rooms: " + ", ".join(taken_rooms)
        return part_1 + part_2 + part_3

