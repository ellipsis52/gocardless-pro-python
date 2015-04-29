# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

class Payment(object):

    def __init__(self, attributes, response):
        self.attributes = attributes
        self.response = response

    @property
    def amount(self):
        return self.attributes.get('amount')

    @property
    def amount_refunded(self):
        return self.attributes.get('amount_refunded')

    @property
    def charge_date(self):
        return self.attributes.get('charge_date')

    @property
    def created_at(self):
        return self.attributes.get('created_at')

    @property
    def currency(self):
        return self.attributes.get('currency')

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
    def metadata(self):
        return self.attributes.get('metadata')

    @property
    def reference(self):
        return self.attributes.get('reference')

    @property
    def status(self):
        return self.attributes.get('status')


# TODO: handle links properly, and double check how response is exposed

