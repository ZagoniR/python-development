# Homework (Memory savers and files)

import uuid
import csv
import os
import json

# Create a list of cars, where the properties of each car are represented by a list
cars = [{"brand": "Opel",
         "model": "Insignia",
         "hp": 180,
         "price": 6000
         },
        {"brand": "Opel",
         "model": "Astra",
         "hp": 180, "price": 6000
         },
        {"brand": "Ford",
         "model": "Mondeo",
         "hp": 100,
         "price": 1700
         },
        {"brand": "Kia",
         "model": "Sportage",
         "hp": 210,
         "price": 16000
         },
        {"brand": "Mercedes",
         "model": "A180",
         "hp": 220,
         "price": 29000
         },
        {"brand": "Dacia",
         "model": "Duster",
         "hp": 130,
         "price": 16000
         },
        {"brand": "Toyota",
         "model": "Corolla",
         "hp": 90,
         "price": 900
         },
        {"brand": "Skoda",
         "model": "Fabia",
         "hp": 65,
         "price": 1000
         }]

# Generate a unique id for each car
for car in cars:
    car["id"] = uuid.uuid1()

# Print the cars list
print("Cars list:", cars)


# Create a function that prints a car ranking (sorted)
def print_cars_ranking(cars_list, display_property, rank_type, ranking_criteria):
    print(ranking_criteria,
          [car_rank[display_property] for car_rank in sorted(cars_list, key=lambda car_rank: car_rank[rank_type])])


# Create a list with the slowest cars (less than 120 horse power), sort it and print the car brand
slow_cars = list(filter(lambda car_rank: car_rank["hp"] < 120, cars))
print_cars_ranking(slow_cars, "model", "hp", "Slow cars:")

# Create a list with the fastest cars (starting from 120 horse power but less that 180), sort it and print the car brand
fast_cars = list(filter(lambda car_rank: 120 <= car_rank["hp"] < 180, cars))
print_cars_ranking(fast_cars, "model", "hp", "Fast cars:")

# Create a list with the sport cars (more than 180 horse power), sort it and print the car brand
sport_cars = list(filter(lambda car_rank: car_rank["hp"] >= 180, cars))
print_cars_ranking(sport_cars, "model", "hp", "Sport cars:")

# Create a list with the cheapest cars (price less than 1000), sort it and print the car brand
cheap_cars = list(filter(lambda car_rank: car_rank["price"] < 1000, cars))
print_cars_ranking(cheap_cars, "model", "price", "Cheap cars:")

# Create a list with medium cars (price starting from 1000 and less than 5000), sort it and print the car brand
medium_cars = list(filter(lambda car_rank: 1000 <= car_rank["price"] < 5000, cars))
print_cars_ranking(medium_cars, "model", "price", "Medium cars:")

# Create a list with the most expensive cars (price starting from 5000), sort it and print the car brand
expensive_cars = list(filter(lambda car_rank: car_rank["price"] >= 5000, cars))
print_cars_ranking(expensive_cars, "model", "price", "Expensive cars:")

# =================================================================================================================

# Create a folder
folder_path = "C:/Users/HP/PycharmProjects/python-development/memory-saver-files/output_data"
try:
    os.mkdir(folder_path)
except OSError as error:
    print(error)


# Create a class to encode the uuid id
class UUIDEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, uuid.UUID):
            # If the obj is uuid, we simply return the value of uuid
            return obj.hex
        return json.JSONEncoder.default(self, obj)


# Create function that creates a JSON Object for a car ranking
def cre_json_obj(car_rank_name, car_rank_list):
    json_obj = {car_rank_name: []}
    for target_car in car_rank_list:
        json_obj[car_rank_name].append(target_car)
    return json_obj


# Create a function that takes a list of dictionaries and ads all key and values to a csv file
def add_dict_to_csv(file_name, list_of_dict):
    with open(file_name, "w") as file:
        csv_writer = csv.writer(file, delimiter=",")
        for entry in list_of_dict:
            for key, value in entry.items():
                csv_writer.writerow([key, value])


# Create a function that reads all the data from a csv file and returns a list
def read_csv_file(file_name):
    car_list = []
    with open(file_name, "r") as csv_file:
        rows = csv.reader(csv_file, delimiter=",")
        for row in rows:
            car_list.append(row)
    return car_list


# Write object to a json file
def write_obj_json_file(file_name, car_list):
    path = folder_path + "/" + file_name
    with open(path, 'w') as jsonFile:
        json.dump(cre_json_obj("car details: ", car_list), jsonFile, cls=UUIDEncoder)


# Create the json file for each car ranking
def cre_json_file(source_file, cars_list, file_name):
    add_dict_to_csv(source_file, cars_list)
    write_obj_json_file(file_name, read_csv_file(source_file))


cre_json_file("input.csv", slow_cars, "slow_cars.json")
cre_json_file("input.csv", fast_cars, "fast_cars.json")
cre_json_file("input.csv", sport_cars, "sport_cars.json")
cre_json_file("input.csv", cheap_cars, "cheap_cars.json")
cre_json_file("input.csv", medium_cars, "medium_cars.json")
cre_json_file("input.csv", expensive_cars, "expensive_cars.json")


# Create a function to create a json file with car brand details
def cre_brand_json_file(source_file, brand):
    brand_cars = list(filter(lambda car_brand: car_brand["brand"] == brand, cars))
    cre_json_file(source_file, brand_cars, brand + ".json")


# Example to create a file with brand details
cre_brand_json_file("input.csv", "Opel")
cre_brand_json_file("input.csv", "Mercedes")
