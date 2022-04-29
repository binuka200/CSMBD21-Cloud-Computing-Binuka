class airports():
    """Airport details Class"""

    def __init__(self):
        self.airportnames = []


    def split_airportnames_csv(self,file):
        """Method to seperate lines of Airport Details
        Args:
			file : Airport Details file
		Return:
			list : list of Airport Details """

        #Seperate lines of Airport Details file
        self.airportnames = file.read().splitlines()
        return self.airportnames
