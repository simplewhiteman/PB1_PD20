def check_pvn(price: float) -> float:
    """Aprekina PVN (21%) summu no cenas."""
    if not isinstance(price, (int, float)):
        raise ValueError("Cena ir jābūt skaitliski.")
    if price < 0:
        raise ValueError("Cena nevar būt negatīva.")
    return round(price * 0.21, 2)

if __name__ == "__main__":
    test_price = 100.0
    print(f"PVN no {test_price} EUR ir: {check_pvn(test_price)} EUR")