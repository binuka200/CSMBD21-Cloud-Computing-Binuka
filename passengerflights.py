class flights():
    """Passenger and Flight Details class"""

    def __init__(self):
        self.passengerflightdetails = []

    def split_passengerflights_csv(self,file):
        """Method to seperate lines of Passenger Details
        Args:
			file : Passenger details Details file
		Return:
			list : list of Passenger and Flight Details """

        # Seperate lines of Passenger Details file
        self.passengerflightdetails = file.read().splitlines()
        return self.passengerflightdetails