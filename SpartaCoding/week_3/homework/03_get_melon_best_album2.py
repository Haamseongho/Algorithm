genres = ["classic", "pop", "classic", "classic", "pop", "balad"]
plays = [500, 600, 150, 800, 2500,700]


def get_melon_best_album(genre_array, play_array):
    genre_play_list_dict = {}
    genre_total_list_dict = {}
    n = len(genre_array)
    for i in range(n):
        genre = genre_array[i]  # 장르 순서대로 가져오기
        play = play_array[i]  # 장르 순서에 맞게 관객수 가져오기
        if genre not in genre_play_list_dict:  # 장르가 장르랑 관객수 같이 리스트업 하는 딕셔너리에 있는지 파악
            genre_play_list_dict[genre] = [[i, play]]  # 없을 경우 그냥 넣어주기
        else:  # 만약에 있다면 append로 추가해주기 (i가 덮어 씌워지는 이슈를 막기 위함)
            genre_play_list_dict[genre].append([i, play])


    print(genre_play_list_dict)

    # 합계를 나타내는 dict
    for i in range(n):
        genre = genre_array[i]
        play = play_array[i]
        if genre not in genre_total_list_dict:  # 장르의 합계를 관리하는 딕셔너리에 장르가 없을 경우
            genre_total_list_dict[genre] = play  # 해당 장르에 대해서 관객수만 더해줄 것
        else:
            genre_total_list_dict[genre] += play  # 기존 탐색했던 딕셔너리 내 더해야 할 장르가 존재할 경우 관객수를 거기에다가 추가로 더해줄 것

    print(genre_total_list_dict)

    # 클래식과 팝 중에 더 합계가 높은 것 먼저 가지고 오기
    # 그 장르 중 관객수가 더 많은 키를 배열에 넣기

    sorted_total_list_dict = sorted(genre_total_list_dict.items(), key=lambda item: item[1], reverse=True)
    print(sorted_total_list_dict)
    result = []

    for genre, play in sorted_total_list_dict:  # '장르', '관객수'
        sorted_genre_play_list = (sorted(genre_play_list_dict[genre], key=lambda item: item[1], reverse=True))  # key = lambda item: item[1]
        # 정렬할 때 key로는 item내 첫 번째 인자 -> 값으로 가겠다.
        for inx in range(len(sorted_genre_play_list)):
            if inx > 1:
                break
            result.append(sorted_genre_play_list[inx][0])

    return result

print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!
