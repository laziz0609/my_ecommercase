




class Product:
    
    def __init__(self, name: str, category: str, price: float, sale: int, stock: int, description: str, id: int | None = None):
        self.name = name
        self.category = category
        self.price = price
        self.sale = sale
        self.stock = stock
        self.description = description
        self.id = id
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name = data["name"],
            category = data["category"],
            price = data["price"],
            sale = data["sale"],
            stock = data["stock"],
            description = data["description"],
            id = data["id"]
        )
        