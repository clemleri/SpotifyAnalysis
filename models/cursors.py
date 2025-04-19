from pydantic import BaseModel

class Cursors(BaseModel):
    after : str
    before : str