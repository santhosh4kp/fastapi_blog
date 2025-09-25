from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from enum import Enum


class Language(str, Enum):
    python = "python"
    javascript = "javascript"
    go = "go"
    rust = "rust"
    
class Comment(BaseModel):
    text: Optional[str] = None

class Blog(BaseModel):
    title: str= Field(min_length=5)
    content: Optional[str] = None
    is_active: bool
    language: Language=Language.python
    crated_at: datetime = Field(default_factory=datetime.now)
    comments: Optional[List[Comment]]
    

# first_blog=Blog(title="My first blog",  is_active=True)
# print(first_blog)

# import time
# time.sleep(5)

blog=Blog(title="seconf blog",  is_active=True, comments=[Comment(text="my first comment")])
print(blog)