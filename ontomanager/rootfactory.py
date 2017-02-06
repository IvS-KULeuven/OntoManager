__author__ = 'wimpe'



from pyramid.security import (
    Allow,
    Everyone,
    )

class RootFactory(object):
    __acl__ = [ (Allow, Everyone, 'login'),
                (Allow, 'group:viewing' , 'view'),  # (Allow, Everyone, 'view')
                (Allow, 'group:querying', 'query'),  # (Allow, Everyone, 'view')
                (Allow, 'group:editing' , 'edit') ]
    def __init__(self, request):
        pass
