#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive OKEX API
# Copyright (c) 2008-2018 Hive Solutions Lda.
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

__copyright__ = "Copyright (c) 2008-2018 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

import appier

from . import base

class OKEXApp(appier.WebApp):

    def __init__(self, *args, **kwargs):
        appier.WebApp.__init__(
            self,
            name = "okex",
            *args, **kwargs
        )

    @appier.route("/", "GET")
    def index(self):
        return self.ticker()

    @appier.route("/ticker", "GET")
    def ticker(self):
        symbol = self.field("symbol", "eth_btc")
        api = self.get_api()
        ticker = api.symbol_ticker(symbol)
        return ticker

    def get_api(self):
        api = base.get_api()
        return api

if __name__ == "__main__":
    app = OKEXApp()
    app.serve()
else:
    __path__ = []
