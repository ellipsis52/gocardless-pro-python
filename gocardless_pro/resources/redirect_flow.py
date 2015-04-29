# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

class RedirectFlow(object):

    def __init__(self, attributes, response):
        self.attributes = attributes
        self.response = response

    @property
    def created_at(self):
        return self.attributes.get('created_at')

    @property
    def description(self):
        return self.attributes.get('description')

    @property
    def id(self):
        return self.attributes.get('id')

    @property
    def links(self):
        return self.attributes.get('links')

    @property
    def redirect_url(self):
        return self.attributes.get('redirect_url')

    @property
    def scheme(self):
        return self.attributes.get('scheme')

    @property
    def session_token(self):
        return self.attributes.get('session_token')

    @property
    def success_redirect_url(self):
        return self.attributes.get('success_redirect_url')


# TODO: handle links properly, and double check how response is exposed

