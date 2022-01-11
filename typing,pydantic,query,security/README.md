- typing,pydantic
    
    ### Optional 이란 None이 허용되는 타입
    
    `def repeat(message: str, times: Optional[int] = None) -> list:`
    
    여기서 → 명시하는건 리턴 값 명시해준다
    
    ```python
    from typing import Optional
    from fastapi import FastAPI
    from pydantic import BaseModel
    app = FastAPI()
    
    class Item(BaseModel):
        name:str
        price:float
        is_offer:Optional[bool] = None
    
    @app.get("/")
    def read_root():
        return {"Hello":"World"}
    @app.get("/items/{item_id}")
    def read_item(item_id: int, q:Optional[str] = None):
        return {"item_id":item_id,"q":q}
    @app.put("/items/{item_id}")
    def update_item(item_id:int, item:Item):
        return {
            "item_name":item.name,
            "item_id":item_id
        }
    ```
    
- 쿼리 매개변수
    
    ```python
    @app.get("/items/") #뒤에 / 붙여서
    async def read_item(skip: int = 0, limit: int = 10):
        return fake_items_db[skip : skip + limit]
    #http://127.0.0.1:8000/items/?skip=0&limit=10
    ```
    
- 추가검증(문자열 길이)
    
    ```python
    from typing import Optional
    
    from fastapi import FastAPI, Query
    
    app = FastAPI()
    
    @app.get("/items/")
    async def read_items(q: Optional[str] = Query(None, max_length=50)):
        results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
        if q:
            results.update({"q": q}) # update함수는 키가 없는 값일때
        return results
    #async def read_items(q: Optional[str] = Query(None, min_length=3, max_length=50)):
    #async def read_items(q: Optional[List[str]] = Query(None)):
    {
      "q": [
        "foo",
        "bar"
      ]
    }
    ```
    
- 보안
    
    ## OAuth2[¶](https://fastapi.tiangolo.com/ko/tutorial/security/#oauth2)
    
    OAuth2는 인증 및 권한 부여를 처리하는 여러 방법을 정의하는 사양입니다.
    
    상당히 광범위한 사양이며 여러 복잡한 사용 사례를 다룹니다.
    
    여기에는 "제3자"를 사용하여 인증하는 방법이 포함됩니다.
    
    이것이 "Facebook, Google, Twitter, GitHub로 로그인"이 있는 모든 시스템이 아래에서 사용하는 것입니다.
    
    ```python
    @app.post("/token")
    async def login(form_data: OAuth2PasswordRequestForm = Depends()):
        user_dict = fake_users_db.get(form_data.username)
    ```