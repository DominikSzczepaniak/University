#creator
from dataclasses import dataclass

@dataclass
class Item:
    price: int
    name: str

@dataclass
class SaleItem:
    item: Item
    quantity: int

class Sale:
    items: list[SaleItem]

    def add_item(self, item: Item, quantity: int): #creator, moznaby bylo tez robic te przedmioty w main i dodawac recznie ale to wtedy
    #nie jest creator
        self.items.append(SaleItem(item, quantity))

def main():
    boots = Item(5, "boots")
    jeans = Item(10, "jeans")
    sale = Sale()
    sale.add_item(boots, 2)
    sale.add_item(jeans, 1)
