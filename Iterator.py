cards = ["Yuriko" , "Arahbo", "Miirym", "Nalia", "Dogmeat"]

itCards = iter(cards)

"""print(next(itCards))
print(next(itCards))
print(next(itCards))
print(next(itCards))
print(next(itCards))"""

while itCards:
    try:
        print(next(itCards))
    except StopIteration:
        print("Fim da lista")
        break