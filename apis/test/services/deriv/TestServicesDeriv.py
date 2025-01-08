from unittest import TestCase, mock

import unittest

import apis.services.deriv.ServicesDeriv as ServicesDeriv

import apis.services.methodologytrends.ServicesMethodologyTrends as ServicesMethodologyTrends

class TestServicesDeriv(unittest.IsolatedAsyncioTestCase):
    
    Services = None

    SerivcesMethodologyTrends = None

    def setUp(self):

        self.Services = ServicesDeriv.ServicesDeriv()

        self.ServicesMethodologyTrends = ServicesMethodologyTrends.ServicesMethodologyTrends()

        self.Services.init_services_methodology_trends(self.ServicesMethodologyTrends)

    def add_entry_persistence_loss(self):

        data = [
            {'status': False, 'message': 'La posición fue perdedora', 'loss': -2, 'contract_details': {'account_id': 243447828, 'audit_details': {'contract_end': [{'epoch': 1736297016, 'tick': 1521.38, 'tick_display_value': '1521.38'}, {'epoch': 1736297018, 'tick': 1522.27, 'tick_display_value': '1522.27'}, {'epoch': 1736297020, 'flag': 'highlight_tick', 'name': 'End Time and Exit Spot', 'tick': 1522.49, 'tick_display_value': '1522.49'}, {'epoch': 1736297022, 'tick': 1522.78, 'tick_display_value': '1522.78'}, {'epoch': 1736297024, 'tick': 1522.89, 'tick_display_value': '1522.89'}], 'contract_start': [{'epoch': 1736296956, 'tick': 1523.17, 'tick_display_value': '1523.17'}, {'epoch': 1736296958, 'tick': 1523.12, 'tick_display_value': '1523.12'}]}, 'barrier': '1522.75', 'barrier_count': 1, 'bid_price': 0, 'buy_price': 2, 'contract_id': 268738067488, 'contract_type': 'CALL', 'currency': 'USD', 'current_spot': 1522.89, 'current_spot_display_value': '1522.89', 'current_spot_time': 1736297024, 'date_expiry': 1736297020, 'date_settlement': 1736297020, 'date_start': 1736296960, 'display_name': 'Volatility 100 Index', 'entry_spot': 1522.75, 'entry_spot_display_value': '1522.75', 'entry_tick': 1522.75, 'entry_tick_display_value': '1522.75', 'entry_tick_time': 1736296962, 'exit_tick': 1522.49, 'exit_tick_display_value': '1522.49', 'exit_tick_time': 1736297020, 'expiry_time': 1736297020, 'is_expired': 1, 'is_forward_starting': 0, 'is_intraday': 1, 'is_path_dependent': 0, 'is_settleable': 1, 'is_sold': 1, 'is_valid_to_cancel': 0, 'is_valid_to_sell': 0, 'longcode': 'Win payout if Volatility 100 Index is strictly higher than entry spot at 1 minute after contract start time.', 'payout': 3.91, 'profit': -2, 'profit_percentage': -100, 'purchase_time': 1736296960, 'sell_price': 0, 'sell_spot': 1522.49, 'sell_spot_display_value': '1522.49', 'sell_spot_time': 1736297020, 'sell_time': 1736297022, 'shortcode': 'CALL_R_100_3.91_1736296960_1736297020_S0P_0', 'status': 'lost', 'transaction_ids': {'buy': 535745816488, 'sell': 535745912448}, 'underlying': 'R_100', 'validation_error': 'This contract has been sold.', 'validation_error_code': 'General'}}
        ]

        data_candles = [
            {'status': True, 'message': '31 velas obtenidas correctamente', 'candles': [{'close': 1512.1, 'epoch': 1736270100, 'high': 1512.85, 'low': 1500.98, 'open': 1511.89}, {'close': 1514.96, 'epoch': 1736271000, 'high': 1518.73, 'low': 1508.77, 'open': 1511.95}, {'close': 1524.79, 'epoch': 1736271900, 'high': 1527.19, 'low': 1514.43, 'open': 1514.43}, {'close': 1533.77, 'epoch': 1736272800, 'high': 1539.04, 'low': 1524.67, 'open': 1524.68}, {'close': 1536.12, 'epoch': 1736273700, 'high': 1539.12, 'low': 1532.49, 'open': 1534.43}, {'close': 1540.82, 'epoch': 1736274600, 'high': 1543.96, 'low': 1532.97, 'open': 1536.05}, {'close': 1538.13, 'epoch': 1736275500, 'high': 1542.03, 'low': 1530.14, 'open': 1541.27}, {'close': 1526.74, 'epoch': 1736276400, 'high': 1539.22, 'low': 1522.03, 'open': 1537.51}, {'close': 1527.5, 'epoch': 1736277300, 'high': 1531.75, 'low': 1525.7, 'open': 1527.14}, {'close': 1531.93, 'epoch': 1736278200, 'high': 1532.45, 'low': 1524.65, 'open': 1527.53}, {'close': 1537.93, 'epoch': 1736279100, 'high': 1541.45, 'low': 1523.4, 'open': 1531.61}, {'close': 1532.09, 'epoch': 1736280000, 'high': 1538.84, 'low': 1527.99, 'open': 1538.34}, {'close': 1531.93, 'epoch': 1736280900, 'high': 1538.58, 'low': 1528.09, 'open': 1532.15}, {'close': 1538.64, 'epoch': 1736281800, 'high': 1539.45, 'low': 1525.02, 'open': 1531.47}, {'close': 1542.98, 'epoch': 1736282700, 'high': 1547.89, 'low': 1536.87, 'open': 1538.68}, {'close': 1548.68, 'epoch': 1736283600, 'high': 1553.95, 'low': 1541.2, 'open': 1543.43}, {'close': 1554.19, 'epoch': 1736284500, 'high': 1556.2, 'low': 1543, 'open': 1548.04}, {'close': 1557.99, 'epoch': 1736285400, 'high': 1560.75, 'low': 1550.67, 'open': 1554.24}, {'close': 1542.98, 'epoch': 1736286300, 'high': 1558.74, 'low': 1540.41, 'open': 1558.12}, {'close': 1530.95, 'epoch': 1736287200, 'high': 1545.22, 'low': 1528.12, 'open': 1542.99}, {'close': 1515.44, 'epoch': 1736288100, 'high': 1534.53, 'low': 1513.8, 'open': 1530.6}, {'close': 1512.87, 'epoch': 1736289000, 'high': 1520.79, 'low': 1512.16, 'open': 1515.43}, {'close': 1506.75, 'epoch': 1736289900, 'high': 1520.94, 'low': 1506.75, 'open': 1512.6}, {'close': 1507.65, 'epoch': 1736290800, 'high': 1512.17, 'low': 1504.38, 'open': 1507.01}, {'close': 1514.49, 'epoch': 1736291700, 'high': 1517.09, 'low': 1506.58, 'open': 1507.23}, {'close': 1509.24, 'epoch': 1736292600, 'high': 1516.64, 'low': 1502.75, 'open': 1513.96}, {'close': 1518.28, 'epoch': 1736293500, 'high': 1519.71, 'low': 1506.81, 'open': 1509.15}, {'close': 1522.28, 'epoch': 1736294400, 'high': 1526.8, 'low': 1513.64, 'open': 1518.63}, {'close': 1523.88, 'epoch': 1736295300, 'high': 1535.01, 'low': 1521.66, 'open': 1522.36}, {'close': 1519.06, 'epoch': 1736296200, 'high': 1529.52, 'low': 1518.53, 'open': 1523.85}, {'close': 1524.74, 'epoch': 1736297100, 'high': 1526.42, 'low': 1517.36, 'open': 1518.6}]}
        ]

        result = self.Services.add_entry_persistence(data,data_candles)

        print("services:", result)

        return result