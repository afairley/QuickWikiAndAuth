from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1251319147.4375069
_template_filename='/home/vegas/Documents/Projects/venturebros/code/QuickWiki/quickwiki/templates/pages/edit.mako'
_template_uri='/pages/edit.mako'
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
        __M_writer(escape(h.secure_form(url('save_page', title=c.title))))
        __M_writer(u'\n  ')
        # SOURCE LINE 6
        __M_writer(escape(h.textarea(name='content', rows=7, cols=40, content=c.content)))
        __M_writer(u' <br />\n  ')
        # SOURCE LINE 7
        __M_writer(escape(h.submit(value='Save changes', name='commit')))
        __M_writer(u'\n')
        # SOURCE LINE 8
        __M_writer(escape(h.end_form()))
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'Editing ')
        __M_writer(escape(c.title))
        return ''
    finally:
        context.caller_stack._pop_frame()


