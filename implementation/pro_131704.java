// 택배상자
/*
<오답 노트>
  * 생각을 잘못해서 main을 매 턴마다 ++ 시켜줘야한다고 생각했었음.
  * 위와 같이 하면, sub 컨테이너에서 pop할 때도 main++이 돼서,
    검사하지도 않고 다음으로 넘어가 버린다.
  * 테스트 케이스 제발 잘 생각하자..! 나에게 제일 부족한 부분.
 */

package implementation;

import java.util.*;

public class pro_131704 {
    Deque<Integer> sub = new ArrayDeque<>();
    int main;
    int i = 0;
    
    public int solution(int[] order) {
        while (main < order.length+1 && i < order.length) {
            if (order[i] > main) {
                sub.push(main);
                main++;
            }
            else if (order[i] == main) {
                i++;
                main++;
            }
            else {
                if (order[i] != sub.peek()) {
                    break;
                }
                i++;
                sub.pop();
            }
        }
        
        // sub 컨베이어 벨트에 남아있는 상자 처리
        while (!sub.isEmpty() && i < order.length) {
            if (order[i] != sub.peek()) {
                break;
            }
            i++;
            sub.pop();
        }

        return i;
    }
}
