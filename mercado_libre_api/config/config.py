
config = {
    'db':{
        'user': 'userTest',
        'address': 'myMongoDB',
        'port': '27017',
        'password': 'securePass1408',
        'info': '',
        'option': '{ useNewUrlParser: true }',
        'db': 'aws'
    }
}

if 'urlMongo' not in config['db']:
    if config['db']['user'] != '':
        config['db']['urlMongo'] = 'mongodb://' + config['db']['user'] + ':' + config['db']['password'] + '@' + config['db']['address'] + ':' + config['db']['port'] + '/' + config['db']['info']
    else:
        config['db']['urlMongo'] = 'mongodb://' + config['db']['address'] + ':' + config['db']['port'] + '/' + config['db']['info']