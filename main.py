from fastapi import FastAPI
from uuid import UUID

app = FastAPI()



students = {}

student_data = { 
}


@app.post("/students")
def create_student(name: str, age: int, sex: str, height: float):

    new_student = student_data.copy()
    id = len(students) + 1
    uuid_ = str(UUID(int=id))
    new_student["id"] = uuid_
    new_student["name"] = name
    new_student["age"] = age
    new_student["sex"] = sex
    new_student["height"] = height 

    students[new_student["id"]] = new_student
    return {"message": "Student created successfully", "data": new_student}


@app.get("/students")
def get_students():
    return {"message": "successful", "data": students}

@app.get("/students/{id}")
def get_student(id):
    student = students.get(id)
    if not student:
        return {"error": "student not found!"}
    
    return {"message": "successful", "data": student}

@app.put("/students/{id}")
def update_student(id: str, name: str, age: int, sex: str, height: float):
     student = students.get(id)

     if not student:
        return {"error": "student not found!"}
     
     student["name"] = name
     student["age"] = age
     student["sex"] = sex
     student["height"] = height

     return {"message": "student updated successfully", "data": student}

@app.delete("/students/{id}")
def delete_student(id: str):
    student = students.get(id)
    if not student:
        return {"error": "student not found"}
    
    del students[id]
    return {"message": "student deleted successfully"}