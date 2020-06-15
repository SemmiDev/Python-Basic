from covid import Covid
covid = Covid()

def covid_worldwide():
	print("::: GLOBAL ::: ")
	print("Active cases : " ,covid.get_total_active_cases())
	print("Confirmed    : ",covid.get_total_confirmed_cases())
	print("Recovered 	: ",covid.get_total_recovered())
	print("Death 		: ",covid.get_total_deaths())
covid_worldwide()

indonesia = covid.get_status_by_country_name("indonesia")
data = {
	key	: indonesia[key]
	for key in indonesia.keys() and {
		 'confirmed',
		'active',
		'deaths',
		'recovered'
	}
}
print("::: INDONESIA :::")
print(data)