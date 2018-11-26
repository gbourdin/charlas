#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from flask import url_for
from mnistapi.app import create_app


@pytest.fixture
def app():
    return create_app()


def test_api_ping_returns_200(client):
    assert client.get(url_for('ping.ping_ping')).status_code == 200


def test_api_ping_returns_pong(client):
    res = client.get(url_for('ping.ping_ping'))
    assert res.data == b'pong'
