import data_calculations
import websocket
import json
import time
import pprint
from binance.exceptions import BinanceAPIException
from requests.exceptions import ReadTimeout
from requests.exceptions import ConnectionError


class DataReceiving:
    def __init__(self):

        self.data_calc = data_calculations.DataCalculations()

        self.connection_error = False

        print("data reveiving loaded")

    def run_trades_datastream_from_server(self):

        trades_stream_socket = 'wss://fstream.binance.com/ws/xmrusdt@aggTrade'

        try:
            ws = websocket.WebSocketApp(trades_stream_socket,
                                        on_message=self.recent_trades_datastream_message,
                                        on_close=self.recent_trades_datastream_close)

        except BinanceAPIException as e:
            print(f"Trades Datastream Error: {e.message}")

        except ReadTimeout:
            pass

        except ConnectionError:
            pass

        except AttributeError:
            pass

        else:
            ws.run_forever(ping_interval=20)

    def recent_trades_datastream_message(self, ws, message):
        if self.connection_error:
            print("TRADES DATA STREAM CONNECTION RE-ESTABLISHED.")

            self.connection_error = False

        data = json.loads(message)

        is_buyer_mm = data['m']
        price = data['p']
        quantity = data['q']
        number_of_trades = int(data['l']) - int(data['f']) + 1

        print(f"Price: {price}, Qunatity: {quantity}, Number of trades: {number_of_trades}, Is buyer MM: {is_buyer_mm}.")

        # self.calculate_received_data()

    def recent_trades_datastream_close(self, ws):
        if not self.connection_error:
            print("TRADES DATA STREAM CONNECTION TERMINATED")

            self.connection_error = True

        time.sleep(10)
        self.run_trades_datastream_from_server()

    def calculate_received_data(self):
        self.data_calc.calculate_params()


