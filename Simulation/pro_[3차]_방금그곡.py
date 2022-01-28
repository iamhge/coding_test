# [3차] 방금그곡
'''
반례 1)
"CCB" ["03:00,03:10,FOO,CCB#CCB", "04:00,04:08,BAR,ABC"] -> "FOO"
"CCB" ["03:00,03:10,FOO,CCB#CCB#", "04:00,04:08,BAR,ABC"] -> "(None)"
'''
code = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

def timeCal(a, b):
    ah, am, bh, bm = int(a[:2]), int(a[3:]), int(b[:2]), int(b[3:])
    return (60*bh + bm) - (60*ah + am)

def solution(m, musicinfos):
    answer = "(None)"
    mis = []
    
    for musicinfo in musicinfos:
        mi = musicinfo.split(',')
        i = 0
        
        runningTime = timeCal(mi[0], mi[1])
        sheetLen = len(mi[3])
        codeLen = sheetLen - mi[3].count('#')
        i = codeLen
        now = 0
        
        # 코드의 길이가 러닝타임보다 짧은 경우
        while i < runningTime:
            if mi[3][now%sheetLen+1] == '#':
                mi[3] += mi[3][now%sheetLen:now%sheetLen+2]
                now += 2
            else:
                mi[3] += mi[3][now%sheetLen]
                now += 1
            i += 1
        
        # 코드의 길이가 러닝타임보다 긴 경우
        while i > runningTime:
            if mi[3][-1] == '#':
                mi[3] = mi[3][:-2]
            else:
                mi[3] = mi[3][:-1]
            i -= 1
            
        mi.append(runningTime)
        mis.append(mi)
    
    nowRunningTime = 0
    
    for mi in mis:
        sheet = mi[3]
        # 마지막이 '#'이 아니면 mi[3]에 포함돼도 조건과 일치하지 않을 수 있다. (코드가 _#코드 일 수 잇으므로)
        # 따라서 m+'#'을 모두 없애준다
        sheet = sheet.replace(m+'#', "")
        
        if m in sheet:
            if nowRunningTime == 0:
                answer = mi[2]
                nowRunningTime = mi[4]
            else:
                if nowRunningTime < mi[4]:
                    answer = mi[2]
                    nowRunningTime = mi[4]
    return answer

# 다른 사람 풀이
'''
<풀이 방법>
  - _# 코드를 애초에 _의 소문자형태로 변환하여 찾는다.
  - 아래 코드를 사용했을 때의 장점) 
    - 마지막에 #이 붙거나 붙지 않거나를 생각하지 않아도 된다.
    - # 때문에 악보의 길이와 실제 문자열 길이가 달라지는데, 이를 생각하지 않아도 된다.
'''
'''
def shap_to_lower(s):
    s = s.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
    return s

def solution(m,musicinfos):
    answer=[0,'(None)']   # time_len, title
    m = shap_to_lower(m)
    for info in musicinfos:
        split_info = info.split(',')
        time_length = (int(split_info[1][:2])-int(split_info[0][:2]))*60+int(split_info[1][-2:])-int(split_info[0][-2:])
        title = split_info[2]
        part_notes = shap_to_lower(split_info[-1])
        full_notes = part_notes*(time_length//len(part_notes))+part_notes[:time_length%len(part_notes)]
        if m in full_notes and time_length>answer[0]:
            answer=[time_length,title]
    return answer[-1]
'''