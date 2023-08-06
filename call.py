from enum import Enum
from fastapi import FastAPI

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


class FoodEnum(str,Enum):
    fruits='fruits'
    vagetables='vagetables'
    dairy='dairy'

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