# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

from . import base_service
from .. import resources
from ..paginator import Paginator

class MandatesService(base_service.BaseService):
    """Service class that provides access to the mandates
    endpoints of the GoCardless Pro API.
    """

    RESOURCE_CLASS = resources.Mandate
    RESOURCE_NAME = 'mandates'

    def create(self, params=None):
        """Create a mandate.

        Creates a new mandate object.

        Args:
          params (dict, optional): Request body.

        Returns:
          Mandate
        """
        path = '/mandates'
        response = self._perform_request('POST', path, params)
        return self._resource_for(response)

    def list(self, params=None):
        """List mandates.

        Returns a [cursor-paginated](#overview-cursor-pagination) list of your
        mandates. Except where stated, these filters can only be used one at a
        time.

        Args:
          params (dict, optional): Query string parameters.

        Returns:
          ListResponse of Mandate instances
        """
        path = '/mandates'
        response = self._perform_request('GET', path, params)
        return self._resource_for(response)

    def all(self, params=None):
        if params is None:
            params = {}
        return Paginator(self, params)

    def get(self, identity, params=None):
        """Get a single mandate.

        Retrieves the details of an existing mandate.

        Args:
          identity (string): Unique identifier, beginning with "MD".
          params (dict, optional): Query string parameters.

        Returns:
          Mandate
        """
        path = self._sub_url_params('/mandates/:identity', {
            'identity': identity,
        })
        response = self._perform_request('GET', path, params)
        return self._resource_for(response)

    def update(self, identity, params=None):
        """Update a mandate.

        Updates a mandate object. This accepts only the metadata parameter.

        Args:
          identity (string): Unique identifier, beginning with "MD".
          params (dict, optional): Request body.

        Returns:
          Mandate
        """
        path = self._sub_url_params('/mandates/:identity', {
            'identity': identity,
        })
        response = self._perform_request('PUT', path, params)
        return self._resource_for(response)

    def cancel(self, identity, params=None):
        """Cancel a mandate.

        Immediately cancels a mandate and all associated cancellable payments.
        Any metadata supplied to this endpoint will be stored on the mandate
        cancellation event it causes.
        
        This will fail with a
        `cancellation_failed` error if the mandate is already cancelled.

        Args:
          identity (string): Unique identifier, beginning with "MD".
          params (dict, optional): Request body.

        Returns:
          Mandate
        """
        path = self._sub_url_params('/mandates/:identity/actions/cancel', {
            'identity': identity,
        })
        response = self._perform_request('POST', path, params)
        return self._resource_for(response)

    def reinstate(self, identity, params=None):
        """Reinstate a mandate.

        <a name="mandate_not_inactive"></a>Reinstates a cancelled or expired
        mandate to the banks. You will receive a `resubmission_requested`
        webhook, but after that reinstating the mandate follows the same
        process as its initial creation, so you will receive a `submitted`
        webhook, followed by a `reinstated` or `failed` webhook up to two
        working days later. Any metadata supplied to this endpoint will be
        stored on the `resubmission_requested` event it causes.
        
      
         This will fail with a `mandate_not_inactive` error if the mandate is
        already being submitted, or is active.
        
        Mandates can be
        resubmitted up to 3 times.

        Args:
          identity (string): Unique identifier, beginning with "MD".
          params (dict, optional): Request body.

        Returns:
          Mandate
        """
        path = self._sub_url_params('/mandates/:identity/actions/reinstate', {
            'identity': identity,
        })
        response = self._perform_request('POST', path, params)
        return self._resource_for(response)

