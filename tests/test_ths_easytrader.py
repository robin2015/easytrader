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
        # _user.prepare(
        #     user="31016658", password= "211122", comm_password="211122"
        # )
        _user.enable_type_keys_for_editor()
        _user.connect()
        return _user

    def test_balance(self, user):
        # 查询[F4]", "资金余额
        # time.sleep(3)
        result = user.balance
        print(result)

    def test_position(self, user):
        # 查询[F4]", "资金股票
        # time.sleep(3)
        result = user.position
        print(result)

    def test_today_entrusts(self, user):
        #当日委托
        result = user.today_entrusts
        print(result)

    def test_today_trades(self, user):
        #当日成交
        result = user.today_trades
        print(result)

    def test_cancel_entrusts(self, user):
        #撤单[F3] 列表
        result = user.cancel_entrusts
        print(result)

    def test_cancel_entrust(self, user):
        # 撤单 根据合同编号 字符串
        result = user.cancel_entrust('4245')
        print(result)

    def test_buy(self, user):
        #买入[F1]
        result = user.buy("600000", 10.00, 100)
        print(result)

    def test_invalid_buy(self, user):
        with pytest.raises(easytrader.exceptions.TradeError):
            result = user.buy("511990", 1, 1e10)
            print(result)

    def test_sell(self, user):
        result = user.sell("600000", 10.00, 100)
        print(result)

    def test_invalid_sell(self, user):
        with pytest.raises(easytrader.exceptions.TradeError):
            result = user.sell("162411", 200, 1e10)
            print(result)

    def test_auto_ipo(self, user):
        user.auto_ipo()
