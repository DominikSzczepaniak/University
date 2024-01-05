import unittest
from src import zad



class DataTests(unittest.TestCase):
    def test_one(self):
        zad.add_friend("Jan", "jan@localhost")  
        assert zad.delete_friend(zad.get_friend_id("Jan", "jan@localhost")) == True

    def test_two(self):
        zad.add_book("Pan Tadeusz", 1834, "Adam Mickiewicz")
        assert zad.delete_book(zad.get_book_id("Pan Tadeusz", 1834, "Adam Mickiewicz")) == True
    
    def test_three(self):
        assert zad.delete_friend(-3) == False


    

class InteractionTests(unittest.TestCase):
    def test_one(self):
        zad.add_book("Pan Tadeusz", 1834, "Adam Mickiewicz")
        zad.add_friend("Jan", "jan@localhost")
        zad.add_friend("Marek", "marek@localhost")
        assert zad.borrow_book("Jan", "Pan Tadeusz", 1834) == True
        assert zad.borrow_book("Marek", "Pan Tadeusz", 1834) == False
        assert zad.return_book("Marek", "Pan Tadeusz", 1834) == False
        assert zad.return_book("Jan", "Pan Tadeusz", 1834) == True
        zad.delete_friend(zad.get_friend_id("Jan", "jan@localhost"))
        zad.delete_friend(zad.get_friend_id("Marek", "marek@localhost"))
        zad.delete_book(zad.get_book_id("Pan Tadeusz", 1834, "Adam Mickiewicz"))

    def test_two(self):
        zad.add_book("Pan Tadeusz", 1834, "Adam Mickiewicz")
        zad.add_friend("Jan", "jan@localhost")
        zad.add_friend("Marek", "marek@localhost")
        zad.delete_book(zad.get_book_id("Pan Tadeusz", 1834, "Adam Mickiewicz"))
        assert zad.borrow_book("Jan", "Pan Tadeusz", 1834) == False
        zad.delete_friend(zad.get_friend_id("Jan", "jan@localhost"))
        zad.delete_friend(zad.get_friend_id("Marek", "marek@localhost"))

    def test_three(self):
        zad.add_book("Pan Tadeusz", 1834, "Adam Mickiewicz")
        zad.add_friend("Jan", "jan@localhost")
        zad.delete_friend(zad.get_friend_id("Jan", "jan@localhost"))
        assert zad.borrow_book("Jan", "Pan Tadeusz", 1834) == False
        zad.delete_book(zad.get_book_id("Pan Tadeusz", 1834, "Adam Mickiewicz"))
    
                        

if __name__ == "__main__":
    unittest.main()