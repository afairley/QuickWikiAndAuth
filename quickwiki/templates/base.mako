<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"
  "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
  <html>
    <head>
        <title>QuickWiki</title>
            ${h.stylesheet_link('/quick.css')}
              </head>

                <body>
                    <div class="content">
                          <h1 class="main">${self.header()}</h1>

                          <% flashes = h.flash.pop_messages() %>
                          % if flashes:
                            % for flash in flashes:
                            <div id="flash">
                                <span class="message">${flash}</span>
                            </div>
                            % endfor
                          % endif
                                ${next.body()}\
                                      <p class="footer">
                                      ${self.footer(request.environ['pylons.routes_dict']['action'])}\
                                                                            </p>
                    </div>
                </body>
</html>

<%def name="footer(action)">\
        Return to the ${h.link_to('FrontPage', url('home'))}
        % if action == "index":
            <% return %>
        % endif
        % if action != 'edit':
          | ${h.link_to('Edit ' + c.title, url('edit_page', title=c.title))}
        % endif
          | ${h.link_to('Title List', url('pages'))}
</%def> 

