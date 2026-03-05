from fastapi import APIRouter, HTTPException, status
from models.request import StoryRequest
from models.response import StoryResponse, StyleInfo, StylesResponse
from services.ai_service import generate_story

router = APIRouter(prefix="/story", tags=["Story"])

STYLES = [
    StyleInfo(name="funny",     description="Lighthearted story full of dev jokes and humor"),
    StyleInfo(name="serious",   description="Honest and sincere, acknowledges the hard work"),
    StyleInfo(name="sarcastic", description="Dripping with sarcasm and dry wit"),
    StyleInfo(name="brutal",    description="Ruthless, savage roast. Zero chill. Very rude."),
    StyleInfo(name="dramatic",  description="Epic, over-the-top cinematic narrative"),
]

@router.get("/styles", response_model=StylesResponse)
def get_styles():
    return StylesResponse(styles=STYLES)


@router.post("/generate", response_model=StoryResponse, status_code=status.HTTP_200_OK)
def generate(request: StoryRequest):
    try:
        result = generate_story(request)
        # the ** unpacks the dict returned by generate_story into keyword arguments. So {"story": "...", "style": "brutal", ...} becomes StoryResponse(story="...", style="brutal", ...)
        return StoryResponse(**result)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Story generation failed: {str(e)}"
        )