def numbers(contra):
    count = 0
    lsst = []
    for i in contra:
        if i[-1]  not in 'aeiou':
            count += 1
            lsst.append(i)
    return count, lsst

listt = ['asd','dasda','sssa']
print(numbers(listt))
