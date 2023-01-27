import unittest
import budget
from spend_chart import create_spend_chart


class UnitTests(unittest.TestCase):

    def setUp(self):
        self.food = budget.Category("Food")
        self.entertainment = budget.Category("Entertainment")
        self.business = budget.Category("Business")
        self.toys = budget.Category("Toys")
        self.auto = budget.Category("Auto")
        self.clothing = budget.Category("Clothing")

    def test_create_spend_chart_first(self):
        self.food.deposit(900, "deposit")
        self.entertainment.deposit(900, "deposit")
        self.business.deposit(900, "deposit")
        self.food.withdraw(105.55)
        self.entertainment.withdraw(33.40)
        self.business.withdraw(10.99)
        actual = create_spend_chart([self.business, self.food, self.entertainment])
        expected = "Percentage spent by category\n" \
                   "100|          \n" \
                   " 90|          \n" \
                   " 80|          \n" \
                   " 70|    o     \n" \
                   " 60|    o     \n" \
                   " 50|    o     \n" \
                   " 40|    o     \n" \
                   " 30|    o     \n" \
                   " 20|    o  o  \n" \
                   " 10|    o  o  \n" \
                   "  0| o  o  o  \n" \
                   "    ----------\n" \
                   "     B  F  E  \n" \
                   "     u  o  n  \n" \
                   "     s  o  t  \n" \
                   "     i  d  e  \n" \
                   "     n     r  \n" \
                   "     e     t  \n" \
                   "     s     a  \n" \
                   "     s     i  \n" \
                   "           n  \n" \
                   "           m  \n" \
                   "           e  \n" \
                   "           n  \n" \
                   "           t  "
        self.assertEqual(actual, expected, 'Expected different chart representation. Check that all spacing is exact.')

    def test_create_spend_chart_second(self):
        self.food.deposit(900, "deposit")
        self.toys.deposit(900)
        self.clothing.deposit(900, "deposit")
        self.entertainment.deposit(900, "deposit")
        self.business.deposit(900, "deposit")
        self.food.withdraw(120.53)
        self.clothing.withdraw(146.23)
        self.toys.withdraw(11.78, "")
        self.business.withdraw(600.99)
        actual = create_spend_chart([self.business, self.food, self.clothing, self.toys, self.auto])
        expected = "Percentage spent by category\n" \
                   "100|                \n" \
                   " 90|                \n" \
                   " 80|                \n" \
                   " 70|                \n" \
                   " 60| o              \n" \
                   " 50| o              \n" \
                   " 40| o              \n" \
                   " 30| o              \n" \
                   " 20| o              \n" \
                   " 10| o  o  o        \n" \
                   "  0| o  o  o  o     \n" \
                   "    ----------------\n" \
                   "     B  F  C  T  A  \n" \
                   "     u  o  l  o  u  \n" \
                   "     s  o  o  y  t  \n" \
                   "     i  d  t  s  o  \n" \
                   "     n     h        \n" \
                   "     e     i        \n" \
                   "     s     n        \n" \
                   "     s     g        "
        self.assertEqual(actual, expected, 'Expected different chart representation. Check that all spacing is exact.')


if __name__ == "__main__":
    unittest.main()
