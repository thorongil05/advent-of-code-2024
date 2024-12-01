file_name = input("Insert file name: ")

if (file_name != "example.txt" and file_name != "input.txt"):
    raise ValueError("Wrong file")

first_location_id_list = []
second_location_id_list = []

with open(file_name, "r") as file:
    for line in file:
        splitted_element_list = line.strip().split("  ")
        first_location_id_list.append(int(splitted_element_list[0].strip()))
        second_location_id_list.append(int(splitted_element_list[1].strip()))

first_location_id_list.sort()
second_location_id_list.sort()

distance_list = []

for (list_a_elem, list_b_elem) in zip(first_location_id_list, second_location_id_list):
    distance_list.append(abs(list_a_elem - list_b_elem))

print(f"Distances: {distance_list}")
print(f"Total distance: {sum(distance_list)}")


number_similarity_map = {}
for element in second_location_id_list:
    number_similarity_map[element] = number_similarity_map.get(element, 0) + 1

print(f"Similarty map {number_similarity_map}")

similarty_list = []
for element in first_location_id_list:
    similarty_list.append(element * number_similarity_map.get(element, 0))

print(f"Similarities: {similarty_list}")
print(f"Total similarity {sum(similarty_list)}")