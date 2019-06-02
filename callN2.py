class Node:
    def __init__(self, data, turn): #コンストラクタ
        self.data = data
        self.turn = turn
        self.add1 = None
        self.add2 = None
        self.add3 = None
        self.add4 = None

class Tree:
    def __init__(self,M): #コンストラクタ
        self.root = Node(0,0) #ルートノード初期化
        self.call(M) #挿入メソッドを使ってノードを挿入する
            
            
    def insert(self, M):
        n = self.root
        while :
            branch(n, M)
            
        
        
        
    def branch(self, n, M):
        entry = n.data
        while entry < M:
            while n.data < M:
                n.add1 = Node(n.data+1, n.turn+1)
                n.add2 = Node(n.data+2, n.turn+1)
                n.add3 = Node(n.data+3, n.turn+1)
                n.add4 = Node(n.data+4, n.turn+1)
                
            return(n.add1, n.add2, n.add3, n.add4)



tree = Tree(6)



#参考　https://qiita.com/menon/items/657f67bb2817e25b2222
