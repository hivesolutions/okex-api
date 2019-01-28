#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive OKEX API
# Copyright (c) 2008-2019 Hive Solutions Lda.
#
# This file is part of Hive OKEX API.
#
# Hive OKEX API is free software: you can redistribute it and/or modify
# it under the terms of the Apache License as published by the Apache
# Foundation, either version 2.0 of the License, or (at your option) any
# later version.
#
# Hive OKEX API is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# Apache License for more details.
#
# You should have received a copy of the Apache License along with
# Hive OKEX API. If not, see <http://www.apache.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2019 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

import hashlib

import appier

from . import ticker
from . import account

BASE_URL = "https://www.okex.com/api/v1/"
""" The default base URL to be used when no other
base URL value is provided to the constructor """

class API(
    appier.API,
    ticker.TickerAPI,
    account.AccountAPI
):

    def __init__(self, *args, **kwargs):
        appier.API.__init__(self, *args, **kwargs)
        self.base_url = appier.conf("OKEX_BASE_URL", BASE_URL)
        self.api_key = appier.conf("OKEX_API_KEY", None)
        self.secret = appier.conf("OKEX_SECRET", None)
        self.base_url = kwargs.get("base_url", self.base_url)
        self.api_key = kwargs.get("api_key", self.api_key)
        self.secret = kwargs.get("secret", self.secret)

    def build(
        self,
        method,
        url,
        data = None,
        data_j = None,
        data_m = None,
        headers = None,
        params = None,
        mime = None,
        kwargs = None
    ):
        auth = kwargs.pop("auth", True)
        sign = kwargs.pop("sign", False)
        if auth and self.api_key: params["api_key"] = self.api_key
        if sign and self.secret:
            query_l = list(appier.legacy.items(params))
            query_l.sort()
            query_l.append(("secret_key", self.secret))
            values = appier.http._urlencode(query_l)
            values = appier.legacy.bytes(values, force = True)
            digest = hashlib.md5(values)
            params["sign"] = digest.hexdigest().upper()
