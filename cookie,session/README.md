- 의존성,종속성
    
    ```python
    from fastapi import Depends, FastAPI
    async def common_parameters(q: Optional[str] = None, skip: int = 0, limit: int = 100):
        return {"q": q, "skip": skip, "limit": limit}
    
    @app.get("/items/")
    async def read_items(commons: dict = Depends(common_parameters)):
        return commons
    #Depends는 하나의 매개변수만 제공
    #----------------클래스의 경우
    class CommonQueryParams:
        def __init__(self, q: Optional[str] = None, skip: int = 0, limit: int = 100):
            self.q = q
            self.skip = skip
            self.limit = limit
    #----------------똑같이 작용
    #쓰는 대신:
    
    commons: CommonQueryParams = Depends(CommonQueryParams)
    #...당신은 쓰기:
    commons: CommonQueryParams = Depends()
    ```
    
- 쿠키,세션