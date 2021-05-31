from pyramid.config import Configurator
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy

from .ontomanager.configuration import groupfinder

from . import rootfactory

from pyramid.session import SignedCookieSessionFactory


def main(global_config, **settings):
    """
    This function returns a Pyramid WSGI application.
    """
    authn_policy = AuthTktAuthenticationPolicy('sosecret', callback=groupfinder, hashalg='sha512')
    authz_policy = ACLAuthorizationPolicy()

    sessionFactory = SignedCookieSessionFactory('itsaseekreet')

    config = Configurator(settings=settings,
                          root_factory='ontomanager.rootfactory.RootFactory',
                          session_factory = sessionFactory)
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)


    config.include('pyramid_chameleon')
    config.include('pyramid_mako')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_static_view('home', 'home', cache_max_age=3600)

    config.add_route('login', '/login')
    config.add_route('logout', '/logout')


    config.add_static_view('queries', 'queries/')
    config.add_static_view('templates', 'templates/')
    config.add_route('default', '/')
    config.add_route('home', '/home')
    config.add_route('models', '/models')
    config.add_route('cache', '/cache')
    config.add_route('config', '/config')
    config.add_route('dataset', '/dataset')
    config.add_route('browse', '/browse')
    config.add_route('query', '/query')
    config.add_route('problems', '/problems')
    config.add_route('sys', '/sys')
    config.add_route('mech', '/mech')
    config.add_route('elec', '/elec')
    config.add_route('soft', '/soft')
    config.add_route('org', '/org')
    config.scan()

    return config.make_wsgi_app()
