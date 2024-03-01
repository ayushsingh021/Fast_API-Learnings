from fastapi import Body,FastAPI

app = FastAPI()

BOOKS = [
    {"title" : "Title one" , "author" : "Author one" , "category" : "science" },
    {"title" : "Title two" , "author" : "Author two" , "category" : "math" },
    {"title" : "Title three" , "author" : "Author three" , "category" : "literature" },
    {"title" : "Title four" , "author" : "Author four" , "category" : "math" },
    {"title" : "Title five" , "author" : "Author five" , "category" : "science" },
    {"title" : "Title six" , "author" : "Author six" , "category" : "bio" },

]

##################################### GET ~ READ ##################################

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


##################################### POST ~ WRITE ##################################

############################################# POST ##############################

# Body is complete empty sort of text field 
@app.post("/books/create_book")
async def create_book(new_book = Body()):
    BOOKS.append(new_book)


##################################### PUT ~ UPDATE ##################################

@app.put("/books/update_book")

async def update_book(updated_book = Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book


##################################### DELETE ##################################

@app.delete("/books/delete_book/{book_title}")

async def delete_book(book_title:str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break
