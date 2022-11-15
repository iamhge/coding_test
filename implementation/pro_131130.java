// 혼자 놀기의 달인
/*
<풀이 방법>
  - (편의상 상자는 0부터 시작하는 것으로 생각.)
  - 한 번 그룹핑이 되면 다른 그룹과 섞이지 않는다.
  - 따라서 그룹핑이 된 상자(i)의 카드(cards[i])는 0으로 visited 표시를 한다.
* */
package implementation;

import java.util.*;

public class pro_131130 {
    public int solution(int[] cards) {
        List<Integer> scores = new ArrayList<>();
        int score = 0;
        int j, tmp;

        for (int i = 0; i < cards.length; i++) {
            j = i;
            while (cards[j] != 0) {
                score++;
                tmp = cards[j];
                cards[j] = 0;
                j = tmp-1;
            }
            if (score != 0) {
                scores.add(score);
                score = 0;
            }
        }

        if (scores.size() == 1) {
            return 0;
        }

        scores.sort(Collections.reverseOrder());

        return scores.get(0)*scores.get(1);
    }
}
