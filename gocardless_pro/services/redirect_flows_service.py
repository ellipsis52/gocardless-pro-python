# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

from ..resources.redirect_flow import RedirectFlow
from .base_service import BaseService

class RedirectFlowsService(BaseService):
    RESOURCE_CLASS = RedirectFlow
    RESOURCE_NAME = 'redirect_flows'

    def create(self, params=None):
        path = '/redirect_flows'
        response = self.perform_request('POST', path, params)
        return self._resource_for(response)

    def get(self, identity, params=None):
        path = self._sub_url_params('/redirect_flows/:identity', {
            'identity': identity,
        })
        response = self.perform_request('GET', path, params)
        return self._resource_for(response)

    def complete(self, identity, params=None):
        path = self._sub_url_params('/redirect_flows/:identity/actions/complete', {
            'identity': identity,
        })
        response = self.perform_request('POST', path, params)
        return self._resource_for(response)

