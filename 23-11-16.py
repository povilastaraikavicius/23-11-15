# from typing import List


# person = {
#     "name": "Vytautas",
#     "surname": "Sluckas",
#     "ip": "127.0.0.1",
#     "programming_language": "python",
#     "address": {"Street": "some street", "House Number": "some house number"},
#     "languages": ["Lithuanian", "English", "Norwegian"],
# }

# person1 = {
#     "name": "Tomas",
#     "surname": "BLABLABA",
#     "ip": "127.0.0.1",
#     "programming_language": "python",
#     "address": {"Street": "some street", "House Number": "some house number"},
#     "languages": ["Latvian", "English", "Swedish"],
# }

# people = [person, person1]


# def get_most_popular_language(people: List[dict]) -> str:
#     languages_dictionary = {}
#     for person in people:
#         languages = person.get("languages")
#         for language in languages:
#             languages_dictionary[language] = languages_dictionary.get(language, 0) + 1

#     return max(languages_dictionary, key=languages_dictionary.get)


# print(get_most_popular_language(people))
# create dictionary with language counts
# for person in people:
# get persons languages
# for language in languages:
# if language is new:
# add key to dictionary with language counts
# else if langauge is not new:
# add count +1 to already existing language in dictionary with language counts


# def get_most_popular_language(people: List[dict]) -> str:
#     dictionary_language_counts = {}

#     for person in people:
#         languages = person.get("languages", [])
#         for language in languages:
#             if language in dictionary_language_counts:
#                 dictionary_language_counts[language] += 1
#             else:
#                 dictionary_language_counts[language] = 1


#     return max(dictionary_language_counts, key=dictionary_language_counts.get)


# result = get_most_popular_language(people)
# print("The most popular language is:", result)


# kitas budas


# from typing import List


# person = {
#     "name": "Vytautas",
#     "surname": "Sluckas",
#     "ip": "127.0.0.1",
#     "programming_language": "python",
#     "address": {"Street": "some street", "House Number": "some house number"},
#     "languages": ["Lithuanian", "English", "Norwegian"],
# }

# person1 = {
#     "name": "Tomas",
#     "surname": "BLABLABA",
#     "ip": "127.0.0.1",
#     "programming_language": "python",
#     "address": {"Street": "some street", "House Number": "some house number"},
#     "languages": ["Latvian", "English", "Swedish"],
# }

# people = [person, person1]


# def get_most_popular_language(people: List[dict]) -> str:
#     language_counts = {}
#     for human in people:
#         for language in human["languages"]:
#             if language in language_counts:
#                 language_counts[language] += 1
#             else:
#                 language_counts[language] = 1

#     max_value = None
#     max_key = None
#     for key, value in language_counts.items():
#         if max_key == None or max_value < value:
#             max_value, max_key = value, key
#     return max_key


# result = get_most_popular_language(people)
# print("The most popular language is:", result)
# dic_one = {"a": 1, "b": 2, "c": 3}
# dict_two = {"d": 20, "b": 30, "c": 40}
# dict_three = {"h": 5, "j": 15, "c": 4}
# dict_four = {"d": 8, "b": 7, "c": 2}


# def custom_dictionary_update(
#     first_dictionary: dict, second_dictionary: dict, overwrite: bool = True
# ) -> dict:
#     if overwrite == True:
#         first_dictionary.update(second_dictionary)
#     else:
#         for key, value in second_dictionary.items():
#             first_dictionary[key] = value
#     return first_dictionary


# result = custom_dictionary_update(dict_three, dict_four, False)
# print(result)


# if overwrite == True:
#   update first dictioanry with the second one as with dictionary update method
# else:
#   do not overwrite values from the first dictionary, only add new values from the second one.


# new exercises


from typing import List


person = {
    "name": "Vytautas",
    "surname": "Sluckas",
    "ip": "127.0.0.1",
    "programming_language": "python",
    "address": {"Street": "some street", "House Number": "some house number"},
    "languages": ["Lithuanian", "English", "Norwegian"],
}

person1 = {
    "name": "Tomas",
    "surname": "BLABLABA",
    "ip": "162.2.0.2",
    "programming_language": "python",
    "address": {"Street": "some street", "House Number": "some house number"},
    "languages": ["Latvian", "English", "Swedish"],
}

person2 = {
    "name": "Tom",
    "surname": "Edison",
    "ip": "127.2.0.1",
    "programming_language": "python",
    "address": {"Street": "some street", "House Number": "some house number"},
    "languages": ["Latvian", "English", "Swedish"],
}


people = [person, person1, person2]

person = {
    "name": "Vytautas",
    "surname": "Sluckas",
    "ip": "127.0.0.1",
    "programming_language": "python",
    "address": {"Street": "some street", "House Number": "some house number"},
    "languages": ["Lithuanian", "English", "Norwegian"],
}

person1 = {
    "name": "Tomas",
    "surname": "BLABLABA",
    "ip": "162.2.0.2",
    "programming_language": "python",
    "address": {"Street": "some street", "House Number": "some house number"},
    "languages": ["Latvian", "English", "Swedish"],
}

person2 = {
    "name": "Tom",
    "surname": "Edison",
    "ip": "127.2.0.1",
    "programming_language": "python",
    "address": {"Street": "some street", "House Number": "some house number"},
    "languages": ["Latvian", "English", "Swedish"],
}

people = [person, person1, person2]
filtered_people = []

for person in people:
    if person["ip"].split(".")[1] == "2":
        filtered_people.append(person)

# for person in filtered_people:
#     print(f"Name: {person['name']}, IP: {person['ip']}")

print(filtered_people)
