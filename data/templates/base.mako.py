from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1251322092.5877111
_template_filename='/home/vegas/Documents/Projects/venturebros/code/QuickWiki/quickwiki/templates/base.mako'
_template_uri='/base.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['footer']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        next = context.get('next', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"\n  "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">\n  <html>\n    <head>\n        <title>QuickWiki</title>\n            ')
        # SOURCE LINE 6
        __M_writer(escape(h.stylesheet_link('/quick.css')))
        __M_writer(u'\n              </head>\n\n                <body>\n                    <div class="content">\n                          <h1 class="main">')
        # SOURCE LINE 11
        __M_writer(escape(self.header()))
        __M_writer(u'</h1>\n\n                          ')
        # SOURCE LINE 13
        flashes = h.flash.pop_messages() 
        
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin()[__M_key]) for __M_key in ['flashes'] if __M_key in __M_locals_builtin()]))
        __M_writer(u'\n')
        # SOURCE LINE 14
        if flashes:
            # SOURCE LINE 15
            for flash in flashes:
                # SOURCE LINE 16
                __M_writer(u'                            <div id="flash">\n                                <span class="message">')
                # SOURCE LINE 17
                __M_writer(escape(flash))
                __M_writer(u'</span>\n                            </div>\n')
        # SOURCE LINE 21
        __M_writer(u'                                ')
        __M_writer(escape(next.body()))
        __M_writer(u'')
        # SOURCE LINE 22
        __M_writer(u'                                      <p class="footer">\n                                      ')
        # SOURCE LINE 23
        __M_writer(escape(self.footer(request.environ['pylons.routes_dict']['action'])))
        __M_writer(u'')
        # SOURCE LINE 24
        __M_writer(u'                                                                            </p>\n                    </div>\n                </body>\n</html>\n\n')
        # SOURCE LINE 38
        __M_writer(u' \n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context,action):
    context.caller_stack._push_frame()
    try:
        url = context.get('url', UNDEFINED)
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 29
        __M_writer(u'')
        # SOURCE LINE 30
        __M_writer(u'        Return to the ')
        __M_writer(escape(h.link_to('FrontPage', url('home'))))
        __M_writer(u'\n')
        # SOURCE LINE 31
        if action == "index":
            # SOURCE LINE 32
            __M_writer(u'            ')
            return 
            
            __M_writer(u'\n')
        # SOURCE LINE 34
        if action != 'edit':
            # SOURCE LINE 35
            __M_writer(u'          | ')
            __M_writer(escape(h.link_to('Edit ' + c.title, url('edit_page', title=c.title))))
            __M_writer(u'\n')
        # SOURCE LINE 37
        __M_writer(u'          | ')
        __M_writer(escape(h.link_to('Title List', url('pages'))))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


