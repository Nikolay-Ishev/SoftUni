class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        repr_list = []
        # finding current subscription
        for s in self.subscriptions:
            if s.id == subscription_id:
                subscription = s
                repr_list.append(subscription.__repr__())
                break
        # finding the customer
        for c in self.customers:
            if c.id == subscription.customer_id:
                customer = c
                repr_list.append(customer.__repr__())
        # finding the trainer
        for t in self.trainers:
            if t.id == subscription.trainer_id:
                trainer = t
                repr_list.append(trainer.__repr__())
        # finding the plan
        for p in self.plans:
            if p.id == subscription.exercise_id:
                plan = p
        # finding the equipment
        for e in self.equipment:
            if e.id == plan.equipment_id:
                equipment = e
                repr_list.append(equipment.__repr__())
                repr_list.append(plan.__repr__())
        return "\n".join(repr_list)
