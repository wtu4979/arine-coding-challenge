import json

# Open file and load JSON data into sample_data
f = open('sample_data.json')
sample_data = json.load(f)

# print(sample_data["medications"])

# Write a program that prints the numbers from 1 to 100. But for multiples of 3 print “Fizz” instead
# of the number and for the multiples of 5 print “Buzz”. For numbers which are multiples of both 3
# and 5 print “FizzBuzz”.
# Use the following function signature:
# def fizzbuzz() -> None

def fizzbuzz() -> None:
    # Iterate through numbers 1 to 100 and print Fizz, Buzz, FizzBuzz, or the number
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz()

# Write a function that takes a string that may be a float, and returns either the converted string as
# float or the default value provided as an argument if the string does not represent a float.
# Use the following function signature:
# def convert_to_float(input_str: str, default: float) -> float

def convert_to_float(input_str: str, default: float) -> float:
    # Try to convert input_str to float, return default if ValueError is raised
    try:
        return float(input_str)
    except ValueError:
        return default


print(convert_to_float("1.2", 0.0))

# Write a function that takes a data object (see Sample Data Object below) as an argument and
# returns the list of all medications that have “antihtn” in their “drugGroup”. If there are no
# matching medications, return an empty list.
# Use the following function signature:
# def get_antihtn_meds(data_obj: dict) -> list

def get_antihtn_meds(data_obj: dict) -> list:
    antihtn_meds = []
    # Iterate through medications and append brandName to antihtn_meds if drugGroup contains "antihtn"
    for med in data_obj["medications"]:
        # drugGroup is a list of strings, so check if "antihtn" is in the list
        if "antihtn" in med["drugGroup"]:
            antihtn_meds.append(med["brandName"])
    return antihtn_meds

print(get_antihtn_meds(data_obj=sample_data))

# Write a function that takes a data object (see Sample Data Object below) as an argument and
# returns the list of medications whose “doseForm” is any form of “tablet”. If there are no
# matching medications, return an empty list.
# Use the following function signature:
# def get_tablet_meds(data_obj: dict) -> list

def get_tablet_meds(data_obj: dict) -> list:
    tablet_meds = []
    # Iterate through medications and append brandName to tablet_meds if doseForm is a tablet
    for med in data_obj["medications"]:
        # doseForm is a list of strings, so check if "tablet" is in the list
        if "tablet" in med["doseForm"]:
            tablet_meds.append(med["brandName"])
    return tablet_meds

print(get_tablet_meds(data_obj=sample_data))

# Write a function that takes a data object (see Sample Data Object below) as an argument and
# returns the “ndc9” value of the medication that was filled most recently. If there’s a tie, return
# any of the “ndc9” for medications filled on that day. If there are no medications, return None.
# Use the following function signature:
# def get_latest_med_ndc(data_obj: dict) -> Optional[str]

from typing import Optional

def get_latest_med_ndc(data_obj: dict) -> Optional[str]:
    medications = data_obj.get('medications')
    # Returns None if medications is None or empty
    if not medications:
        return None

    latest_fill_date = None
    latest_ndc9 = None

    # Iterate through medications and fills to find the latest fill date and corresponding ndc9
    for medication in medications:
        fills = medication.get('fills')
        if not fills:
            continue

        for fill in fills:
            fill_date = fill.get('fillDate')
            # Only update latest_fill_date and latest_ndc9 if fill_date is not None and is more recent than latest_fill_date
            if fill_date and (latest_fill_date is None or fill_date > latest_fill_date):
                latest_fill_date = fill_date
                latest_ndc9 = medication.get('ndc9')

    return latest_ndc9


print(get_latest_med_ndc(data_obj=sample_data))

# Close file
f.close()
