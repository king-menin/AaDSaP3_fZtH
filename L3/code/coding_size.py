import sys
import chardet


beer = "🍺 some"
print([sys.getsizeof(beer[:index]) for index in range(len(beer) + 1)])
easy = "easy"
изич = "изич"
易易易易 = "易易易易"
print([sys.getsizeof(easy[:index]) for index in range(len(easy) + 1)])
print([sys.getsizeof(изич[:index]) for index in range(len(изич) + 1)])
print([sys.getsizeof(易易易易[:index]) for index in range(len(易易易易) + 1)])
print(sys.getsizeof(изич + easy), sys.getsizeof(易易易易 + изич + easy))
print(chardet.detect(easy.encode()), chardet.detect(изич.encode()), chardet.detect(易易易易.encode()))
