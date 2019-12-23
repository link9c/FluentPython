import collections

# 带命名的元组
# Card = collections.namedtuple('card', ['rank', 'suit'])
Card = collections.namedtuple('card', 'rank suit')


class Deck(object):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]


if __name__ == '__main__':
    # 定义len和getitem方法实现迭代
    bear_card = Card('7', 'diamonds')
    print(bear_card)
    deck = Deck()
    print(len(deck))
    print(deck[0])
    print(deck[:3])
    print(deck[12::13])


    for card in reversed(deck):
        # doctest: +ELLIPSIS
        print(card)
