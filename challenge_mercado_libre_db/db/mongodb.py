from config.config import config
from pymongo import MongoClient

class mongoDB(object):
    _client = MongoClient(config['db']['urlMongo'])
    db = _client[config['db']['db']]