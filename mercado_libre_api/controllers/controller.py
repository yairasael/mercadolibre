from flask import jsonify
from utils.utils import Utils


class Search(object):
    def searchCost(params):
        try:
            id = params.get('instanceId')
            if id != '':
                search = Utils.searchCost(id)
                if search is not False:
                    return jsonify({
                        'costo': search['cost']
                    })
                else:
                    return jsonify({
                        'success': False,
                        'response': 'No id Found'
                    })
            else:
                return jsonify({
                    'success': False,
                    'response': 'No id Found'
                })
        except ValueError as err:
            print(err)
            return jsonify({
                'error': err,
                'success': False,
            })
