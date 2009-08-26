"""Setup the QuickWiki application"""
import logging

from quickwiki import model
from quickwiki.config.environment import load_environment
from quickwiki.model import meta

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    """Place any commands to setup quickwiki here"""
    load_environment(conf.global_conf, conf.local_conf)

    # Create the tables if they don't already exist
    log.info("Creating tables...")
    meta.metadata.create_all(bind=meta.engine)
    log.info("Tables are up ")

    log.info("Adding front page data...")
    page = model.Page(title   = u'FrontPage', 
                      content = u'**Welcome** to the QuickWiki front page!')
    meta.Session.add(page)
    meta.Session.commit()
    log.info("Succesfully set up")
