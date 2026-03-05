from pydantic import BaseModel

# This defines the shape of what we send back to the client. FastAPI will serialize this to JSON automatically.
class StoryResponse(BaseModel):
    story: str
    style: str
    commit_count: int
    word_count: int

class StyleInfo(BaseModel):
    name: str
    description: str

class StylesResponse(BaseModel):
    styles: list[StyleInfo]