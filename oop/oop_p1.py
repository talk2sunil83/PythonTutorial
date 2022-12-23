# %%

from datetime import datetime
from typing import List
from dataclasses import dataclass
from enum import Enum
# %%


class Unit(Enum):
    Kilogram = 1,
    Gram = 2,
    Litre = 3,
    ML = 4
    Dozen = 5,
    Meter = 6,
    CM = 7
    Qtl = 8
    Other = 9


class ItemType(Enum):
    Food = 1,
    Apearal = 2,
    Luxary = 3,
    Electronics = 4,
    Cosmetics = 5,
    Hygene = 6,
    Kitchen = 7
    Other = 8


@dataclass
class Expense:
    # def __init__(self, item: str, unit: str, quantity: float, rate: float, on: datetime) -> None:
    # self.item: str
    # self.unit: str
    # self.quantity: float
    # self.rate: float
    # self.on: datetime

    # def __repr__(self) -> str:
    #     return f"{self.item=}, {self.unit=}, {self.quantity=}, {self.rate=}, Purchade on: {self.on}"

    # item: str
    # unit: str
    # quantity: float
    # rate: float
    # on: datetime

    item: str
    item_type: ItemType
    unit: Unit
    quantity: float
    rate: float
    on: datetime

    def __eq__(self, __o: object) -> bool:
        return self.rate * self.quantity == __o.rate * __o.quantity

    def __gt__(self, __o: object) -> bool:
        return self.rate * self.quantity > __o.rate * __o.quantity

    def __ge__(self, __o: object) -> bool:
        return self.rate * self.quantity >= __o.rate * __o.quantity

    def __lt__(self, __o: object) -> bool:
        return self.rate * self.quantity < __o.rate * __o.quantity

    def __le__(self, __o: object) -> bool:
        return self.rate * self.quantity <= __o.rate * __o.quantity
# %%


class ExpenseTracker:
    def __init__(self) -> None:
        self.__expenses__: List[Expense]

    def add_expense(self, expense: Expense) -> None:
        self.__expenses__.append(expense)

    def get_total_items(self) -> int:
        return len(self.__expenses__)


# %%
har_expense_tracker = ExpenseTracker()
sep_expense_tracker = ExpenseTracker()
sub_expense_tracker = ExpenseTracker()
sun_expense_tracker = ExpenseTracker()
swa_expense_tracker = ExpenseTracker()


# %%
expense = Expense("Banana", ItemType.Food, Unit.Kilogram, 5, 120, datetime.now())

# %%
# print(expense)
# %%
expense1 = Expense("Milk", ItemType.Food, Unit.Litre, 2, 60, datetime.now())
print(expense1)
# %%
print(
    expense > expense1,
    expense >= expense1,
    expense < expense1,
    expense <= expense1,
    expense == expense1,
)

# %%
