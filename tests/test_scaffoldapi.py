#!/usr/bin/env python
"""Tests for `scaffoldapi` package."""

import pytest
import requests
from scaffoldapi import scaffoldapi


def test_returns_sum_as_float():
    """ Tests returns_sumn_as_float returns a float"""
    assert scaffoldapi.returns_sum_as_float(1.5, 6) == float(7.5)


def test_who_am_i_online():
    """ Tests who_am_i_online(0 returns a requests.Response type"""
    assert type(scaffoldapi.who_am_i_online()) == requests.Response
