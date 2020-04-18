# coding: utf-8
import os
import sys
import time
import pytest
import easytrader

sys.path.append(".")


class TestThsClientTrader:
    @pytest.fixture
    def user(self):
        _user = easytrader.use("ths")
        _user.prepare(
            user="31016658", password= "211122", comm_password="211122"
        )
        return _user

    def test_balance(self, user):
        time.sleep(3)
        result = user.balance

    def test_today_entrusts(self, user):
        result = user.today_entrusts

    def test_today_trades(self, user):
        result = user.today_trades

    def test_cancel_entrusts(self, user):
        result = user.cancel_entrusts

    def test_cancel_entrust(self, user):
        result = user.cancel_entrust("123456789")

    def test_invalid_buy(self, user):
        import easytrader

        with pytest.raises(easytrader.exceptions.TradeError):
            result = user.buy("511990", 1, 1e10)

    def test_invalid_sell(self, user):
        import easytrader

        with pytest.raises(easytrader.exceptions.TradeError):
            result = user.sell("162411", 200, 1e10)

    def test_auto_ipo(self, user):
        user.auto_ipo()
