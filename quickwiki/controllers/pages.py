from cgi import escape

import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to
from pylons.decorators.secure import authenticate_form

from quickwiki.lib.base     import BaseController, render
from quickwiki.lib.helpers  import flash
from quickwiki.model        import Page, wikiwords
from quickwiki.model.meta   import Session
log = logging.getLogger(__name__)

class PagesController(BaseController):

    def __before__(self):
        if request.environ.get('repoze.who.identity') == None:
                    abort(401)
        self.page_q = Session.query(Page)

    def show(self, title):
        page = self.page_q.filter_by(title=title).first()
        if page:
           c.content = page.get_wiki_content()
           return render('/pages/show.mako')
        elif wikiwords.match(title):
            return render('/pages/new.mako')
        abort(404)
    def edit(self, title):
        page = self.page_q.filter_by(title=title).first()
        if page:
           c.content = page.content
        return render('/pages/edit.mako')
    @authenticate_form
    def save(self, title):
        page = self.page_q.filter_by(title=title).first()
        if not page:
          page = Page(title)
        page.content = escape(request.POST.getone('content'))
        Session.add(page)
        Session.commit()
        flash('Successfully saved %s!' % title)
        redirect_to('show_page', title=title)
    def delete(self):
        titles = request.POST.getall('title')
        pages  = self.page_q.filter(Page.title.in_(titles))
        for page in pages:
          Session.delete(page)
        Session.commit()
        for title in titles:
          flash('Deleted %s.' %title)
        redirect_to('pages')
    def index(self):
        c.titles = [page.title for page in self.page_q.all()]
        return render('/pages/index.mako')
