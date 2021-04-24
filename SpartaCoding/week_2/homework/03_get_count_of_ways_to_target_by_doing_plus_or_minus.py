numbers = [1, 1, 1, 1, 1]
target_number = 3
result_count = 0

def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index, current_sum):
    # 구현해보세요!
    # 종료조건: target_number를 찾은 경우
    if current_index == len(array):
        if current_sum == target:
            global result_count
            result_count += 1  # 총 횟수
        return

    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index + 1,
                                                       current_sum + array[current_index])
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index + 1,
                                                       current_sum - array[current_index])


get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number, 0, 0)  # 5를 반환해야 합니다!
print(result_count)