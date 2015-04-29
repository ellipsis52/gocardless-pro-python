# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

from ..resources.refund import Refund
from .base_service import BaseService

class RefundsService(BaseService):
    RESOURCE_CLASS = Refund
    RESOURCE_NAME = 'refunds'

    def create(self, params=None):
        path = '/refunds'
        response = self.perform_request('POST', path, params)
        return self._resource_for(response)

    def list(self, params=None):
        path = '/refunds'
        response = self.perform_request('GET', path, params)
        return self._resource_for(response)

    def get(self, identity, params=None):
        path = self._sub_url_params('/refunds/:identity', {
            'identity': identity,
        })
        response = self.perform_request('GET', path, params)
        return self._resource_for(response)

    def update(self, identity, params=None):
        path = self._sub_url_params('/refunds/:identity', {
            'identity': identity,
        })
        response = self.perform_request('PUT', path, params)
        return self._resource_for(response)

