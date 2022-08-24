from db.mongodb import mongoDB


class Utils(object):
    def searchCost(id):
        try:
            db = mongoDB.db['cost']
            if db is not None:
                search = db.find_one({'name': id})
                if search is not None:
                    return search
                else:
                    return False
            else:
                return False
        except ValueError as err:
            return False