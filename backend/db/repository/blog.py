from sqlalchemy.orm import Session
from schemas.blog import CreateBlog,UpdateBlog
from db.models.blog import Blog

def create_new_blog(blog: CreateBlog, db:Session, author_id=1):
    blog=Blog(title=blog.title,
              slug= blog.slug,
              content=blog.content,
              owner_id=author_id)              
    
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog

def retreive_blog(id:int, db:Session):
    blog=db.query(Blog).filter(Blog.id==id).first()
    return blog

def list_blogs(db: Session):
    blogs=db.query(Blog).filter(Blog.is_active==True).all()
    return blogs

def update_blog_by_id(id: int, blog:UpdateBlog, db:Session, author_id:int=1):
    blog_in_db=db.query(Blog).filter(Blog.id==id).first()
    if not blog_in_db:
        return
    blog_in_db.title=blog.title
    blog_in_db.content=blog.content
    db.add(blog_in_db)
    db.commit()
    db.refresh(blog_in_db)
    return blog_in_db
    
def delete_by_id(id:int, db:Session,author_id:int=1):
    blog_in_db=db.query(Blog).filter(Blog.id==id)
    if not blog_in_db.first():
        return {"error": f"Cound not find the blog with id {id}"}
    blog_in_db.delete()
    db.commit()
    return {"msg": f"deleted the entry with id {id}"}
    