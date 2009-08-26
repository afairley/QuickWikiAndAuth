<%inherit file="/base.mako"/>\

<%def name="header()">Editing ${c.title}</%def>

${h.secure_form(url('save_page', title=c.title))}
  ${h.textarea(name='content', rows=7, cols=40, content=c.content)} <br />
  ${h.submit(value='Save changes', name='commit')}
${h.end_form()}

