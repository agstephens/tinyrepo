def get_intersection(set1, set2):
    l1 = [i for i in set1]
    l2 = [i for i in set2]

    intersect = []
    for i1 in l1:
        if i1 in l2:
            intersect.append(i1)

    return set(intersect)


print(get_intersection({1, 2, 3}, {2, 3, 4}))

