#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
from uuid import uuid4

headers = {'content-type': 'application/json'}


def set_params(method, params):
    """Set params to query limesurvey"""
    data = {'method': method, 'params': params, 'id': str(uuid4())}
    return json.dumps(data)


def get_session_key(limedict):
    """This function receive a dictionary with connection parameters.
        { "url": "full path for remote control",
          "username: "account name to be used"
          "password" "password for account"}"""
    url = limedict['url']
    user = limedict['username']
    password = limedict['password']
    params = {'username': user, 'password': password}
    data = set_params('get_session_key', params)
    req = requests.post(url, data=data, headers=headers)
    return {'token': req.json()['result'], 'user': user, 'url': url}


def list_surveys(session):
    """retrieve a list of surveys from current user"""
    params = {'sUser': session['user'], 'sSessionKey': session['token']}
    data = set_params('list_surveys', params)
    req = requests.post(session['url'], data=data, headers=headers)
    return req.text
