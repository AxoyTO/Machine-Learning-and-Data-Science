class BankCard:

    def __init__(self, total_sum):
        self.total_sum = total_sum

    def GetTotalSum(self):
        return self.total_sum

    def SetTotalSum(self, val):
        self.total_sum == val

    def put(self, added_sum):
        self.total_sum += added_sum
        ("You put", added_sum, "dollars.", self.total_sum, "dollars are left.")

    def __call__(self, spent_sum):
        if(self.total_sum - spent_sum >= 0):
            self.total_sum -= spent_sum
            print("You spent", spent_sum, "dollars.",
                  self.total_sum, "dollars are left.")
        else:
            print("Not enough money to spent", spent_sum, "dollars.")

    def __repr__(self):
        return 'To learn the balance you should put the money on the card, spent some money or get the bank data. The last procedure is not free and costs 1 dollar.'

    @property
    def balance(self):
        if(self.total_sum > 0):
            self.total_sum -= 1
            return self.total_sum
        else:
            raise ValueError


if __name__ == "__main__":
    a = BankCard(10)
    a(5)
    print(a)
    print(a.balance)
    print(a.total_sum)
