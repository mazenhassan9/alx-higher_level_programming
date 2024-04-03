def list_division(mylist1, mylist2, L):
    new = []
    for x in range(L):
        try:
            d = mylist1[x] / mylist2[x]
        except (TypeError):
            print("wrong type")
            d = 0
        except (ZeroDivisionError):
            print("division by 0")
            d = 0
        except (IndexError):
            print("out of range")
            d = 0
        finally:
            new.append(d)
    return (new)
