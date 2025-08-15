from pydantic import BaseModel, EmailStr
try:
    # Pydantic v2
    from pydantic import ConfigDict
    V2 = True
except Exception:
    V2 = False

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str

    if V2:
        # v2 style
        model_config = ConfigDict(from_attributes=True)  # type: ignore
    else:
        # v1 fallback
        class Config:
            orm_mode = True
