distances_tupples = [
    ("Bansko", 97),
    ("Belgium - Brussels", 1701),
    ("Egypt - Alexandria", 1403),
    ("France - Nice", 1307),
    ("Hungary - Szeged", 469),
    ("Ireland - Dublin", 2479),
    ("Italy - Palermo", 987),
    ("Norway - Oslo", 2098),
    ("Russia - Moscow", 1779),
    ("Spain - Madrid", 2259),
    ("United Kingdom - London", 2019)
]

# dist_names = []
# distances = []

# for t in distances_tupples:
#     dist_names.append(t[0])
#     distances.append(t[1])


dist_names = [dist[0] for dist in distances_tupples]
distances = [dist[1] for dist in distances_tupples]

print(dist_names)
print(distances)
