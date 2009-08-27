import re
import logging
import sets

from docutils.core import publish_parts

from pylons import url
from quickwiki.lib.helpers import link_to

import sqlalchemy as sa
from sqlalchemy import orm

from quickwiki.model import meta


log = logging.getLogger(__name__)



SAFE_DOCUTILS = dict(file_insertion_enabled=False, raw_enabled=False)
wikiwords = re.compile(r"\b([A-Z]+\w+[A-Z]+\w+)", re.UNICODE)

pages_table = sa.Table('pages', meta.metadata,
	sa.Column('title', sa.types.Unicode(40), primary_key=True),
	sa.Column('content',sa.types.Unicode(),default='')
	)

class Page(object):
	def __init__(self, title, content=None):
		self.title   = title
		self.content = content

	def __unicode__(self):
		return self.title
	
	__str__ = __unicode__
	
	def get_wiki_content(self):
		"""Convert reStructuredText content to HTML for display, and create 
		   links for wikiwords"""
		content = publish_parts(self.content, writer_name='html',
					settings_overrides=SAFE_DOCUTILS)['html_body']
		titles  = sets.Set(wikiwords.findall(content))
		for title in titles:
			title_url = url(controller='pages', action='show', title=title)
			content   = content.replace(title, link_to(title, title_url))
		return content		

orm.mapper(Page,pages_table)

