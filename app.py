def check_pvn(price: float) -> float:
    """Aprekina PVN (21%) summu no cenas."""
    if not isinstance(price, (int, float)):
        raise ValueError("Cena ir jābūt skaitliski.")
    if price < 0:
        raise ValueError("Cena nevar būt negatīva.")
    return round(price * 0.21, 2)

def get_total_price(price: float) -> float:
    """Jaunā funkcionalitāte: Aprēķina kopējo cenu kopā ar PVN."""
    return round(price + check_pvn(price), 2)

if __name__ == "__main__":
    test_price = 100.0
    print(f"PVN no {test_price} EUR ir: {check_pvn(test_price)} EUR")
    print(f"Kopā ar PVN: {get_total_price(test_price)} EUR")
