# BaseModel is the base class for all Pydantic models. Field lets you add extra rules and metadata to a field
from pydantic import BaseModel, Field
# Literal lets you restrict a field to specific allowed values only. If the client sends anything outside those values, Pydantic rejects it with a 422 automatically — no if/else needed.
from typing import Literal

class StoryRequest(BaseModel):
    # The ... (called Ellipsis in Python) means this field is required — no default, client must send it. If they don't, Pydantic returns a 422 error immediately.
    git_log: str = Field(
        ...,
        min_length=10,
        description="The git log to be processed. Required.",
        examples=["a1b2c3 Fix login bug\nb2c3d4 Add dark mode"]
        )
    style : Literal['funny', 'serious', 'sarcastic', 'brutal', 'dramatic'] = Field(
        default='brutal',
        description="Narrative style for the story"
    )
    max_words: int = Field(
        default=100,
        ge=50,
        le=1000,
        description="Approximate word count of the story"
    )
