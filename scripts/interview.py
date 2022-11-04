# Convert number to roman character

def ConvertNumberToRoman(number):
    num = [1, 4, 5, 9, 10, 40, 50, 90,
           100, 400, 500, 900, 1000]

    sym = ["I", "IV", "V", "IX", "X", "XL",
           "L", "XC", "C", "CD", "D", "CM", "M"]

    i = 12

    while number:
        div = number // num[i]
        number %= num[i]
        while div:
            print(sym[i], end="")
            div -= 1
        i -= 1


def mostFrequent(arr, n):
    arr.sort()

    # find the max frequency using linear travseal
    max_count = 1
    res = arr[0]
    curr_count = 1
    for i in range(1, n):
        if (arr[i] == arr[i - 1]):
            curr_count += 1
        else:
            curr_count = 1

        # if last element is most frequent
        if(curr_count > max_count):
            max_count = curr_count
            res = arr[i - 1]
    return res


def most_frequent(List):
    counter = 0
    num = List[0]

    for i in List:
        curr_frequency = List.count(i)
        if (curr_frequency > counter):
            counter = curr_frequency
            num = i

    return num

List = [2, 1, 2, 2, 1, 3]
print(most_frequent(List))

if __name__ == "__main__":
    # testing int to roman:
    number1 = 36500
    print("the Romain value is : ", end=" ")
    ConvertNumberToRoman(number1)

#     # testing the most frequent
#     # Driver Code
#     arr = [40, 50, 30, 40, 50, 30, 30, 8,8,8,8,8]
#     n = len(arr)
#     print(mostFrequent(arr, n))
