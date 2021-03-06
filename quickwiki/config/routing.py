"""Routes configuration

The more specific and detailed routes should be defined first so they
may take precedent over the more generic routes. For more information
refer to the routes manual at http://routes.groovie.org/docs/
"""
from pylons import config
from routes import Mapper

def make_map():
    """Create, configure and return the routes Mapper"""
    map = Mapper(directory=config['pylons.paths']['controllers'],
                 always_scan=config['debug'])
    map.minimization = False

    # The ErrorController route (handles 404/500 error pages); it should
    # likely stay at the top, ensuring it can always be resolved
    map.connect('/error/{action}', controller='error')
    map.connect('/error/{action}/{id}', controller='error')

    # CUSTOM ROUTES HERE
    map.connect('envirodump', '/envirodump', controller='envirodump', action='index')
    map.connect('home', '/', controller='pages',action='show',
                title='FrontPage')
    map.connect('pages', '/pages', controller='pages', action='index')
    map.connect('show_page', '/pages/show/{title}', controller='pages',
                action='show')
    map.connect('edit_page', '/pages/edit/{title}', controller='pages',
                action='edit')
    map.connect('save_page', '/pages/save/{title}', controller='pages',
                action='save', conditions=dict(method='POST'))
    map.connect('delete_page', '/pages/delete', controller='pages',
                action='delete')
    map.connect('/{title}', controller='pages', action='show')

    #map.connect('/{controller}/{action}')
    #map.connect('/{controller}/{action}/{id}')

    return map
