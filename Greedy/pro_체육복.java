import java.util.Arrays;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = n;
        // 뒷번호 친구 검사해야하므로 (n+1) + 1
        int[] reserveFlag = new int[n+2];

        for (int r: reserve) {
            for (int l: lost) {
                if (r == l) {
                    reserveFlag[r] += 1;
                    break;
                }
            }
            reserveFlag[r] += 1;
        }
        
        Arrays.sort(lost);
        for (int l: lost) {
            // 본인 체육복 쓰는 경우
            if (reserveFlag[l] == 2) {
                reserveFlag[l] = 0;
            }
            // 앞 번호 친구에게 여벌 체육복이 있는지
            else if (reserveFlag[l-1] == 1) {
                reserveFlag[l-1] = 0;
            }
            // 뒷 번호 친구에게 여벌 체육복이 있는지
            else if (reserveFlag[l+1] == 1) {
                reserveFlag[l+1] = 0;
            }
            else {
                answer -= 1;
            }
        }
        return answer;
    }
}