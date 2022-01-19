# 스킬트리
def solution(skill, skill_trees):
    answer = len(skill_trees)
    
    turn = 0
    for skill_tree in skill_trees:
        for st in skill_tree:
            if st in skill:
                if st == skill[turn]:
                    turn += 1
                else:
                    answer -= 1
                    break
        turn = 0
    
    return answer