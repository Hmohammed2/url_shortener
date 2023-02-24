from pydantic import BaseModel

class URLBase(BaseModel):
    target_url: str

class URL(URLBase):
    is_active: bool         # allows you to deactivate the shortened url
    clicks: int         # allows you to record how many times the shortened url has been visited

    class Config:
        # ORM = Object relational mapping. Provides the means to interact with a database using OOP approach
        orm_mode = True

class URLinfo(URL):
    url: str
    url_string: str