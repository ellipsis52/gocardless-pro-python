# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

from . import base_service
from .. import resources
from ..paginator import Paginator

class BankDetailsLookupsService(base_service.BaseService):
    """Service class that provides access to the bank_details_lookups
    endpoints of the GoCardless Pro API.
    """

    RESOURCE_CLASS = resources.BankDetailsLookup
    RESOURCE_NAME = 'bank_details_lookups'

    def create(self, params=None):
        """Perform a bank details lookup.

        Performs a bank details lookup.
        
        Bank account details
        may be supplied using [local details](#appendix-local-bank-details) or
        an IBAN.

        Args:
          params (dict, optional): Request body.

        Returns:
          BankDetailsLookup
        """
        path = '/bank_details_lookups'
        response = self._perform_request('POST', path, params)
        return self._resource_for(response)

