'''

Task2

'''

def merge_func(array, LID=0, RID=None):
    RID = RID or len(array)

    if RID - LID > 1:

        midvalue = (LID + RID) // 2
        merge_func(array, LID, midvalue)
        merge_func(array, midvalue, RID)

        merged = []
        i = LID
        j = midvalue
        while i < midvalue and j < RID:
            if array[i] <= array[j]:
                merged.append(array[i])
                i = i + 1
            else:
                merged.append(array[j])
                j = j + 1

        merged.extend(array[i:midvalue])
        array[LID:LID + len(merged)] = merged
    return array


if __name__ == '__main__':
    array = [10, 11, 32, 56, 1]
    print(merge_func(array))