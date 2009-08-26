try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='QuickWiki',
    version='0.1.6',
    description='QuickWiki - Pylons 0.9.7 Tutorial application',
    author='',
    author_email='',
    url='http://docs.pylonshq.com/tutorials/quickwik_tutorial.html',
    install_requires=[
        "Pylons>=0.9.7",
        "SQLAlchemy>=0.5",
        "docutils==0.4",
    ],
    setup_requires=["PasteScript>=1.6.3"],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    test_suite='nose.collector',
    package_data={'quickwiki': ['i18n/*/LC_MESSAGES/*.mo']},
    #message_extractors={'quickwiki': [
    #        ('**.py', 'python', None),
    #        ('templates/**.mako', 'mako', {'input_encoding': 'utf-8'}),
    #        ('public/**', 'ignore', None)]},
    zip_safe=False,
    paster_plugins=['PasteScript', 'Pylons'],
    entry_points="""
    [paste.app_factory]
    main = quickwiki.config.middleware:make_app

    [paste.app_install]
    main = pylons.util:PylonsInstaller
    """,
)
