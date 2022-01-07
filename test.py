from pymongo import MongoClient
from fastapi import FastAPI,Query
import pprint

app = FastAPI()


@app.get("/")
def read_root():
    
    client = MongoClient()
    client = MongoClient('localhost',27017)

    db = client['test']
    print(db['test'].find({'a':'1'}))
    pprint.pprint(db['test'].find_one({'a':"1"}))
    return {"Hello":"World"}

    


if __name__ =="__main__":
    app.run(debug=True)