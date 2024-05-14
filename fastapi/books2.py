from typing import Optional
from fastapi import FastAPI

from pydantic import BaseModel, Field
#BaseModel - used for data validation the object that we are giving is valid or not
#Field - 
app = FastAPI()


class Book:
    id :int
    title : str
    author : str
    description : str
    rating : int

    def __init__(self , id, title, author , description , rating) -> None:
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


class BookRequest(BaseModel):
    id : Optional[int] = Field("Not required to enter")
    title : str = Field(min_length=3)
    author : str = Field(min_length= 1)
    description : str = Field(min_length=1 , max_length=160)
    rating : int = Field(gt=0 , lt=100) #gt -greater than #lt- less than
    

class Config:
    schema_extra = {
        "example":{
            "title" : "A new Book",
            "author" : "dark_comder",
            "description": "A new desc of the book",
            "rating" : 5  
        }
    }

BOOKS = [
    Book(1,"DSA" , "N.K" , "Nice book for dsa" , 5),
    Book(2,"Cracking the coding interview" , "Powell" , "Nice book for interview" , 4),
    Book(3,"Rich dad" , "Nads" , "Nice book for richs" , 9),
    Book(4,"Money" , "john" , "Nice book for none" , 4),
    Book(5,"CP" , "don" , "Nice book for CP" , 8),
    Book(6,"Dev" , "bunny" , "Nice book for dev" , 5)
]

@app.get("/books")

async def get_all_books():
    return BOOKS

@app.post("/books/create_book")
# BookRequest is data validation part
async def create_book(book_request : BookRequest):
    # print(type(book_request))
    new_book = Book(**book_request.model_dump()) #**book_request.model_dump() --converting the req to book object
    BOOKS.append(gen_book_id(new_book))

def gen_book_id(book : Book):
    if len(BOOKS) > 0:
        book.id = BOOKS[-1].id + 1
    else:
        book.id = 1
    
    return book

@app.get("/books/read_books/{book_id}")

async def read_book(book_id: int):
    for book in BOOKS:
        if book.id == book_id:
            return book
