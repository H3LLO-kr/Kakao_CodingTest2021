def solution(id_list, report, k):
    num_id = len(id_list)
    num_list = len(report)
    id_deced = [0 for i in range(num_id)]
    answer = [0 for i in range(num_id)]
    split_report = [0 for i in range(num_list)]
    for i in range(num_list):
        split_report[i] = report[i].split()
    for i in range(num_list):
        for j in range(i + 1, num_list):
            if split_report[i] == split_report[j]:
                split_report[j][1] = -1
    for i in range(num_list):
        for j in range(num_id):
            if split_report[i][0] == id_list[j]: split_report[i][0] = j
            if split_report[i][1] == id_list[j]: split_report[i][1] = j
    for i in range(num_list):
        if split_report[i][1] != -1:
            id_deced[split_report[i][1]] += 1
    for i in range(num_id):
        if id_deced[i] >= k:
            for j in range(num_list):
                if split_report[j][1] == i:
                    answer[split_report[j][0]] += 1
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))