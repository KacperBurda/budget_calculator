import unittest
import budget


class UnitTests(unittest.TestCase):

    def setUp(self):
        self.food = budget.Category("Food")
        self.entertainment = budget.Category("Entertainment")
        self.business = budget.Category("Business")

    def test_deposit_first(self):
        self.food.deposit(900, "deposit")
        actual = self.food.ledger[0]
        expected = {"amount": 900, "description": "deposit"}
        self.assertEqual(actual, expected)

    def test_deposit_second(self):
        self.entertainment.deposit(654.54, "donation")
        self.entertainment.deposit(100, "income")
        actual = self.entertainment.ledger
        expected = [{"amount": 654.54, "description": "donation"}, {"amount": 100, "description": "income"}]
        self.assertEqual(actual, expected)

    def test_deposit_zero(self):
        self.food.deposit(900, "deposit")
        self.food.deposit(0, "deposit")
        actual = self.food.ledger
        expected = [{"amount": 900, "description": "deposit"}]
        self.assertEqual(actual, expected)

    def test_deposit_negative_value(self):
        error_content = "Only positive values accepted. For withdraw use 'withdraw' method."
        self.assertRaisesRegex(ValueError, error_content, self.food.deposit, -900)

    def test_deposit_no_description(self):
        self.food.deposit(45.56)
        actual = self.food.ledger[0]
        expected = {"amount": 45.56, "description": ""}
        self.assertEqual(actual, expected)
    #
    def test_withdraw_first(self):
        self.food.deposit(900, "deposit")
        self.food.withdraw(123, "eggs, water")
        actual = self.food.ledger[1]
        expected = {"amount": -123, "description": "eggs, water"}
        self.assertEqual(actual, expected)

    def test_withdraw_second(self):
        self.food.deposit(900, "deposit")
        self.food.withdraw(45.67, "eggs, water")
        self.food.withdraw(435.67, "meat, butter")
        actual = self.food.ledger
        expected = [{"amount": 900, "description": "deposit"},
                    {"amount": -45.67, "description": "eggs, water"},
                    {"amount": -435.67, "description": "meat, butter"}]
        self.assertEqual(actual, expected)

    def test_withdraw_no_description(self):
        self.business.deposit(900, "deposit")
        good_withdraw = self.business.withdraw(145.30)
        actual = self.business.ledger[1]
        expected = {"amount": -145.30, "description": ""}
        self.assertEqual(actual, expected)
        self.assertEqual(good_withdraw, True, 'Expected `withdraw` method to return `True`.')

    def test_withdraw_negative_value(self):
        self.business.deposit(900, "deposit")
        error_content = "Only positive values accepted."
        self.assertRaisesRegex(ValueError, error_content, self.business.withdraw, -145)

    def test_withdraw_amount_greater_than_deposit(self):
        self.business.deposit(900, "deposit")
        good_withdraw = self.business.withdraw(1200, "withdraw")
        actual = self.business.ledger
        expected = [{"amount": 900, "description": "deposit"}]
        self.assertEqual(actual, expected)
        self.assertEqual(good_withdraw, False, 'Expected `withdraw` method to return `False`.')

    def test_withdraw_zero(self):
        self.food.deposit(900, "deposit")
        actual = self.food.ledger
        bad_withdraw = self.food.withdraw(0, "toys")
        expected = [{"amount": 900, "description": "deposit"}]
        self.assertEqual(actual, expected)
        self.assertEqual(bad_withdraw, False, 'Expected `withdraw` method to return `False`.')

    def test_get_balance_first(self):
        self.food.deposit(900, "deposit")
        self.food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
        actual = self.food.get_balance()
        expected = 854.33
        self.assertEqual(actual, expected, 'Expected balance to be 854.33')

    def test_get_balance_second(self):
        self.entertainment.deposit(1500, "deposit")
        self.entertainment.deposit(300, "income")
        self.entertainment.withdraw(400, "milk, cereal, eggs, bacon, bread")
        self.entertainment.withdraw(500, "milk, cereal, eggs, bacon, bread")
        actual = self.entertainment.get_balance()
        expected = 900
        self.assertEqual(actual, expected)
    #
    def test_transfer_good(self):
        self.food.deposit(900, "deposit")
        self.food.withdraw(450.67, "milk, cereal, eggs, bacon, bread")
        transfer_amount = 200
        food_balance_before = self.food.get_balance()
        entertainment_balance_before = self.entertainment.get_balance()
        good_transfer = self.food.transfer(transfer_amount, self.entertainment)
        food_balance_after = self.food.get_balance()
        entertainment_balance_after = self.entertainment.get_balance()
        actual = self.food.ledger[2]
        expected = {"amount": -transfer_amount, "description": "Transfer to Entertainment"}
        self.assertEqual(actual, expected)
        self.assertEqual(good_transfer, True, 'Expected `transfer` method to return `True`.')
        self.assertEqual(food_balance_before - food_balance_after, transfer_amount)
        self.assertEqual(entertainment_balance_after - entertainment_balance_before, transfer_amount)
        actual = self.entertainment.ledger[0]
        expected = {"amount": transfer_amount, "description": "Transfer from Food"}
        self.assertEqual(actual, expected)

    def test_transfer_zero(self):
        self.food.deposit(1000, "deposit")
        good_transfer = self.food.transfer(0, self.entertainment)
        self.assertEqual(good_transfer, False, 'Expected `transfer` method to return `False`.')

    def test_transfer_no_funds(self):
        self.food.deposit(1000, "deposit")
        good_transfer = self.food.transfer(1200, self.entertainment)
        self.assertEqual(good_transfer, False, 'Expected `transfer` method to return `False`.')

    def test_transfer_negative_value(self):
        self.food.deposit(900, "deposit")
        error_content = "Only positive values accepted."
        self.assertRaisesRegex(ValueError, error_content, self.food.transfer, -900, self.entertainment)

    def test_check_funds_true(self):
        self.food.deposit(20, "deposit")
        actual = self.food.check_funds(10)
        expected = True
        self.assertEqual(actual, expected, 'Expected `check_funds` method to be True')

    def test_check_funds_zero(self):
        self.food.deposit(20, "deposit")
        actual = self.food.check_funds(0)
        expected = False
        self.assertEqual(actual, expected, 'Expected `check_funds` method to be False')

    def test_check_funds_false(self):
        self.food.deposit(20, "deposit")
        actual = self.food.check_funds(40)
        expected = False
        self.assertEqual(actual, expected, 'Expected `check_funds` method to be False')

    def test_to_string_first(self):
        self.food.deposit(900, "deposit")
        self.food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
        self.food.transfer(20, self.entertainment)
        actual = str(self.food)
        expected = f"*************Food*************\n" \
                   f"deposit                 900.00\n" \
                   f"milk, cereal, eggs, bac -45.67\n" \
                   f"Transfer to Entertainme -20.00\n" \
                   f"Total: 834.33"
        self.assertEqual(actual, expected)

    def test_to_string_second(self):
        self.entertainment.deposit(2000, "deposit")
        self.entertainment.deposit(100, "performance, artist royalties, scene view")
        self.entertainment.withdraw(400.23, "fees")
        self.entertainment.withdraw(700.46, "taxes")
        self.entertainment.transfer(100.76, self.food)
        self.entertainment.transfer(45.64, self.business)
        actual = str(self.entertainment)
        expected = "********Entertainment*********\n" \
                   "deposit                2000.00\n" \
                   "performance, artist roy 100.00\n" \
                   "fees                   -400.23\n" \
                   "taxes                  -700.46\n" \
                   "Transfer to Food       -100.76\n" \
                   "Transfer to Business    -45.64\n" \
                   "Total: 852.91"
        self.assertEqual(actual, expected)
