#!/usr/bin/env python


def Sum_reducer(tuple):
    """ Simple sum reducer which sums the mapped values
    	Args:
			tuple : Mapped Values
		Return:
			tuple : (key,sum of values) """

    k,v=tuple
    return (k, sum(v))


def reducer_highest_flights_per_person(list):
        """Single threaded Reducer to find the passenger with the highest number of flights
        	Args:
				list: summed passengers with number of flights
		    Return:
				list : list of passengers with the highest number of flights"""

        max = 0
        highest_passenger = []
        highest_passenger_output = []
        #Loop to find and assign the highest number of flights to max
        for k,v in list:
            if v>=max:
                max = v

        #Loop to add the passengers with the highest number of flights(max)
        for k,v in list:
            if v == max:
                highest_passenger.append(k)

        #Loop passengers with the highest number of flights(max) and append the list as a tuple
        for passenger in highest_passenger:
            highest_passenger_output.append((passenger,max))

        #Return the passenger with the highest number of flights
        return highest_passenger_output
