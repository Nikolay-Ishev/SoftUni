from project.hero import Hero
from unittest import TestCase, main


class HeroTest(TestCase):
    def setUp(self):
        self.hero = Hero(username="Test", level=7, health=100, damage=10)
        # self.enemy = Hero(username="Test_2", level=6, health=90, damage=8)

    def test_init_creates_all_attributes(self):
        self.assertEqual("Test", self.hero.username)
        self.assertEqual(7, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(10, self.hero.damage)

    def test_battle_raises_error_when_username_equals_enemy_name(self):
        enemy = Hero(username="Test", level=6, health=90, damage=8)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_raises_error_when_yours_or_enemy_hp_zero_or_lower(self):
        enemy = Hero(username="Test_2", level=6, health=0, damage=8)
        with self.assertRaises(ValueError) as ex:
            enemy.battle(self.hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight Test_2. He needs to rest", str(ex.exception))

    def test_battle_calculations_when_draw(self):
        enemy = Hero(username="Test_2", level=10, health=60, damage=10)
        self.assertEqual("Draw", self.hero.battle(enemy))
        self.assertEqual(-10, enemy.health)
        self.assertEqual(0, self.hero.health)

    def test_battle_calculations_when_win(self):
        enemy = Hero(username="Test_2", level=10, health=60, damage=5)
        self.assertEqual("You win", self.hero.battle(enemy))
        self.assertEqual(55, self.hero.health)
        self.assertEqual(15, self.hero.damage)
        self.assertEqual(8, self.hero.level)
        self.assertEqual(-10, enemy.health)

    def test_battle_calculations_when_loose(self):
        enemy = Hero(username="Test_2", level=10, health=100, damage=10)
        self.assertEqual("You lose", self.hero.battle(enemy))
        self.assertEqual(0, self.hero.health)
        self.assertEqual(15, enemy.damage)
        self.assertEqual(35, enemy.health)
        self.assertEqual(11, enemy.level)

    def test_str_returns_correct_info(self):
        result = f"Hero Test: 7 lvl\n" \
               f"Health: 100\n" \
               f"Damage: 10\n"
        self.assertEqual(result, str(self.hero))

if __name__ == "__main__":
    main()
