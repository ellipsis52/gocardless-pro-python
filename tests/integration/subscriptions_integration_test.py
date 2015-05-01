# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

import requests
import responses
from nose.tools import assert_equal, assert_is_instance

from gocardless_pro import resources
from gocardless_pro import list_response

from .. import helpers

@responses.activate
def test_subscriptions_create():
    fixture = helpers.load_fixture('subscriptions')['create']
    helpers.stub_response(fixture)
    response = helpers.client.subscriptions.create(*fixture['url_params'])
    body = fixture['body']['subscriptions']

    assert_is_instance(response, resources.Subscription)

    assert_equal(response.amount, body.get('amount'))
    assert_equal(response.count, body.get('count'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.currency, body.get('currency'))
    assert_equal(response.day_of_month, body.get('day_of_month'))
    assert_equal(response.end_at, body.get('end_at'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.interval, body.get('interval'))
    assert_equal(response.interval_unit, body.get('interval_unit'))
    assert_equal(response.links, body.get('links'))
    assert_equal(response.metadata, body.get('metadata'))
    assert_equal(response.month, body.get('month'))
    assert_equal(response.name, body.get('name'))
    assert_equal(response.start_at, body.get('start_at'))
    assert_equal(response.status, body.get('status'))
    assert_equal(response.upcoming_payments, body.get('upcoming_payments'))

@responses.activate
def test_subscriptions_list():
    fixture = helpers.load_fixture('subscriptions')['list']
    helpers.stub_response(fixture)
    response = helpers.client.subscriptions.list(*fixture['url_params'])
    body = fixture['body']['subscriptions']

    assert_is_instance(response, list_response.ListResponse)
    assert_is_instance(next(iter(response)), resources.Subscription)

    assert_equal(response.before, fixture['body']['meta']['cursors']['before'])
    assert_equal(response.after, fixture['body']['meta']['cursors']['after'])

    assert_equal([r.amount for r in response],
                  [b.get('amount') for b in body])
    assert_equal([r.count for r in response],
                  [b.get('count') for b in body])
    assert_equal([r.created_at for r in response],
                  [b.get('created_at') for b in body])
    assert_equal([r.currency for r in response],
                  [b.get('currency') for b in body])
    assert_equal([r.day_of_month for r in response],
                  [b.get('day_of_month') for b in body])
    assert_equal([r.end_at for r in response],
                  [b.get('end_at') for b in body])
    assert_equal([r.id for r in response],
                  [b.get('id') for b in body])
    assert_equal([r.interval for r in response],
                  [b.get('interval') for b in body])
    assert_equal([r.interval_unit for r in response],
                  [b.get('interval_unit') for b in body])
    assert_equal([r.links for r in response],
                  [b.get('links') for b in body])
    assert_equal([r.metadata for r in response],
                  [b.get('metadata') for b in body])
    assert_equal([r.month for r in response],
                  [b.get('month') for b in body])
    assert_equal([r.name for r in response],
                  [b.get('name') for b in body])
    assert_equal([r.start_at for r in response],
                  [b.get('start_at') for b in body])
    assert_equal([r.status for r in response],
                  [b.get('status') for b in body])
    assert_equal([r.upcoming_payments for r in response],
                  [b.get('upcoming_payments') for b in body])

@responses.activate
def test_subscriptions_get():
    fixture = helpers.load_fixture('subscriptions')['get']
    helpers.stub_response(fixture)
    response = helpers.client.subscriptions.get(*fixture['url_params'])
    body = fixture['body']['subscriptions']

    assert_is_instance(response, resources.Subscription)

    assert_equal(response.amount, body.get('amount'))
    assert_equal(response.count, body.get('count'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.currency, body.get('currency'))
    assert_equal(response.day_of_month, body.get('day_of_month'))
    assert_equal(response.end_at, body.get('end_at'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.interval, body.get('interval'))
    assert_equal(response.interval_unit, body.get('interval_unit'))
    assert_equal(response.links, body.get('links'))
    assert_equal(response.metadata, body.get('metadata'))
    assert_equal(response.month, body.get('month'))
    assert_equal(response.name, body.get('name'))
    assert_equal(response.start_at, body.get('start_at'))
    assert_equal(response.status, body.get('status'))
    assert_equal(response.upcoming_payments, body.get('upcoming_payments'))

@responses.activate
def test_subscriptions_update():
    fixture = helpers.load_fixture('subscriptions')['update']
    helpers.stub_response(fixture)
    response = helpers.client.subscriptions.update(*fixture['url_params'])
    body = fixture['body']['subscriptions']

    assert_is_instance(response, resources.Subscription)

    assert_equal(response.amount, body.get('amount'))
    assert_equal(response.count, body.get('count'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.currency, body.get('currency'))
    assert_equal(response.day_of_month, body.get('day_of_month'))
    assert_equal(response.end_at, body.get('end_at'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.interval, body.get('interval'))
    assert_equal(response.interval_unit, body.get('interval_unit'))
    assert_equal(response.links, body.get('links'))
    assert_equal(response.metadata, body.get('metadata'))
    assert_equal(response.month, body.get('month'))
    assert_equal(response.name, body.get('name'))
    assert_equal(response.start_at, body.get('start_at'))
    assert_equal(response.status, body.get('status'))
    assert_equal(response.upcoming_payments, body.get('upcoming_payments'))

@responses.activate
def test_subscriptions_cancel():
    fixture = helpers.load_fixture('subscriptions')['cancel']
    helpers.stub_response(fixture)
    response = helpers.client.subscriptions.cancel(*fixture['url_params'])
    body = fixture['body']['subscriptions']

    assert_is_instance(response, resources.Subscription)

    assert_equal(response.amount, body.get('amount'))
    assert_equal(response.count, body.get('count'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.currency, body.get('currency'))
    assert_equal(response.day_of_month, body.get('day_of_month'))
    assert_equal(response.end_at, body.get('end_at'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.interval, body.get('interval'))
    assert_equal(response.interval_unit, body.get('interval_unit'))
    assert_equal(response.links, body.get('links'))
    assert_equal(response.metadata, body.get('metadata'))
    assert_equal(response.month, body.get('month'))
    assert_equal(response.name, body.get('name'))
    assert_equal(response.start_at, body.get('start_at'))
    assert_equal(response.status, body.get('status'))
    assert_equal(response.upcoming_payments, body.get('upcoming_payments'))
