# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

import json

import requests
import responses
from nose.tools import (
  assert_equal,
  assert_is_instance,
  assert_is_none,
  assert_is_not_none,
  assert_not_equal,
  assert_raises
)

from gocardless_pro.errors import MalformedResponseError
from gocardless_pro import resources
from gocardless_pro import list_response

from .. import helpers
  

@responses.activate
def test_billing_request_flows_create():
    fixture = helpers.load_fixture('billing_request_flows')['create']
    helpers.stub_response(fixture)
    response = helpers.client.billing_request_flows.create(*fixture['url_params'])
    body = fixture['body']['billing_request_flows']

    assert_is_instance(response, resources.BillingRequestFlow)
    assert_is_not_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal(response.authorisation_url, body.get('authorisation_url'))
    assert_equal(response.auto_fulfil, body.get('auto_fulfil'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.exit_uri, body.get('exit_uri'))
    assert_equal(response.expires_at, body.get('expires_at'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.language, body.get('language'))
    assert_equal(response.lock_bank_account, body.get('lock_bank_account'))
    assert_equal(response.lock_currency, body.get('lock_currency'))
    assert_equal(response.lock_customer_details, body.get('lock_customer_details'))
    assert_equal(response.redirect_uri, body.get('redirect_uri'))
    assert_equal(response.session_token, body.get('session_token'))
    assert_equal(response.show_redirect_buttons, body.get('show_redirect_buttons'))
    assert_equal(response.links.billing_request,
                 body.get('links')['billing_request'])
    assert_equal(response.prefilled_bank_account.account_type,
                 body.get('prefilled_bank_account')['account_type'])
    assert_equal(response.prefilled_customer.address_line1,
                 body.get('prefilled_customer')['address_line1'])
    assert_equal(response.prefilled_customer.address_line2,
                 body.get('prefilled_customer')['address_line2'])
    assert_equal(response.prefilled_customer.address_line3,
                 body.get('prefilled_customer')['address_line3'])
    assert_equal(response.prefilled_customer.city,
                 body.get('prefilled_customer')['city'])
    assert_equal(response.prefilled_customer.company_name,
                 body.get('prefilled_customer')['company_name'])
    assert_equal(response.prefilled_customer.country_code,
                 body.get('prefilled_customer')['country_code'])
    assert_equal(response.prefilled_customer.danish_identity_number,
                 body.get('prefilled_customer')['danish_identity_number'])
    assert_equal(response.prefilled_customer.email,
                 body.get('prefilled_customer')['email'])
    assert_equal(response.prefilled_customer.family_name,
                 body.get('prefilled_customer')['family_name'])
    assert_equal(response.prefilled_customer.given_name,
                 body.get('prefilled_customer')['given_name'])
    assert_equal(response.prefilled_customer.postal_code,
                 body.get('prefilled_customer')['postal_code'])
    assert_equal(response.prefilled_customer.region,
                 body.get('prefilled_customer')['region'])
    assert_equal(response.prefilled_customer.swedish_identity_number,
                 body.get('prefilled_customer')['swedish_identity_number'])

@responses.activate
def test_timeout_billing_request_flows_create_retries():
    fixture = helpers.load_fixture('billing_request_flows')['create']
    with helpers.stub_timeout_then_response(fixture) as rsps:
      response = helpers.client.billing_request_flows.create(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      assert_equal(rsps.calls[0].request.headers.get('Idempotency-Key'),
                   rsps.calls[1].request.headers.get('Idempotency-Key'))
    body = fixture['body']['billing_request_flows']

    assert_is_instance(response, resources.BillingRequestFlow)

def test_502_billing_request_flows_create_retries():
    fixture = helpers.load_fixture('billing_request_flows')['create']
    with helpers.stub_502_then_response(fixture) as rsps:
      response = helpers.client.billing_request_flows.create(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      assert_equal(rsps.calls[0].request.headers.get('Idempotency-Key'),
                   rsps.calls[1].request.headers.get('Idempotency-Key'))
    body = fixture['body']['billing_request_flows']

    assert_is_instance(response, resources.BillingRequestFlow)
  

@responses.activate
def test_billing_request_flows_initialise():
    fixture = helpers.load_fixture('billing_request_flows')['initialise']
    helpers.stub_response(fixture)
    response = helpers.client.billing_request_flows.initialise(*fixture['url_params'])
    body = fixture['body']['billing_request_flows']

    assert_is_instance(response, resources.BillingRequestFlow)
    assert_is_not_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal(response.authorisation_url, body.get('authorisation_url'))
    assert_equal(response.auto_fulfil, body.get('auto_fulfil'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.exit_uri, body.get('exit_uri'))
    assert_equal(response.expires_at, body.get('expires_at'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.language, body.get('language'))
    assert_equal(response.lock_bank_account, body.get('lock_bank_account'))
    assert_equal(response.lock_currency, body.get('lock_currency'))
    assert_equal(response.lock_customer_details, body.get('lock_customer_details'))
    assert_equal(response.redirect_uri, body.get('redirect_uri'))
    assert_equal(response.session_token, body.get('session_token'))
    assert_equal(response.show_redirect_buttons, body.get('show_redirect_buttons'))
    assert_equal(response.links.billing_request,
                 body.get('links')['billing_request'])
    assert_equal(response.prefilled_bank_account.account_type,
                 body.get('prefilled_bank_account')['account_type'])
    assert_equal(response.prefilled_customer.address_line1,
                 body.get('prefilled_customer')['address_line1'])
    assert_equal(response.prefilled_customer.address_line2,
                 body.get('prefilled_customer')['address_line2'])
    assert_equal(response.prefilled_customer.address_line3,
                 body.get('prefilled_customer')['address_line3'])
    assert_equal(response.prefilled_customer.city,
                 body.get('prefilled_customer')['city'])
    assert_equal(response.prefilled_customer.company_name,
                 body.get('prefilled_customer')['company_name'])
    assert_equal(response.prefilled_customer.country_code,
                 body.get('prefilled_customer')['country_code'])
    assert_equal(response.prefilled_customer.danish_identity_number,
                 body.get('prefilled_customer')['danish_identity_number'])
    assert_equal(response.prefilled_customer.email,
                 body.get('prefilled_customer')['email'])
    assert_equal(response.prefilled_customer.family_name,
                 body.get('prefilled_customer')['family_name'])
    assert_equal(response.prefilled_customer.given_name,
                 body.get('prefilled_customer')['given_name'])
    assert_equal(response.prefilled_customer.postal_code,
                 body.get('prefilled_customer')['postal_code'])
    assert_equal(response.prefilled_customer.region,
                 body.get('prefilled_customer')['region'])
    assert_equal(response.prefilled_customer.swedish_identity_number,
                 body.get('prefilled_customer')['swedish_identity_number'])

def test_timeout_billing_request_flows_initialise_doesnt_retry():
    fixture = helpers.load_fixture('billing_request_flows')['initialise']
    with helpers.stub_timeout(fixture) as rsps:
      with assert_raises(requests.ConnectTimeout):
        response = helpers.client.billing_request_flows.initialise(*fixture['url_params'])
      assert_equal(1, len(rsps.calls))

def test_502_billing_request_flows_initialise_doesnt_retry():
    fixture = helpers.load_fixture('billing_request_flows')['initialise']
    with helpers.stub_502(fixture) as rsps:
      with assert_raises(MalformedResponseError):
        response = helpers.client.billing_request_flows.initialise(*fixture['url_params'])
      assert_equal(1, len(rsps.calls))
  
