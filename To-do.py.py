


from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel


app=FastAPI()




class Todoitem(BaseModel):
    title:str
    completed:bool


Todos={
    1:{
        "title":"Finish Microcontrollers DA",
        "completed":False,
    },

    2:{
        "title":"Study for cryptography quiz",
        "completed":False,
    },

    3:{
        "title":"Prepare slides for IIP project presentation ",
        "completed":False,
    },

    4:{
        "title":"Prepare report for GDSC",
        "completed":True,
    }
}

@app.get("/todos",status_code=status.HTTP_200_OK)
def get_todo_items(title:str=""):
    results={}
    if title !="" or title!=None:
     for id in Todos:
        if title in Todos[id]["title"]:
            results[id]=Todos[id]
        
    else:
        results=Todos

    return results


@app.get("/todos/{id}",status_code=status.HTTP_200_OK)
def get_particular_todo_item(id:int):
    if id in Todos:
      return Todos[id]
    
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Task not found")


@app.post("/todos",status_code=status.HTTP_201_CREATED)
def create_todo_items(todo_item:Todoitem):
    id=max(Todos)+1
    Todos[id]=todo_item.dict()
    return Todos[id]



@app.put("/todos/{id}",status_code=status.HTTP_200_OK)
def update_todo_item(id:int,todo_item:Todoitem):
    if id in Todos:
     Todos[id]=todo_item.dict()
     return Todos[id]

    return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Task not found")

@app.delete("/todos/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_todo_item(id:int):
 if id in Todos:
    Todos.pop(id)
    return

 return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Task not found")
