#!/usr/bin/env python

unique_flight_id = []
def Unique_flight_mapper(line):
	""" Find the Unique Flights from the Passenger data and then return the Airport Name with unique flights
		Args:
				line (list): Passenger details file lines
		Return:
				tuple : (Airportname,1) """
	#Split the lines
	cols = line.split(',')

	#Finding Unique flights only if the flight has a Unique Flight ID (Can avoid errors for the Test dataset)
	if cols[1] != "":
		if cols[1] not in unique_flight_id:
			#Append Unique flights to the list
			unique_flight_id.append(cols[1])
			#Return the Airport name with the unique flight
			return (cols[2], 1)


def mapper_passengers(line):
		"""Mapping the Passengers
			Args:
				line (list): Passenger details file lines
			Return:
				tuple : (PassengerID,1) """

		#Split the lines
		cols = line.split(',')
		#Return the passenger only if passenger has an ID (Can avoid errors for the Test dataset)
		if cols[0] != "":
			return (cols[0],1)


