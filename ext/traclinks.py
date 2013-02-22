'''
Sphinx/docutils extension to create links to a Trac site using
a RestructuredText interpreted text role that looks like this:

    :trac:`trac_link_text`

for example:

    :trac:`#2015`

creates a link to ticket number 2015.

adapted from recipe here:
http://stackoverflow.com/questions/2096401/sphinx-generate-automatic-references-to-trac-tickets-and-changesets  # noqa
'''

import urllib
from docutils import nodes, utils


def make_trac_link(name, rawtext, text, lineno, inliner,
                   options={}, content=[]):
    env = inliner.document.settings.env
    trac_url = env.config.traclinks_base_url
    ref = trac_url + '/intertrac/' + urllib.quote(text, safe='')
    node = nodes.reference(rawtext, utils.unescape(text),
                           refuri=ref, **options)
    return [node], []


# setup function to register the extension
def setup(app):
    app.add_config_value('traclinks_base_url',
                         'http://trac.edgewall.com/trac',
                         'env')
    app.add_role('trac', make_trac_link)
