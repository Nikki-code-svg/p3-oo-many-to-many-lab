
class Author:
    
    def __init__(self, name:str):
        self.name = name
        self._contracts = []
        
    def contracts(self):
       return self._contracts
    
    def books(self):
        return [ contract.book for contract in self._contracts ]

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        self._contracts.append(contract)
        return contract
        
    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)



class Book:
    
    def __init__(self, title):
        self.title = title
        self._contracts = []

    def contracts(self):
        return self._contracts
    
    def authors(self):
        return [ contract.author for contract in self._contracts ]
    

class Contract:


    all = []

    def __init__(self, author, book, date, royalties):
       if not isinstance(author, Author):
            raise TypeError("DID NOT RAISE type of AUTHOR")
       if not isinstance(book, Book):
            raise TypeError("DID NOT Raise type of book")
       if not isinstance(date, str):
            raise TypeError("Date must be a string")
       if not isinstance(royalties, int):
            raise TypeError("DID not put in correct type integer")
       self.author = author
       self.book = book
       self.date = date
       self.royalties = royalties
       Contract.all.append(self)
       author._contracts.append(self)
       book._contracts.append(self)

    def __repr__(self):
        return f"Contract(author={self.author} book={self.book} date={self.date} royalties={self.royalties})"
    

    @classmethod
    def contracts_by_date(cls, date):
         return [ contract for contract in cls.all if contract.date == date] 
      
        
    