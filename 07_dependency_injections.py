from fastapi import FastAPI, Depends, HTTPException, status

blogs = {
    "1": "Sfirst blog hai",
    "2": "Second blog hai",
    "3": "Third blog hai"
}


user = {
    "8": "santhosh",
    "9": "sam"
    }

app = FastAPI(title="Dependency Injection Example")

# def get_obj_or_404(id: str):
#     obj = blogs.get(id)
#     if not obj:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Object with id {id} not found ")
#     return obj

class GetOjector404:
    def __init__(self, model)-> None:
        self.model = model
    def __call__(self, id: str  ):
        obj = self.model.get(id)
        if not obj:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Object with id {id} not found ")
        return obj

blog_dependency = GetOjector404(blogs)
user_dependency = GetOjector404(user)


@app.get("/blog/{id}")
def get_blog(blog_name: str = Depends(blog_dependency)):
    return blog_name


@app.get("/user/{id}")
def get_blog(user_name: str = Depends(user_dependency)):
    return user_name