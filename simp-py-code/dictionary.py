#This has to do with some conversions
conversions = {
    "yotta" : "10^24",
    "zetta" : "10^21",
    "exa" : "10^18",
    "peta" : "10^15",
    "tera" : "10^12",
    "giga" : "10^9",
    "mega" : "10^6",
    "kilo" : "10^3",
    "hecto" : "10^2",
    "deka" : "10^1",
    }
print( conversions.get("exa"))
print( conversions["peta"])
print( conversions["yotta"])
print( conversions.get("kol", "invalid"))