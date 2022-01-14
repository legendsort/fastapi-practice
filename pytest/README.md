- 비동기 테스트(pytest)
    
    ## 실행 명령어
    
    ```
    $ pytest
    ```
    
    디렉토리 내 `test_*.py` 또는 `*_test.py` 파일을 모두 실행합니다.
    
    ```python
    
    from httpx import AsyncClient
    
    from .main import app
    
    @pytest.mark.anyio
    async def test_root():
        async with AsyncClient(app=app, base_url="http://test") as ac:
            response = await ac.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Tomato"}
    
    ---init.py
    aaaa = pytest.mark.skipif(True, reason="a test that must run to verify bridge interfaces")
    ---쓰는곳
    @aaa
    
    @pytest.fixture(autouse=True, scope='module') #scope는이 fixture하는 함수가 
    #테스트 모듈당 한번만 호출되는것
    #autouse는 자동사용설비(모든 테스트가 자동으로 요청 하도록 하는 편리한 방법, 많은 중복 요청을
    #차단 할 수 있고 고급 설비 사용 제공
    #scope = "session" : 픽스쳐는 테스트 세션이 끝나면 파괴됩니다.
    ```
    
    ### **FastAPI** 앱 파일[¶](https://fastapi.tiangolo.com/ko/tutorial/testing/#fastapi-app-file)
    
    하자 당신이 파일이 있다고 가정 해 `main.py`당신과 **FastAPI의** 응용 프로그램을 :
    
    ```python
    from fastapi import FastAPI
    
    app = FastAPI()
    
    @app.get("/")
    async def read_main():
        return {"msg": "Hello World"}
    ```
    
    ### 테스트 파일[¶](https://fastapi.tiangolo.com/ko/tutorial/testing/#testing-file)
    
    그런 다음 `test_main.py`테스트 가 포함된 파일 을 갖고 모듈( ) `app`에서 가져올 수 있습니다 .`mainmain.py`
    
    ```python
    from fastapi.testclient import TestClient
    
    from .main import app
    
    client = TestClient(app)
    
    def test_read_main():
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"msg": "Hello World"}
    ```
    
    ### GET POST 작업
    
    ```python
    @app.get("/items/{item_id}", response_model=Item)
    async def read_main(item_id: str, x_token: str = Header(...)):
        if x_token != fake_secret_token:
            raise HTTPException(status_code=400, detail="Invalid X-Token header")
        if item_id not in fake_db:
            raise HTTPException(status_code=404, detail="Item not found")
        return fake_db[item_id]
    @app.post("/items/", response_model=Item)
    async def create_item(item: Item, x_token: str = Header(...)):
        if x_token != fake_secret_token:
            raise HTTPException(status_code=400, detail="Invalid X-Token header")
        if item.id in fake_db:
            raise HTTPException(status_code=400, detail="Item already exists")
        fake_db[item.id] = item
        return item
    ```
    
    ### 테스트 파일
    
    ```python
    def test_read_item():
        response = client.get("/items/foo", headers={"X-Token": "coneofsilence"})
        assert response.status_code == 200
        assert response.json() == {
            "id": "foo",
            "title": "Foo",
            "description": "There goes my hero",
        }
    def test_read_item_bad_token():
        response = client.get("/items/foo", headers={"X-Token": "hailhydra"})
        assert response.status_code == 400
        assert response.json() == {"detail": "Invalid X-Token header"}
    
    def test_read_inexistent_item():
        response = client.get("/items/baz", headers={"X-Token": "coneofsilence"})
        assert response.status_code == 404
        assert response.json() == {"detail": "Item not found"}
    ```
    
    - pytest.raises
        - `function`: 기본 범위, 픽스처는 테스트가 끝나면 파괴됩니다.
        - `class`: 픽스쳐는 클래스의 마지막 테스트를 분해하는 동안 파괴됩니다.
        - `module`: 모듈의 마지막 테스트를 분해하는 동안 고정 장치가 파괴됩니다.
        - `package`: 패키지의 마지막 테스트를 분해하는 동안 고정물이 파괴됩니다.
        - `session`: 픽스쳐는 테스트 세션이 끝나면 파괴됩니다.

 