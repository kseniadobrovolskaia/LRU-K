import random as rnd


def find_lru(cache):
    min_value = cache[0][1]
    index = 0
    for i in range(len(cache)):
        if cache[i][1] <= min_value:
            min_value = cache[i][1]
            index = i
    return index


def find_same_request(cache, request):
    for i in range(len(cache)):
        if cache[i][0] == request:
            return i
    return -1


def find_empty_cell(cache):
    for i in range(len(cache)):
        if cache[i][0] == -1:
            return i


f_data = open('data.txt', 'w')
f_answer = open('answers.txt', 'w')

for j in range(5):
    cash_hit = 0

    size_cache = int(input('Enter len cache '))
    cache = [[-1, 0] for i in range(size_cache)]

    number_requests = int(input('Enter number of requests '))
    max_number = int(input('Enter max number request '))
    numbers = []
    for i in range(number_requests):
        numbers.append(rnd.randint(0, max_number))

    f_data.write(str(size_cache) + ' ' + str(number_requests) + ' ' + (' '.join(map(str, numbers))) + '\n')

    for i in range(number_requests):
        index = find_same_request(cache, numbers[i])
        if index >= 0:
            cache[index][1] = i
            cash_hit += 1
        elif cache[-1][1] == 0:
            index = find_empty_cell(cache)
            cache[index] = [numbers[i], i]
        else:
            lru_index = find_lru(cache)
            cache.pop(lru_index)
            cache.insert(lru_index, [numbers[i], i])

    f_answer.write(str(cash_hit) + '\n')

    print(cash_hit)

f_data.close()
f_answer.close()
