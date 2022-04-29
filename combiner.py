def combiner_Airportcode_to_Name(passengeerdict, airportlist):
    """ Simple sum reducer which sums the mapped values
        	Args:
    			passengeerdict (dict): dictonary containg Airportcode and Flight Count 
    			airportlist (list) = List of Airport details
    		Return:
    			finallist : (Airport name, Flight count) """
    global_lookup_tables = {}
    finallist = []
    
    #Loop through Airport File lines
    for line in airportlist:
        #Split lines
        cols = line.split(',')

        # If the number of columns are only greater than 1 add the Airport name and Airport code to the global lookup table
        # Used to handle missing rows in the Airport names dataset
        if len(cols) > 1:
            #Add airport code and Name to global lookup table
            global_lookup_tables[cols[1]] = cols[0]
            
    #Loop through Airport code and Flight count of Mapped Passenger Flight data
    for Airportcode, flightcount in passengeerdict.items():
        #Loop through global lookup table
        for key, Airportname in global_lookup_tables.items():
            #If Airport code in Mapped data equals to Airport code in Global lookup table
            if Airportcode == key:
                #Add Airport name and Flightcount to final list
                finallist.append((Airportname, flightcount))
    # Return list of Airport name and Flightcount
    return finallist


def Sum_combiner(tuple):
    """ Simple sum reducer which sums the mapped values
    	Args:
			tuple : Mapped Values
		Return:
			tuple : (key,sum of values) """

    k, v = tuple
    return (k, sum(v))
