from carddeck import CardDeck

d1 = CardDeck('Nellie')
d2 = CardDeck('Andy')
print(d1, d2)

d1.shuffle()
for i in range(7):
    print(d1.draw())