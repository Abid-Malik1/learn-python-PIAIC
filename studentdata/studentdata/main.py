from fastapi import FastAPI
import uvicorn

app = FastAPI()

students=[
    {
        "userName":"Abid Malik",
        "rollNo":79
    }
] 

@app.get("/students")
def getStudents():
    return students

@app.get("/studentdata")
def studentData():
    return studentData

@app.get("/addstudent")
def addStudent(userName, rollNo):
    global studentData
    studentData.append({"userName", userName, "rollNo", rollNo})
    return studentData



def start():
    uvicorn.run("studentdata.main:app",host="127.0.0.1",port=8000,reload=True)
    