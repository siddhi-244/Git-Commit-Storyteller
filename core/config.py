from pydantic_settings import BaseSettings

# BaseSettings has all the env reading and validation
class Settings(BaseSettings):
    # required environment variable - else app will crash
    groq_api_key:str
    app_name:str = "Git Commit StoryTeller"
    model:str = "llama3-8b-8192"
    # if .env has MAX_TOKENS=500, pydantic auto-converts the string "500" to the integer 500.
    max_tokens:int = 1024

    # tells BaseSettings where to look for environment variables
    class Config:
        env_file = ".env"
#  it runs validation immediately when the module is imported
settings = Settings()
