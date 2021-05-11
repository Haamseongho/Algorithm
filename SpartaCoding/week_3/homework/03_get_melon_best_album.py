genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


# 장르 별로 곡의 정보(인덱스, 재생횟수) 배열로 묶어 저장한다.
def get_melon_best_album(genre_array, play_array):
    # 구현해보세요!
    # 우선 같은 장르끼리 먼저 횟수를 다 더한다
    # 장르별로 순서를 Sort한다
    # 가장 많이 듣는 장르 순으로 나열하되, 장르 내에서도 가장 많이 듣는 곡부터 해서
    # 나열하도록 진행한다.
    # 우선 장르를 키로하여 리스트에 넣는다
    genre_total_play_dict = {}
    genre_index_play_array_dict = {}

    n = len(genre_array)
    for i in range(n):
        genre = genre_array[i]
        play = play_array[i]
        if genre not in genre_total_play_dict:
            genre_total_play_dict[genre] = play
            genre_index_play_array_dict[genre] = [[i, play]]
        else:
            genre_total_play_dict[genre] += play
            genre_index_play_array_dict[genre].append([i, play]) # 이미 인덱스와 재생횟수 배열을 품고 있다는 것이므로
            # append로 추가만 할 것

    print(genre_total_play_dict)
    print(genre_index_play_array_dict)
    # dictionary 내 값을 가지고 비교해서 큰 값의 key를 뽑아내는 방법
    dict.items(genre_total_play_dict)
    print(genre_total_play_dict)
    sorted_genre_play_array = sorted(genre_index_play_array_dict.items(), key=lambda item:item[1], reverse=True)
    result = []

    return


print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!
