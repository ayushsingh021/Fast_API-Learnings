from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {"title" : "Title one" , "author" : "Author one" , "category" : "science" },
    {"title" : "Title two" , "author" : "Author two" , "category" : "math" },
    {"title" : "Title three" , "author" : "Author three" , "category" : "literature" },
    {"title" : "Title four" , "author" : "Author four" , "category" : "math" },
    {"title" : "Title five" , "author" : "Author five" , "category" : "science" },
    {"title" : "Title six" , "author" : "Author six" , "category" : "bio" },

]
##########################   Path Paramter ###########################################

@app.get("/books")

async def get_all_books():
    
    return BOOKS;

# 


@app.get("/books/{book_title}")

async def get_fav_book(book_title:str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book


@app.get("/books/{dyanamic_param}")

#give explicit type for error handling
async def get_books(dyanamic_param:str):
    return {"dyanamic_param" : dyanamic_param}


##########################   query Paramter ###########################################
# http://127.0.0.1:8000/books/?category=math -- creates this type of url
@app.get("/books/")
#query_paramneters
async def read_category_by_query(category: str):
    books_to_ret = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_ret.append(book)
    
    return books_to_ret

###### Both using path and query parameter ####################

@app.get("/books/{author_name}/")

async def read_author_category_by_query(author_name:str , category_name:str):
    ans_books = []
    for book in BOOKS:
        if book.get("author").casefold() == author_name.casefold() and \
                book.get("category").casefold() == category_name.casefold():
             ans_books.append(book)
        
        return ans_books