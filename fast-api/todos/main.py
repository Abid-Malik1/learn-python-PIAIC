from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def helloWorld():
    return"Hello Python Baby"
@app.post("/")
def helloWorld():
    return"Post Hello Python Baby"

@app.delete("/")
def helloWorld():
    return"Hello Python Baby is deleted"
@app.put("/")
def helloWorld():
    return"Put is called baby"

@app.get("/gettodos")
def getTodos():
    print("Get Todos is called")
    return"todos is called"

@app.post("/posttodos")
def getTodos():
    print("Get post Todos is called")
    return"post todos is called"

@app.get("/getsingletodos")
def getSingleTodo():
    print("Get  Single Todo is called")
    return "Get Single Todo is Called"

@app.get("/gettodos/{userName}/{password}")
def getTodos(userName, password):
    print("username is",userName)
    print("password is",password)
    return userName + password


def start():
    uvicorn.run("todos.main:app",host="127.0.0.1",port=7990, reload=True)

