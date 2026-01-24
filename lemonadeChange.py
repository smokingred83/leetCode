def lemonadeChange(bills: [int]) -> bool:
    bills_5 = []
    bills_10 = []
    for bill in bills:
        match bill:
            case 10:
                if len(bills_5) <= 0:
                    return False
                bills_10.append(bill)
                bills_5.pop()
            case 20:
                if len(bills_10) > 0:
                    if len(bills_5) <= 0:
                        return False
                    bills_10.pop()
                    bills_5.pop()
                elif len(bills_5) >= 3:
                    bills_5 = bills_5[:-3]
                else:
                    return False
            case _:
                bills_5.append(bill)
    return True


if __name__ == '__main__':
    res = lemonadeChange([5, 5, 10, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 20, 5, 20, 5])
    res
