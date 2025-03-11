from os import remove

brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

brand["number_stores"] =2

clients = brand["type_of_clothes"]

clients_sentence = f"Zara's clients are {', '.join(clients[:-1])}, and {clients[-1]}."
print(clients_sentence)
#4 Add new key-value
brand["country_creation"] = "Spain"
#5 check
if "international_competitors"in brand:
    brand["international_competitors"].append("Desigual")
#6
del brand["creation_date"]
#7
print(brand["international_competitors"][-1])
#8
us_colors = brand["major_color"]["US"]
# 9

print(f"The major clothes colors in the US are: {', '.join(us_colors)}")

#10
print(len(brand))

#11
print(brand.keys() )

#12
# Create the more_on_zara dictionary
more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}


