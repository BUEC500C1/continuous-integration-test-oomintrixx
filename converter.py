# ============================================================
# Defining my own functions here
# ============================================================

def distanceConvert(val, input_unit, output_unit):
    METER = ["m", "meter", "M", "Meter", "METER", "meters"]
    FEET = ["ft", "FT", "FEET", "feet", "Feet", "feets"]
    INCH = ["INCH", "inch", "inches"]
    MILE = ["miles", "Miles"]

    meter = 1.0
    feet = 3.28084
    inches = 39.3701
    miles = 0.000621371

    if input_unit in METER:
        val /= meter
    if input_unit in FEET:
        val /= feet
    if input_unit in INCH:
        val /= inches
    if input_unit in MILE:
        val /= miles

    if output_unit in METER:
        val *= meter
    if output_unit in FEET:
        val *= feet
    if output_unit in INCH:
        val *= inches
    if output_unit in MILE:
        val *= miles

    return val

def weightConvert(val, input_unit, output_unit):
    KILOGRAM = ["kg", "KG", "kilogram", "KILOGRAM"]
    OUNCE = ["Oz", "ounces", "ounce"]
    POUND = ["pound", "pounds", "POUND", "POUNDS"]

    kilogram = 1.0
    ounces = 35.274
    pounds = 2.20462

    if input_unit in KILOGRAM:
        val /= kilogram
    if input_unit in OUNCE:
        val /= ounces
    if input_unit in POUND:
        val /= pounds


    if output_unit in KILOGRAM:
        val *= kilogram
    if output_unit in OUNCE:
        val *= ounces
    if output_unit in POUND:
        val *= pounds

    return val

def temperatureConvert(val, input_unit, output_unit):
    FAHRENHEIT = ["F", "FAHRENHEIT", "Fahrenheit"]
    CELCIUS = ["C", "CELCIUS", "Celcius"]

    if input_unit in FAHRENHEIT:
        if output_unit in FAHRENHEIT:
            return val
        if output_unit in CELCIUS:
            return (val - 32) * 5 / 9

    if input_unit in CELCIUS:
        if output_unit in FAHRENHEIT:
            return 9 / 5 * val + 32
        if output_unit in CELCIUS:
            return val

    return -1


def extractUnitType(text):
    val = 0
    valIdx = -1
    unit_1 = ""
    unit_2 = ""
    unit_type = ""
    DISTANCE = ["meters", "m", "meter", "M", "Meter", "METER","ft", "FT", "FEET", "feet", "Feet","INCH", "inch","miles", "Miles"]
    WEIGHT = ["kg", "KG", "kilogram", "KILOGRAM", "Oz", "ounces", "ounce", "pound", "pounds", "POUND", "POUNDS"]
    TEMPERATURE = ["F", "FAHRENHEIT", "Fahrenheit", "C", "CELCIUS", "Celcius"]
    textlist = text.split(" ")
    for i in textlist:
        if i.replace(".", "", 1).isdigit():
            val = i
            valIdx = text.find(val)

    for dis1 in DISTANCE:
        if dis1 in textlist:
            for dis2 in DISTANCE:
                if dis2 in textlist and dis2 != dis1:
                    dis1Idx = text.find(dis1)
                    dis2Idx = text.find(dis2)
                    if valIdx != -1 and dis1Idx > valIdx and abs(valIdx - dis1Idx) < abs(valIdx - dis2Idx):
                        unit_1 = dis1
                        unit_2 = dis2
                        unit_type = "distance"
                        break

                    if valIdx != -1 and dis2Idx > valIdx and abs(valIdx - dis2Idx) < abs(valIdx - dis1Idx):
                        unit_1 = dis2
                        unit_2 = dis1
                        unit_type = "distance"
                        break

    for wght1 in WEIGHT:
        if wght1 in text:
            for wght2 in WEIGHT:
                if wght2 in textlist and wght2 != wght1:
                    wght1Idx = text.find(wght1)
                    wght2Idx = text.find(wght2)
                    if valIdx != -1 and wght1Idx > valIdx and abs(valIdx - wght1Idx) < abs(valIdx - wght2Idx):
                        unit_1 = wght1
                        unit_2 = wght2
                        unit_typ2 = "weight"
                        break

                    if valIdx != -1 and wght2Idx > valIdx and abs(valIdx - wght2Idx) < abs(valIdx - wght1Idx):
                        unit_1 = wght2
                        unit_2 = wght1
                        unit_type = "weight"
                        break

    for temp1 in TEMPERATURE:
        if temp1 in text:
            for temp2 in TEMPERATURE:
                if temp2 in textlist and temp2 != temp1:
                    temp1Idx = text.find(temp1)
                    temp2Idx = text.find(temp2)
                    if valIdx != -1 and temp1Idx > valIdx and abs(valIdx - temp1Idx) < abs(valIdx - temp2Idx):
                        unit_1 = temp1
                        unit_2 = temp2
                        unit_typ2 = "temperature"
                        break

                    if valIdx != -1 and temp2Idx > valIdx and abs(valIdx - temp2Idx) < abs(valIdx - temp1Idx):
                        unit_1 = temp2
                        unit_2 = temp1
                        unit_type = "temperature"
                        break

    return unit_1, unit_2, unit_type, val

def unitConverter(text):
    unit_1, unit_2, unit_type, val = extractUnitType(text)
    val = float(val)
    if(unit_type == "distance"):
        return str(distanceConvert(val, unit_1, unit_2)) + " " + unit_2
    if(unit_type == "weight"):
        return str(weightConvert(val, unit_1, unit_2)) + " " + unit_2
    if(unit_type == "temperature"):
        return str(temperatureConvert(val, unit_1, unit_2)) + " " + unit_2

    return "Not a valid request!"

if __name__ == "__main__":
    #print(defineUnitType("convert 12.5 miles to meters"))

    print("what do you want to convert?")
    text = input()
    print(unitConverter("convert 12.5 miles to meters"))
