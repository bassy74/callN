# coding: utf-8
# Your code here!
# coding: UTF-8

class Node:
    def __init__(self, data, turn): #コンストラクタ
        self.data = data
        self.turn = turn
        self.add1 = None
        self.add2 = None
        self.add3 = None
        self.add4 = None

class Tree:
    def __init__(self, number_list): #コンストラクタ
        self.root = None #ルートノード初期化
        for node in number_list: #数値を持つ配列から二分木を生成
            self.insert(node) #挿入メソッドを使ってノードを挿入する
            
    def insert(self, data):
        n = self.root
        
        if n == None:
            self.root = Node(data,1)
            return
        else:
            for i in range(6):
                turn = i + 1
                if n.turn == turn:
                    if n.add1 is None:
                        n.add1 = Node(n.data+1, turn+1)
                        return
                    else:
                        n = n.add1
                        
                    if n.add2 is None:
                        n.add2 = Node(n.data+2, turn+1)
                        return
                    else:
                        n = n.add2
                    
                    if n.add3 is None:
                        n.add3 = Node(n.data+3, turn+1)
                        return
                    else:
                        n = n.add3
                        
                    if n.add4 is None:
                        n.add4 = Node(n.data+4, turn+1)
                        return
                    else:
                        n = n.add4
                

iarray_A = list(range(1,30))

print(iarray_A)

tree = Tree(iarray_A)

print(tree)

#参考　https://qiita.com/menon/items/657f67bb2817e25b2222
