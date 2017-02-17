__author__ = 'wimpe'


from pyramid.security import Allow
from pyramid.security import Everyone


class RootFactory(object):
    __acl__ = [ (Allow, Everyone, 'login'),
                (Allow, 'group:viewing' , 'view'),
                (Allow, 'group:querying', 'query'),
                (Allow, 'group:editing' , 'edit') ]
    def __init__(self, request):
        pass
