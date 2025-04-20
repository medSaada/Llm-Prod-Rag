from pydantic_settings import BaseSettings, SettingsConfigDict

#class inherits from BaseSettings (so that i can deal with it like a settings class)
#pydantic-settings require to define a Config class so that it can read the .env file

class Settings(BaseSettings):

    OPENAI_API_KEY: str
    APP_NAME: str
    APP_VERSION: str
    

    class Config:
        env_file = ".env"
        #all what is in the env file will be read and converted to the settings class
    

def get_settings():
    #this function will be used to get the settings creating a one instance of the settings class
    return Settings()
