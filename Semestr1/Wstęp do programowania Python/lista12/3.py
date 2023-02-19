def in_tree(tree, e):
    if tree == []:
        return False
    n, left, right = tree
    if n == e:
        return True
    if e < n:
        return in_tree(left, e)
    return in_tree(right, e)

def tree_to_list(tree):
    if tree == []:
        return []
    n, left, right = tree
    return tree_to_list(left) + [n] + tree_to_list(right)

def tree_size(tree):
    if tree == []:
        return 0
    wielkosc = 0
    for i in tree:
        if(type(i) == list):
            wielkosc += tree_size(i)
        else:
            wielkosc += 1
    return wielkosc

def tree_generator(tree):
    if tree == []:
        return
    n, left, right = tree
    for e in tree_generator(left):
        yield e
    yield n

    for e in tree_generator(right):
        yield e
    

def add_to_tree(e, tree):
    if tree == []:
        tree += [e, [], []]
        return
    x, left, right = tree
    if e < x:
        add_to_tree(e, left)
    elif e > x:
        add_to_tree(e, right)
   
def elements_of_tree(tree):
    if tree == []:
        return []
    elementy = []
    for i in tree:
        if(type(i) == list):
            for k in elements_of_tree(i):
                elementy.append(k)
        else:
            elementy.append(i) 
    return elementy


class Set:
    def __init__(self, *elems):
        self.tree = []
        for e in elems:
            self.add(e)
            
    def add(self, e):
        add_to_tree(e, self.tree)    
        
    def __contains__(self, e):
        return in_tree(self.tree, e) 
        
    def __str__(self):
        return f'Set({tree_to_list(self.tree)})'    
        
    def __or__(self, other):
        new = Set(*tree_to_list(self.tree))
        for e in tree_to_list(other.tree):
            new.add(e)
        return new 

    def __len__(self):
        return tree_size(self.tree)

    def __add__(self, other):
        elementy1 = elements_of_tree(self.tree)
        elementy2 = elements_of_tree(other.tree)
        for i in elementy2:
            if i not in elementy1:
                elementy1.append(i)
        return Set(elementy1)

    def __sub__(self, other):
        elementy1 = elements_of_tree(self.tree)
        elementy2 = elements_of_tree(other.tree)
        wynik = []
        for i in elementy1:
            if i not in elementy2:
                wynik.append(i)
        return Set(wynik)

        
    #def __iter__(self):
    #    return iter(tree_to_list(self.tree))  
    
    def __iter__(self):
        return tree_generator(self.tree)   

zbior = Set(1, 2, 3, 4, 4, 4, 4, 5, 10) 
zbior.add(6)
print(len(zbior))
zbior2 = Set(5, 6, 7)
zbior = zbior + zbior2
print(zbior)
zbior3 = Set(7, 8, 9, 10)
zbior = zbior - zbior3
print(zbior)