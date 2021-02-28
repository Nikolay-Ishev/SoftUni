class Hero:
    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = int(hp)
        self.mp = int(mp)

    def cast_spell(self, mp_needed, spell):
        if self.mp >= int(mp_needed):
            self.mp -= int(mp_needed)
            print(f"{self.name} has successfully cast {spell} and now has {self.mp} MP!")
        else:
            print(f"{self.name} does not have enough MP to cast {spell}!")

    def take_damage(self, damage, attacker):
        if self.hp > int(damage):
            self.hp -= int(damage)
            print(f"{self.name} was hit for {damage} HP by {attacker} and now has {self.hp} HP left!")
        else:
            dead_hero = [x for x in heroes_list if x.name == self.name]
            heroes_list.remove(dead_hero[0])
            print(f"{self.name} has been killed by {attacker}!")

    def recharge(self, amount):
        amount = int(amount)
        if amount + self.mp <= 200:
            self.mp += amount
        else:
            amount = 200 - self.mp
            self.mp = 200
        print(f"{self.name} recharged for {amount} MP!")

    def heal(self, amount):
        amount = int(amount)
        if amount + self.hp <= 100:
            self.hp += amount
        else:
            amount = 100 - self.hp
            self.hp = 100
        print(f"{self.name} healed for {amount} HP!")


heroes_list = []
n = int(input())
for hero in range(n):
    h_name, h_hp, h_mp = input().split()
    h_hp = int(h_hp)
    h_mp = int(h_mp)
    h_name = Hero(h_name, h_hp, h_mp)
    heroes_list.append(h_name)

command = input()
while command != "End":
    command = command.split(" - ")
    if command[0] == "CastSpell":
        h = [x for x in heroes_list if x.name == command[1]]
        h[0].cast_spell(command[2], command[3])
    elif command[0] == "TakeDamage":
        h = [x for x in heroes_list if x.name == command[1]]
        h[0].take_damage(command[2], command[3])
    elif command[0] == "Recharge":
        h = [x for x in heroes_list if x.name == command[1]]
        h[0].recharge(command[2])
    elif command[0] == "Heal":
        h = [x for x in heroes_list if x.name == command[1]]
        h[0].heal(command[2])
    command = input()
heroes_dict = {}
for x in heroes_list:
    heroes_dict[x.name] = [x.hp, x.mp]
heroes_ord = dict(sorted(heroes_dict.items(), key=lambda x: (-x[1][0], x[0])))
for key, value in heroes_ord.items():
    print(f"{key}")
    print(f"HP: {value[0]}")
    print(f"MP: {value[1]}")
