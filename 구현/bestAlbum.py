# 베스트 앨범
def solution(genres, plays):
    answer = []
    genre_play = list(zip(genres, plays))
    total_play_by_genre = dict()
    play_rank_by_genre = dict()

    for idx in range(len(genre_play)):

        genre, play = genre_play[idx]

        if genre not in total_play_by_genre:
            total_play_by_genre[genre] = play
        else:
            total_play_by_genre[genre] += play

        if genre not in play_rank_by_genre:
            play_rank_by_genre[genre] = [(idx, play)]
        else:
            play_rank_by_genre[genre].append((idx, play))
            play_rank_by_genre[genre].sort(
                reverse=True, key=lambda x: (x[1], -x[0]))

    total_play_by_genre = sorted(
        list(total_play_by_genre.items()), key=lambda x: x[1], reverse=True)

    for genre_play in total_play_by_genre:
        genre = genre_play[0]

        if len(play_rank_by_genre[genre]) >= 2:
            for i in range(2):
                answer.append(play_rank_by_genre[genre][i][0])
        else:
            for i in range(len(play_rank_by_genre[genre])):
                answer.append(play_rank_by_genre[genre][i][0])

    return answer
