#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive OKEX API
# Copyright (c) 2008-2025 Hive Solutions Lda.
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

__copyright__ = "Copyright (c) 2008-2025 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

import appier


class AccountAPI(object):

    def self_account(self):
        url = self.base_url + "userinfo.do"
        contents = self.post(url, sign=True)
        return contents

    def withdraw_account(
        self, symbol, address, amount, trade_pwd, fee=None, target="address"
    ):
        appier.verify(
            symbol in ("btc_usd", "eth_usd", "ltc_usd"),
            message="Symbol '%s' not supported for withdraw" % symbol,
        )

        if symbol.startswith("btc"):
            fee = fee or "0.002"
        if symbol.startswith("ltc"):
            fee = fee or "0.001"
        if symbol.startswith("eth"):
            fee = fee or "0.01"

        url = self.base_url + "withdraw.do"
        contents = self.post(
            url,
            symbol=symbol,
            chargefee=fee,
            trade_pwd=trade_pwd,
            withdraw_address=address,
            withdraw_amount=amount,
            sign=True,
        )
        return contents
