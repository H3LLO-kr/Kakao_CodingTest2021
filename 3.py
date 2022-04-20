import math

def time_operate(start_time, end_time):
    start_timel = start_time.split(':')
    end_timel = end_time.split(':')
    start_timel[0] = int(start_timel[0])
    start_timel[1] = int(start_timel[1])
    end_timel[0] = int(end_timel[0])
    end_timel[1] = int(end_timel[1])
    return (end_timel[0] - start_timel[0]) * 60 + end_timel[1] - start_timel[1]

def solution(fees, records):
    answer = []
    records_list = [0 for i in range(len(records))]
    car_list = [0 for i in range(10000)]
    for i in range(len(records)):
        records_list[i] = records[i].split()
    records_list
    for i in range(len(records)):
        if records_list[i][2] == 'IN':
            for j in range(i, len(records)):
                if records_list[i][1] == records_list[j][1] and records_list[j][2] == 'OUT':
                    car_list[int(records_list[i][1])] += time_operate(records_list[i][0], records_list[j][0])
                    break
                elif j == len(records) - 1:
                    car_list[int(records_list[i][1])] += time_operate(records_list[i][0], '23:59')
                    break
    for i in range(10000):
        if car_list[i] != 0:
            if car_list[i] <= fees[0]:
                answer.append(fees[1])
            else:
                answer.append(fees[1] + int(math.ceil(float(car_list[i] - fees[0]) / fees[2]) * fees[3]))
    return answer