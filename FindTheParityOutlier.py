def find_outlier(integers):
    sub1 = []
    sub2 = []
    for i in integers:
        if i % 2 == 0:
            sub1.append(i)
        else:
            sub2.append(i)

    return sub1[0] if len(sub1) < len(sub2) else sub2[0]