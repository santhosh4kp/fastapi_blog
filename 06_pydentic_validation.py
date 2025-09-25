from pydantic import BaseModel, Field, field_validator, root_validator, model_validator
from typing import List, Optional

class CreateUser(BaseModel):
    email: str
    password: str
    confirm_password: str   
    
    @field_validator('email')
    def email_must_contain_at_symbol(cls, v):
        if '@' not in v:
            raise ValueError('Invalid email address')
        if 'admin' in v:
            raise ValueError('Invalid email address')
        return v

    @model_validator(mode='after')
    def passwords_match(cls, model):
        if model.password != model.confirm_password:
            raise ValueError('Passwords do not match')
        return model


user=CreateUser(password="password123", confirm_password="password123", email="san@gmail.com")
# ...existing code...
print(user)

# user_1=CreateUser(password="password123", confirm_password="password123", email="san_admin@gmail.com")
# # ...existing code...
# print(user_1)