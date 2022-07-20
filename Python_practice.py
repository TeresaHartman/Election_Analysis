# print("Hello World")

# #counties = ["Arapahoe", "Denver", "Jefferson"]
# if counties[1] == 'Denver':
#     print(counties[1])

# if counties[3] != 'Jefferson':
#     print(counties[2])

# temperature = int(input("What is the temperatue outside? "))

# if temperature > 80:
#     print("Turn on the AC.")

# else:
#     print("Open the windows.")

# counties = ["Arapahoe","Denver","Jefferson"]
# # if "El Paso" in counties:
# #     print("El Paso is in the list of counties.")
# # else:
# #     print("El Paso is not the list of counties.")

# # for county in counties:
# #     print(county)

# for i in range(len(counties)):
#     print(counties[i])

# counties_tuples = ("Arapahoe","Denver","Jefferson")
# for i in len(counties_tuples):

#       print(counties_tuples[i])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# for county in counties_dict.keys():
#     print(county)

# for voters in counties_dict.values():
#     print(voters)

for county, voters in counties_dict.items():
#     #print(county, voters)
#     print(county + "county has " + str(voters) + " registered voters.")
    #could also use the follow with the "f" to not have to use str. but then need to use {}
    print(f"{county} county has {voters} registered voters.")

# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                 {"county":"Denver", "registered_voters": 463353},
#                 {"county":"Jefferson", "registered_voters": 432438}]

# for county_dict in voting_data:
#     print(county_dict)

# for county in range(len(voting_data)):
#     print(county)

# for county_dict in voting_data:
#     print(county_dict['registered_voters'])