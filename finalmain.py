#Importing the libraries and modules
import multiprocessing as mp
import passengerflights
import airportnam
import mapper
import reducer
import combiner
import shuffle_and_sort
import taskoutput

#Install Pandas library to get Task Outputs as CSV files(pip install pandas)

if __name__ == '__main__':

	#Opening the Airportnames CSV file with utf8 encoding
	with open('Data/Top30_airports_LatLong(1).csv', encoding="utf8") as p:
		Airportdetails = airportnam.airports()    #Instantiating an Airportdetailts objects from Airportname class
		airportnames = Airportdetails.split_airportnames_csv(p)  #Splitting the CSV records by line using the methpd of the class
		print(f"Airport Details\n\n{airportnames}\n")#Printing Airportname details

	# Opening the Passengerdata CSV file with utf8 encoding
	with open('Data/AComp_Passenger_data_no_error(1).csv', encoding="utf8") as f:
		Passengerflightdetails = passengerflights.flights() #Instantiating an Passengerflight object from passengerflight class
		passenger_data = Passengerflightdetails.split_passengerflights_csv(f) #Splitting the CSV records by line using the methpd of the class
		print(f"Passenger Data \n\n{passenger_data}\n")#Printing Passenger data

	#Using python multprocessing to distribute data and workload to the available processors(Parelleism)
	with mp.Pool(processes=mp.cpu_count()) as pool:
		print("\n\nTask 1 \n\n")

		# Task1

		#1st Mapper finding and returning the Airport names with unique flight IDS
		Mapper1_uniqueflights = pool.map(mapper.Unique_flight_mapper, passenger_data, chunksize=int(len(passenger_data) / mp.cpu_count()))
		print(f"Mapper1_uniqueflights_output \n\n{Mapper1_uniqueflights}\n")
		#Shuffling the mapped data
		shuffled_airports = shuffle_and_sort.shuffles(Mapper1_uniqueflights)
		print(f"shuffled_airports_output \n\n{shuffled_airports}\n")
		#Combiner to combine Airport codes to Airport names
		Combiner_Airportnames = combiner.combiner_Airportcode_to_Name(shuffled_airports, airportnames)
		print(f"Combined_airports_output \n\n{Combiner_Airportnames}\n")
		# Sorting the combined data
		Sorted = shuffle_and_sort.sort(Combiner_Airportnames)
		print(f"Sorted_airports_output- Alphabetically \n\n{Sorted}\n")
		#Reducer used to reduce the mapped data to find the total number of flights from each airport
		Reducer1_total_flights_per_airport = pool.map(reducer.Sum_reducer, Sorted.items(), chunksize=int(len(Sorted.keys()) / mp.cpu_count()))
		print(f"Reducer1_total_flights_per_airport_outpout-Task1 output \n\n{Reducer1_total_flights_per_airport}\n")
		#Output the total number of flights from each airport as a CSV file(Task1_Output.csv)
		taskoutput.task1output(Reducer1_total_flights_per_airport)

		#Task2

		print("\n\nTask2\n\n")

		#2nd Mapper mapping the passengers
		Mapper2_passengers = pool.map(mapper.mapper_passengers, passenger_data, chunksize=int(len(passenger_data) / mp.cpu_count()))
		print(f"Mapper2_passengers_output \n\n{Mapper2_passengers}\n")
		#Shuffling the mapped data
		shuffle_passengers = shuffle_and_sort.shuffles(Mapper2_passengers)
		print(f"shuffle_passengers_output \n\n{shuffle_passengers}\n")
		#Cpmbiner to reduce and sum the passengers
		Combiner_sum_passengers = pool.map(combiner.Sum_combiner, shuffle_passengers.items(), chunksize=int(len(shuffle_passengers.keys()) / mp.cpu_count()))
		print(f"Combiner_sum_passengers_output \n\n{Combiner_sum_passengers}\n")
		#2nd Reducer to find the passenger with the highest number of flights
		Reducer2_passengers_with_highest_flights = reducer.reducer_highest_flights_per_person(Combiner_sum_passengers)
		print(f"Reducer2_passengers_with_highest_flights_output - task 2 ouput  \n\n{Reducer2_passengers_with_highest_flights}\n")
		# Output the passengers with the highest number of flights as a CSV file(Task2_Output.csv)
		taskoutput.task2output(Reducer2_passengers_with_highest_flights)



