import os
from dotenv import load_dotenv

envs = load_dotenv()

# class Config:
#     SECRET_KEY:str = envs.get('SECRET_KEY')
#     DEBUG:bool = envs.get('DEBUG')
#     SECRET_COOKIE:str = envs.get('SECRET_COOKIE')



# class DevConfig(Config):
#     SQLALCHEMY_DATABASE_URI:str = envs.get('SQLALCHEMY_DATABASE_URI')
#     SQLALCHEMY_TRACK_MODIFICATIONS:bool = envs.get('SQLALCHEMY_TRACK_MODIFICATIONS')