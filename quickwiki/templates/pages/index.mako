<%inherit file="/base.mako"/>\

<%def name="header()">Title List</%def>

${h.secure_form(url('delete_page'))}

<ul id="titles">
  % for title in c.titles:
    <li>
        ${h.link_to(title, url('show_page', title=title))} -
        ${h.checkbox('title', title)}
    </li>
    % endfor
</ul>

${h.submit('delete', 'Delete')}

${h.end_form()}

