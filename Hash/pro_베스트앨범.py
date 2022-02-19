# 베스트앨범
def solution(genres, plays):
    answer = []
    music = {}
    playTime = {}
    
    for i in range(len(genres)):
        if genres[i] not in music:
            music[genres[i]] = []
            playTime[genres[i]] = 0
        music[genres[i]].append(i)
        playTime[genres[i]] += plays[i]
    
    for p in sorted(playTime.items(), key=lambda x: x[1], reverse=True):
        answer.extend(sorted(music[p[0]], key=lambda x: plays[x], reverse=True)[:2])
    
    return answer