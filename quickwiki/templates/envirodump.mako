<%inherit file="/base.mako"/>\
<%def name="header()">Less messy pylons environment dump</%def>

Hello World, the environ variable looks like: <br />
<table>
    % for key,value in request.environ.items():
      <tr> <th>request.environ[' ${key} ']</th> <td> ${value}</td></tr>
    % endfor
</table>
