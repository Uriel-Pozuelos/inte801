from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    SECRET_KEY: str = os.getenv('SECRET_KEY')
    DEBUG: bool = os.getenv('DEBUG').lower() == 'true'  # Convierte a booleano
    SECRET_COOKIE: str = os.getenv('SECRET_COOKIE')
    RECAPTCHA_PUBLIC_KEY: str = os.getenv('RECAPTCHA_PUBLIC_KEY')
    RECAPTCHA_PRIVATE_KEY: str = os.getenv('RECAPTCHA_PRIVATE_KEY')


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI: str = 'mysql+pymysql://root:root@127.0.0.1:3306/dream'
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS').lower() == 'true'  # Convierte a booleano
