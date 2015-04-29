# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

class Creditor(object):

    def __init__(self, attributes, response):
        self.attributes = attributes
        self.response = response

    @property
    def address_line1(self):
        return self.attributes.get('address_line1')

    @property
    def address_line2(self):
        return self.attributes.get('address_line2')

    @property
    def address_line3(self):
        return self.attributes.get('address_line3')

    @property
    def city(self):
        return self.attributes.get('city')

    @property
    def country_code(self):
        return self.attributes.get('country_code')

    @property
    def created_at(self):
        return self.attributes.get('created_at')

    @property
    def id(self):
        return self.attributes.get('id')

    @property
    def links(self):
        return self.attributes.get('links')

    @property
    def name(self):
        return self.attributes.get('name')

    @property
    def postal_code(self):
        return self.attributes.get('postal_code')

    @property
    def region(self):
        return self.attributes.get('region')


# TODO: handle links properly, and double check how response is exposed

