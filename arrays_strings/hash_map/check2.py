'''Item クラス'''
class Item:
    
    '''初期化メソッド'''
    def __init__(self, name, price):
        self.__data = {"name":name, "price":price} #辞書型のオブジェクト
    
    '''辞書の"name"キーの値は参照と変更が可能にします。'''
    @property
    def name(self):
        return self.__data["name"]
    
    @name.setter
    def name(self, value):
        self.__data["name"] = value
    
    '''辞書の"price"キーはgetterメソッドしか書かないのでリードオンリーになります。'''
    @property
    def price(self):
        return self.__data["price"]

watch = Item("Rolex", 100000)
# watch.price = 50000

for i in range(11):
    print(i, i//10, i%10)
l3 = [3, 'c', None]
l2 = [2,'b',l3]
l1 = [1,'a',l2]

print(l1)

lst = [
    [[0,'a'],[0,'aa'],[0,'aaa']],
    [[1,'b'],[1,'bb']],
    [None,None],
    [[2,'c']]
]
print(f'lst {lst}')
print(f'lst[0] {lst[0]} len(lst[0]) {len(lst[0])}')