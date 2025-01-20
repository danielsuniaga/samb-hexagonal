import decimal

class EntityTestServicesDeriv:

    entrys = None

    candles = None

    indicators = None

    def __init__(self):

        self.init_entrys()

        self.init_candlers()

        self.init_indicators()

    def init_indicators(self):

        self.indicators = {
            'rsi': decimal.Decimal('43.28089347904403926139136608'),
            'sma_short': 1675.5009999999997,
            'sma_long': 1641.4026666666664,
            'last_candle': 1671.25
        }

        return True
    
    def get_indicators(self):

        return self.indicators  

    def init_candlers(self):

        self.candles =  {'status': True, 'message': '31 velas obtenidas correctamente', 'candles': [{'close': 1512.1, 'epoch': 1736270100, 'high': 1512.85, 'low': 1500.98, 'open': 1511.89}, {'close': 1514.96, 'epoch': 1736271000, 'high': 1518.73, 'low': 1508.77, 'open': 1511.95}, {'close': 1524.79, 'epoch': 1736271900, 'high': 1527.19, 'low': 1514.43, 'open': 1514.43}, {'close': 1533.77, 'epoch': 1736272800, 'high': 1539.04, 'low': 1524.67, 'open': 1524.68}, {'close': 1536.12, 'epoch': 1736273700, 'high': 1539.12, 'low': 1532.49, 'open': 1534.43}, {'close': 1540.82, 'epoch': 1736274600, 'high': 1543.96, 'low': 1532.97, 'open': 1536.05}, {'close': 1538.13, 'epoch': 1736275500, 'high': 1542.03, 'low': 1530.14, 'open': 1541.27}, {'close': 1526.74, 'epoch': 1736276400, 'high': 1539.22, 'low': 1522.03, 'open': 1537.51}, {'close': 1527.5, 'epoch': 1736277300, 'high': 1531.75, 'low': 1525.7, 'open': 1527.14}, {'close': 1531.93, 'epoch': 1736278200, 'high': 1532.45, 'low': 1524.65, 'open': 1527.53}, {'close': 1537.93, 'epoch': 1736279100, 'high': 1541.45, 'low': 1523.4, 'open': 1531.61}, {'close': 1532.09, 'epoch': 1736280000, 'high': 1538.84, 'low': 1527.99, 'open': 1538.34}, {'close': 1531.93, 'epoch': 1736280900, 'high': 1538.58, 'low': 1528.09, 'open': 1532.15}, {'close': 1538.64, 'epoch': 1736281800, 'high': 1539.45, 'low': 1525.02, 'open': 1531.47}, {'close': 1542.98, 'epoch': 1736282700, 'high': 1547.89, 'low': 1536.87, 'open': 1538.68}, {'close': 1548.68, 'epoch': 1736283600, 'high': 1553.95, 'low': 1541.2, 'open': 1543.43}, {'close': 1554.19, 'epoch': 1736284500, 'high': 1556.2, 'low': 1543, 'open': 1548.04}, {'close': 1557.99, 'epoch': 1736285400, 'high': 1560.75, 'low': 1550.67, 'open': 1554.24}, {'close': 1542.98, 'epoch': 1736286300, 'high': 1558.74, 'low': 1540.41, 'open': 1558.12}, {'close': 1530.95, 'epoch': 1736287200, 'high': 1545.22, 'low': 1528.12, 'open': 1542.99}, {'close': 1515.44, 'epoch': 1736288100, 'high': 1534.53, 'low': 1513.8, 'open': 1530.6}, {'close': 1512.87, 'epoch': 1736289000, 'high': 1520.79, 'low': 1512.16, 'open': 1515.43}, {'close': 1506.75, 'epoch': 1736289900, 'high': 1520.94, 'low': 1506.75, 'open': 1512.6}, {'close': 1507.65, 'epoch': 1736290800, 'high': 1512.17, 'low': 1504.38, 'open': 1507.01}, {'close': 1514.49, 'epoch': 1736291700, 'high': 1517.09, 'low': 1506.58, 'open': 1507.23}, {'close': 1509.24, 'epoch': 1736292600, 'high': 1516.64, 'low': 1502.75, 'open': 1513.96}, {'close': 1518.28, 'epoch': 1736293500, 'high': 1519.71, 'low': 1506.81, 'open': 1509.15}, {'close': 1522.28, 'epoch': 1736294400, 'high': 1526.8, 'low': 1513.64, 'open': 1518.63}, {'close': 1523.88, 'epoch': 1736295300, 'high': 1535.01, 'low': 1521.66, 'open': 1522.36}, {'close': 1519.06, 'epoch': 1736296200, 'high': 1529.52, 'low': 1518.53, 'open': 1523.85}, {'close': 1524.74, 'epoch': 1736297100, 'high': 1526.42, 'low': 1517.36, 'open': 1518.6}]}

        return True
    
    def get_candles(self):

        return self.candles
    

    def init_entrys(self):

        self.entrys = {
            'true':{
                'status': True,
                'message': 'La posición fue exitosa',
                'profit': 3.91,
                'contract_details': {
                    'account_id': 243447828,
                    'audit_details': {
                        'contract_end': [
                            {'epoch': 1736459802, 'tick': 1583.81, 'tick_display_value': '1583.81'},
                            {'epoch': 1736459804, 'tick': 1583.62, 'tick_display_value': '1583.62'},
                            {'epoch': 1736459806, 'flag': 'highlight_tick', 'name': 'Exit Spot', 'tick': 1584, 'tick_display_value': '1584.00'},
                            {'epoch': 1736459807, 'flag': 'highlight_time', 'name': 'End Time'},
                            {'epoch': 1736459808, 'tick': 1583.93, 'tick_display_value': '1583.93'},
                            {'epoch': 1736459810, 'tick': 1584.13, 'tick_display_value': '1584.13'},
                            {'epoch': 1736459812, 'tick': 1584.12, 'tick_display_value': '1584.12'}
                        ],
                        'contract_start': [
                            {'epoch': 1736459742, 'tick': 1583.53, 'tick_display_value': '1583.53'},
                            {'epoch': 1736459744, 'tick': 1584.03, 'tick_display_value': '1584.03'},
                            {'epoch': 1736459746, 'tick': 1583.53, 'tick_display_value': '1583.53'},
                            {'epoch': 1736459747, 'flag': 'highlight_time', 'name': 'Start Time'},
                            {'epoch': 1736459748, 'flag': 'highlight_tick', 'name': 'Entry Spot', 'tick': 1583.34, 'tick_display_value': '1583.34'},
                            {'epoch': 1736459750, 'tick': 1583.6, 'tick_display_value': '1583.60'},
                            {'epoch': 1736459752, 'tick': 1583.8, 'tick_display_value': '1583.80'}
                        ]
                    },
                    'barrier': '1583.34',
                    'barrier_count': 1,
                    'bid_price': 3.91,
                    'buy_price': 2,
                    'contract_id': 268936590908,
                    'contract_type': 'CALL',
                    'currency': 'USD',
                    'current_spot': 1584.12,
                    'current_spot_display_value': '1584.12',
                    'current_spot_time': 1736459812,
                    'date_expiry': 1736459807,
                    'date_settlement': 1736459807,
                    'date_start': 1736459747,
                    'display_name': 'Volatility 100 Index',
                    'entry_spot': 1583.34,
                    'entry_spot_display_value': '1583.34',
                    'entry_tick': 1583.34,
                    'entry_tick_display_value': '1583.34',
                    'entry_tick_time': 1736459748,
                    'exit_tick': 1584,
                    'exit_tick_display_value': '1584.00',
                    'exit_tick_time': 1736459806,
                    'expiry_time': 1736459807,
                    'is_expired': 1,
                    'is_forward_starting': 0,
                    'is_intraday': 1,
                    'is_path_dependent': 0,
                    'is_settleable': 1,
                    'is_sold': 1,
                    'is_valid_to_cancel': 0,
                    'is_valid_to_sell': 0,
                    'longcode': 'Win payout if Volatility 100 Index is strictly higher than entry spot at 1 minute after contract start time.',
                    'payout': 3.91,
                    'profit': 1.91,
                    'profit_percentage': 95.5,
                    'purchase_time': 1736459747,
                    'sell_price': 3.91,
                    'sell_spot': 1584,
                    'sell_spot_display_value': '1584.00',
                    'sell_spot_time': 1736459806,
                    'sell_time': 1736459808,
                    'shortcode': 'CALL_R_100_3.91_1736459747_1736459807_S0P_0',
                    'status': 'won',
                    'transaction_ids': {'buy': 536140917448, 'sell': 536141044328},
                    'underlying': 'R_100',
                    'validation_error': 'This contract has been sold.',
                    'validation_error_code': 'General'
                }
            },
            'false':{
                'status': False,
                'message': 'La posición fue perdedora',
                'loss': -2,
                'contract_details': {
                    'account_id': 243447828,
                    'audit_details': {
                        'contract_end': [
                            {'epoch': 1736191388, 'tick': 1450.91, 'tick_display_value': '1450.91'},
                            {'epoch': 1736191390, 'tick': 1450.51, 'tick_display_value': '1450.51'},
                            {'epoch': 1736191392, 'flag': 'highlight_tick', 'name': 'Exit Spot', 'tick': 1450.57, 'tick_display_value': '1450.57'},
                            {'epoch': 1736191393, 'flag': 'highlight_time', 'name': 'End Time'},
                            {'epoch': 1736191394, 'tick': 1451.03, 'tick_display_value': '1451.03'},
                            {'epoch': 1736191396, 'tick': 1451.55, 'tick_display_value': '1451.55'},
                            {'epoch': 1736191398, 'tick': 1451.56, 'tick_display_value': '1451.56'}
                        ],
                        'contract_start': [
                            {'epoch': 1736191328, 'tick': 1451.86, 'tick_display_value': '1451.86'},
                            {'epoch': 1736191330, 'tick': 1451.43, 'tick_display_value': '1451.43'},
                            {'epoch': 1736191332, 'tick': 1451.69, 'tick_display_value': '1451.69'},
                            {'epoch': 1736191333, 'flag': 'highlight_time', 'name': 'Start Time'},
                            {'epoch': 1736191334, 'flag': 'highlight_tick', 'name': 'Entry Spot', 'tick': 1451.14, 'tick_display_value': '1451.14'},
                            {'epoch': 1736191336, 'tick': 1451.7, 'tick_display_value': '1451.70'},
                            {'epoch': 1736191338, 'tick': 1451.44, 'tick_display_value': '1451.44'}
                        ]
                    },
                    'barrier': '1451.14',
                    'barrier_count': 1,
                    'bid_price': 0,
                    'buy_price': 2,
                    'contract_id': 268604865768,
                    'contract_type': 'CALL',
                    'currency': 'USD',
                    'current_spot': 1451.56,
                    'current_spot_display_value': '1451.56',
                    'current_spot_time': 1736191398,
                    'date_expiry': 1736191393,
                    'date_settlement': 1736191393,
                    'date_start': 1736191333,
                    'display_name': 'Volatility 100 Index',
                    'entry_spot': 1451.14,
                    'entry_spot_display_value': '1451.14',
                    'entry_tick': 1451.14,
                    'entry_tick_display_value': '1451.14',
                    'entry_tick_time': 1736191334,
                    'exit_tick': 1450.57,
                    'exit_tick_display_value': '1450.57',
                    'exit_tick_time': 1736191392,
                    'expiry_time': 1736191393,
                    'is_expired': 1,
                    'is_forward_starting': 0,
                    'is_intraday': 1,
                    'is_path_dependent': 0,
                    'is_settleable': 1,
                    'is_sold': 1,
                    'is_valid_to_cancel': 0,
                    'is_valid_to_sell': 0,
                    'longcode': 'Win payout if Volatility 100 Index is strictly higher than entry spot at 1 minute after contract start time.',
                    'payout': 3.91,
                    'profit': -2,
                    'profit_percentage': -100,
                    'purchase_time': 1736191333,
                    'sell_price': 0,
                    'sell_spot': 1450.57,
                    'sell_spot_display_value': '1450.57',
                    'sell_spot_time': 1736191392,
                    'sell_time': 1736191395,
                    'shortcode': 'CALL_R_100_3.91_1736191333_1736191393_S0P_0',
                    'status': 'lost',
                    'transaction_ids': {
                        'buy': 535479965788,
                        'sell': 535480153388
                    },
                    'underlying': 'R_100',
                    'validation_error': 'This contract has been sold.',
                    'validation_error_code': 'General'
                }
            }
        }

        return True
    
    def get_entrys_true(self):

        return self.entrys['true']
    
    def get_entrys_false(self):

        return self.entrys['false']
    