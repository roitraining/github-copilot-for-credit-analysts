def add_balances(bal_a: float, bal_b: float) -> float:
    # Return the sum of bal_a and bal_b rounded to 2 decimal places
    return round(bal_a + bal_b, 2)


def test_add_balances():
    assert add_balances(1200.50, 300.25) == 1500.75

    