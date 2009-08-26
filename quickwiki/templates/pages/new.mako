<%inherit file="/base.mako"/>\

<%def name="header()">${c.title}</%def>

<p>This page doesn't exist yet.
  <a href="${url('edit_page', title=c.title)}">Create the page</a>.
</p>

