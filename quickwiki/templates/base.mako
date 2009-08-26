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
                                ${next.body()}\
                                      <p class="footer">
                                              Return to the ${h.link_to('FrontPage', url('FrontPage'))}
                                                      | ${h.link_to('Edit ' + c.title, url('edit_page', title=c.title))}
                                      </p>
                    </div>
                </body>
</html>

