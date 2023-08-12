from enum import Enum
from anyio import Path
from fastapi import FastAPI, Query
from pydantic import BaseModel

app= FastAPI()

#fonksiyon çağrımızın kullanılmadığı durumlarda ,
# deprecated=True ifadesini yazmamız yeterli olacaktır.
@app.get('/', description='This is our first route')
async def base_get_root():
    return {'message': 'Hello World', }

@app.post('/')
async def post():
    return {'message':'Hello from the post root'}

@app.put('/')
async def put():
    return {'message':'Hello from the put root'}

@app.get('/users')
async def items():
    return {'message':'Hello from list items'}

@app.get('/users/{user_id}')
async def get_item(user_id:int ):
    return {'item_id':user_id}

#Bir class tanımlarız değişken ekleriz
class FoodEnum(str,Enum):
    fruits='fruits'
    vagetables='vagetables'
    dairy='dairy'
#get işlemi ile class içindeki tüm elemanları görüntüleriz.
@app.get('/food/{food_name}')
async def get_food(food_name:FoodEnum):
    if food_name == FoodEnum.vagetables:
        return {'food_name':food_name,'message':'you are healthy'}

    if food_name.value == 'fruits':
        return {'food_name':food_name,
                'message':'you are still healthy , but likes sweet things.'}
    return {food_name:'food_name','message':'I like chocolate milk'}


fake_item_list=[{'item_name':'BMW'},{'item_name':'mercedes'}]
@app.get('/items')
async def list_items(skip: int=5,limit: int=10):
    return fake_item_list[ skip: skip + limit]


@app.get('/items/{item_id}')
async def getget_item(item_id:str,q:str| None=None, short:bool = False):
    item={'item_id':item_id}
    if q:
        item.update({'q':q})
    if not short:
        item.update({'deseription':'Lorem ipsum anfcjdbvbhfbsdhfbhdfbshdf'})
    return item

@app.get('/users/{user_id}/items/{item_id}')
async def get_users_item(user_id: int,item_id: str ,q:str| None=None, short:bool = False ):
    item={'item_id':item_id, 'owner_id':user_id}
    if q:
        item.update({'q':q})
    if not short:
        item.update({'deseription':'Lorem ipsum anfcjdbvbhfbsdhfbhdfbshdf'})
        return item
    

#import baseModel
class Item(BaseModel):
    name:str
    description:str | None=None
    price:float
    tax:float | None=None

# @app.post('/items')
# async def create_items(item: Item):
#     if  item==Item.name :
#          return{"item":item,"message":"This is a message Item class"}

@app.post('/items')
async def create_items(item: Item):
    item_dict = item.dict()
    if  item.tax :
         price_with_tax =item.price + item.tax
         item_dict.update({"price_with_tex":price_with_tax})
         return item_dict
    
# @app.put("/items/{item_id}")
# async def create_item_with_put(item_id=int,item : Item,q:str |None:None):
#     result ={"item_id":item_id,**item_dict()}
#     if q:
#          result.update({"q":q})
#     return result

@app.get("/items")
async def read_items(q:str = Query(None, 
                                   min_length=4,max_length=10,
                                   title="Sample query string",
                                   description='This is a sample query string.',
                                   alias="item-quey",
                                   deprecated=True)):
    results = {"items":[{"item_id":"Foo"}, {"item_id":"Bar"}]}
    #items değerine liste elemanlarını atıyoruz.
    if q:#parametre olarak girilen değer ise
        results.update({"q":q})
        return results
    
# @app.get("/items_validation/{item_id}")
# async def read_items_validation(
#     *,
#     item_id: int= Path(..., title= "The ID of the item to get", ge=10,le=100),
#     q:str,
# ):
#     results = {"item_id":item_id}
#     if q:
#          results.update({"q":q})
#     return results