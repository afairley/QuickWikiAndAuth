from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1251321417.0916431
_template_filename='/home/vegas/Documents/Projects/venturebros/code/QuickWiki/quickwiki/templates/pages/index.mako'
_template_uri='/pages/index.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['header']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, '/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        url = context.get('url', UNDEFINED)
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'')
        # SOURCE LINE 2
        __M_writer(u'\n')
        # SOURCE LINE 3
        __M_writer(u'\n\n')
        # SOURCE LINE 5
        __M_writer(escape(h.secure_form(url('delete_page'))))
        __M_writer(u'\n\n<ul id="titles">\n')
        # SOURCE LINE 8
        for title in c.titles:
            # SOURCE LINE 9
            __M_writer(u'    <li>\n        ')
            # SOURCE LINE 10
            __M_writer(escape(h.link_to(title, url('show_page', title=title))))
            __M_writer(u' -\n        ')
            # SOURCE LINE 11
            __M_writer(escape(h.checkbox('title', title)))
            __M_writer(u'\n    </li>\n')
        # SOURCE LINE 14
        __M_writer(u'</ul>\n\n')
        # SOURCE LINE 16
        __M_writer(escape(h.submit('delete', 'Delete')))
        __M_writer(u'\n\n')
        # SOURCE LINE 18
        __M_writer(escape(h.end_form()))
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'Title List')
        return ''
    finally:
        context.caller_stack._pop_frame()


