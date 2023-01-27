from dataclasses import dataclass, field


@dataclass(repr=False)
class Category:
    name: str
    ledger: list = field(default_factory=list)
    sum_withdraws: list = field(default_factory=list)

    def deposit(self, amount, description: str = ''):
        if amount > 0:
            deposit = {'amount': float(amount), 'description': description}
            self.ledger.append(deposit)
            return deposit
        if amount < 0:
            raise ValueError("Only positive values accepted. For withdraw use 'withdraw' method.")

    def withdraw(self, amount, description: str = ''):
        if amount < 0:
            raise ValueError("Only positive values accepted.")
        if self.check_funds(amount):
            withdraw = {'amount': -abs(amount), 'description': description}
            self.ledger.append(withdraw)
            self.sum_withdraws.append(withdraw)
            return True
        else:
            return False

    def sum_category_withdraws(self):
        summed_category = abs(sum([x['amount'] for x in self.sum_withdraws]))
        return summed_category

    def get_balance(self):
        balance = sum([record['amount'] for record in self.ledger])
        return balance

    def transfer(self, amount, obj):
        if amount < 0:
            raise ValueError("Only positive values accepted.")
        if self.check_funds(amount):
            description = f'Transfer to {obj.name}'
            self.withdraw(amount, description)
            description = f'Transfer from {self.name}'
            obj.deposit(amount, description)
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount == 0:
            return False
        if amount > self.get_balance():
            return False
        else:
            return True

    def __str__(self):
        lines_to_display = [f"{self.name:*^30}\n"]
        for x in enumerate(self.ledger):
            if len(x[1]['description']) <= 23:
                lines_to_display.append(
                    f"{self.ledger[x[0]]['description']:<23}{float(self.ledger[x[0]]['amount']):>7.2f}\n")
            else:
                lines_to_display.append(
                    f"{self.ledger[x[0]]['description'][0:23:]:<21}{float(self.ledger[x[0]]['amount']):>7.2f}\n")
        lines_to_display.append(f"Total: {self.get_balance()}")

        display = ''.join(lines_to_display)
        return display
