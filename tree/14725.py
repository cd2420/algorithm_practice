# 개미굴

class Trie:
    def __init__(self):
        self.root = {0: True}

    def add(self, foods):
        check = self.root
        for food in foods:
            if food not in check:
                check[food] = {0: True}
                if 0 in check:
                    del check[0]
            check = check[food]

    def show(self, check, cnt):
        if 0 in check:
            return
        keys = sorted(check.keys())
        for k in keys:
            print("--" * cnt + k)
            self.show(check[k], cnt+1)
        


N = int(input())
foods = []
trie = Trie()
for _ in range(N):
    check = input().split()
    num = int(check[0])
    foods = check[1:]
    trie.add(foods)
trie.show(trie.root, 0)