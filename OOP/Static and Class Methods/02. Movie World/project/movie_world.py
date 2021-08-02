class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if self.customer_capacity() > len(self.customers):
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if self.dvd_capacity() > len(self.dvds):
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        for c in self.customers:
            if c.id == customer_id:
                customer = c
        for d in self.dvds:
            if d.id == dvd_id:
                dvd = d
        # If the customer has already rented that dvd
        for d in customer.rented_dvds:
            if d.id == dvd_id:
                return f"{customer.name} has already rented {d.name}"
        # if the dvd is rented by somebody else
        if dvd.is_rented:
            return "DVD is already rented"
        # If the customer is not allowed to rent the DVD
        if dvd.age_restriction > customer.age:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        # Otherwise, the rent is successful
        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        for c in self.customers:
            if c.id == customer_id:
                customer = c
        for d in self.dvds:
            if d.id == dvd_id:
                dvd = d
        if dvd in customer.rented_dvds:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f"{customer.name} has successfully returned {dvd.name}"
        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        repr_list = []
        for c in self.customers:
            repr_list.append(c.__repr__())
        for d in self.dvds:
            repr_list.append(d.__repr__())
        return "\n".join(repr_list)
