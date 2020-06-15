# program konversi satuan temperature
print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input('Suhu dalam celcius : '))
print("== Suhu adalah ", celcius," Celcius")

reamur = (4/5) * celcius
print("reamur     ->  ", reamur," Reamur")

fahrenheit = ((9/5) * celcius) + 32
print("fahrenheit ->  ", fahrenheit," Fahrenheit")

kelvin = celcius + 273
print("kelvin     ->  ", kelvin," Kelvin")