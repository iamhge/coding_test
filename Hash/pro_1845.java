// 폰켓몬
package Hash;

import java.util.*;

public class pro_1845 {

    public int solution(int[] nums) {
        Map<Integer, Integer> phoneketmon = new HashMap<>();

        for (int num: nums) {
            phoneketmon.put(num, phoneketmon.getOrDefault(num, 0) + 1);
        }

        return Math.min(phoneketmon.size(), nums.length/2);
    }
}
