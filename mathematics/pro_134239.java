package mathematics;

import java.util.*;

public class pro_134239 {
    static List<Integer> arr = new ArrayList<>();
    
    public double[] solution(int k, int[][] ranges) {
        // double[] answer = {};
        List<Double> answer = new ArrayList<>();
        
        collatzConjecture(k);
        double[] di = definiteIntegral();
        
        for (int[] range: ranges) {
            if (range[0] <= di.length + range[1]) {
                answer.add(Arrays.stream(Arrays.copyOfRange(di, range[0], di.length + range[1])).sum());
            }
            else  {
                // 주어진 구간의 시작점이 끝점보다 커서 유효하지 않은 경우 정적분 결과를 -1로 정의한다.
                // 위 조건을 읽지 않아서 계속 왜 맞는데 틀리냐며.. ㅠ.ㅠ
                // answer.add(Arrays.stream(Arrays.copyOfRange(di, di.length + range[1], range[0])).sum());
                answer.add(-1.0);
            }
            
        }
        
        return answer.stream().mapToDouble(i -> i).toArray();
    }
    
    // 우박 수열 구하기
    public void collatzConjecture(int k) {
        arr.add(k);
        
        while (k > 1) {
            if (k % 2 == 0) {
                k /= 2;
            }
            else {
                k *= 3;
                k += 1;
            }
            arr.add(k);
        }
    }
    
    // 모든 구간의 정적분 결과 구하기
    public double[] definiteIntegral() {
        double[] di = new double[arr.size()-1];
        
        for (int i = 0; i < arr.size()-1; i++) {
            di[i] = (arr.get(i) + arr.get(i+1)) / 2.0;
        }
        
        return di;
    }
}