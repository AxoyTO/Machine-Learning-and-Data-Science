def longestCommonPrefix(x):
    total_elements = len(x)
    x_without_space = x
    for i in range(0, total_elements):
        str = ""
        ch_flag = 0
        for j in range(0, len(x[i])):
            if x[i][j] != " " and ch_flag == 0:
                str = str + x[i][j]
                ch_flag = 1
            elif ch_flag == 1:
                str = str + x[i][j]
        # print(str)
        x_without_space[i] = str

    # print(x_without_space)

    min_len = len(x_without_space[0])
    element_min_len = 0
    for i in range(1, total_elements):
        if len(x_without_space[i]) < min_len:
            min_len = len(x_without_space[i])
            element_min_len = i

    # print(x_without_space)
    # print(element_min_len)
    # print(min_len)

    count = 0
    br_flag = 0
    j = 0

    for j in range(0, min_len):
        for i in range(0, total_elements-1):
            # print("[{}][{}] = ".format(i, j) + x_without_space[i][j] +
            #      " ---- [{}][{}] = ".format(i+1, j) + x_without_space[i+1][j])
            if x_without_space[i][j] != x_without_space[i+1][j]:
                br_flag = 1
                break
        if(br_flag == 1):
            break
        else:
            count += 1

    # print(count)
    result = x_without_space[element_min_len][:count]
    # print(result)
    if count == 0:
        return ""
    count += 1
    return result


'''
    for i in range(0, total_elements-1):
        for j in range(0, min_len):
            print("[{}][{}] = ".format(i, j) + x_without_space[i][j] +
                  " ---- [{}][{}] = ".format(i+1, j) + x_without_space[i+1][j])
            if x_without_space[i][j] != x_without_space[i+1][j]:
                br_flag = 1
                break
            else:

        if(br_flag == 1):
            break
        else:
            count += 1
'''


if __name__ == "__main__":
    print(longestCommonPrefix(
        ["123", " 1 23", "12 3"]))
