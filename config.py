import os


class Config(object):
    # General
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # Database
    # [DB_TYPE] + [DB_CONNECTOR]: // [USERNAME]: [PASSWORD] @ [HOST]:[PORT] / [DB_NAME]
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://anonymous:@ensembldb.ensembl.org:3306/ensembl_website_97"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
