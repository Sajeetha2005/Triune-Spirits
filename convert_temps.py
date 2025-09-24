import csv
line = None
def convert_temps(path):
  f = open(path,"r")
  lines = f.readlines()
  try:
    f.close()
  except Exception as e:
    print("Error closing file:", e)
  with open("converted_temps.csv", 'w') as f:
   try:
    f.write("celsius,fahrenheit,kelvin\n")
   except Exception as e:
    print("Error writing to file:", e)
   for line in lines[1:]:
    c = float(line.strip())
    f_value = (c * 9/5) + 32
    k = c + 273.15
    try:
      f.write(f"{c},{f_value},{k}\n")
    except Exception as e:
      print("Error writing to file:", e)
  print("Conversion done! Check converted_temps.csv")
convert_temps("temps.csv")
