import data_calculations


class DataReceiving:
    def __init__(self):

        self.data_calc = data_calculations.DataCalculations()

        print("data reveiving loaded")
    def run_datastream_from_server(self):
        print("run datastream from server engaged.")
        print("first data obtained")

        self.calculate_received_data()

    def calculate_received_data(self):
        self.data_calc.calculate_params()
