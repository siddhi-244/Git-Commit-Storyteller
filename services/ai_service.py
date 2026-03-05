from groq import Groq
from core.config import settings
from models.request import StoryRequest

client = Groq(api_key=settings.groq_api_key)

# Set Ai's personality
STYLE_PROMPTS = {
    "funny":    "You are a comedian writer. Write a funny, lighthearted story full of dev jokes and humor.",
    "serious":   "You are a thoughtful writer. Write an honest, sincere story that is somewhat sweet and acknowledges the hard work behind each commit.",
    "sarcastic": "You are a sarcastic writer. Write a story dripping with sarcasm and dry wit about the developer's choices.",
    "brutal":    "You are a ruthless, savage roast comedian. You have absolutely zero chill. Rip apart every commit decision with brutal, rude, no-holds-barred roasting. Be mean, be harsh, be hilarious. Do not hold back.",
    "dramatic":  "You are a dramatic Hollywood screenwriter. Write an epic, over-the-top cinematic narrative.",
}

def build_prompt(request: StoryRequest) -> str:
    commit_lines = [
        line.strip() 
        for line in request.git_log.strip().splitlines()
        if line.strip()
    ]
    commits_text = "\n".join(commit_lines)
    return f"""
You are given the following git commit history of a software project: 
{commits_text}
Turn this into a {request.style} story in approximately {request.max_words} words.
Each commit is a chapter or moment in the story.
Be creative. Be vivid. Make it entertaining.
Only return the story, nothing else.
""".strip()

def count_commits(git_log: str) -> int:
    return len([
        line for line in git_log.strip().splitlines()
        if line.strip()
    ])

def generate_story(request: StoryRequest) -> dict:
    prompt = build_prompt(request)
    system_prompt = STYLE_PROMPTS[request.style]

    chat = client.chat.completions.create(
        model=settings.model,
        max_tokens=settings.max_tokens,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": prompt},
        ]
    )
    story = chat.choices[0].message.content.strip()
    return {
        "story": story,
        "style": request.style,
        "commit_count": count_commits(request.git_log),
        "word_count": len(story.split()),
    }


