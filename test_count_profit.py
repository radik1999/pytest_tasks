from pytest import mark

from tasks import count_profit


class TestCountProfit:
    @mark.parametrize('data, profit', [(
            {
                "cost_price": 225.89,
                "sell_price": 550.00,
                "inventory": 100
            }, 32411),
        ({
             "cost_price": 32.67,
             "sell_price": 45.00,
             "inventory": 1200
         }, 14796),
        ({
             "cost_price": 2.77,
             "sell_price": 7.95,
             "inventory": 8500
         }, 44030)
    ])
    def test_count_profit(self, data, profit):
        assert count_profit(data) == profit

    def test_count_profit_empty(self):
        assert count_profit({}) is None
