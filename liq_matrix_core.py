import data_receiving


class LiqMatrixCore:
    def __init__(self):
        self.receiving = data_receiving.DataReceiving()

        print("core loaded")

    def run_data_receiving(self):
        self.receiving.run_trades_datastream_from_server()

