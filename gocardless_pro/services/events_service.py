# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

from ..resources.event import Event
from .base_service import BaseService

class EventsService(BaseService):
    RESOURCE_CLASS = Event
    RESOURCE_NAME = 'events'

    def list(self, params=None):
        path = '/events'
        response = self.perform_request('GET', path, params)
        return self._resource_for(response)

    def get(self, identity, params=None):
        path = self._sub_url_params('/events/:identity', {
            'identity': identity,
        })
        response = self.perform_request('GET', path, params)
        return self._resource_for(response)

