// H-Index
/*
<개념 참고 링크>
  - [Java] 자바 배열복사하는 방법을 알아보자!  Arrays.copyOf
    : https://seeminglyjs.tistory.com/215
  - 63. (java/자바) Arrays.stream.sum() 사용해 배열에 저장된 데이터 합계 sum 및 평균값 average 구하기
    : https://kkh0977.tistory.com/69
  - Java - 배열 정렬(Sorting) (오름차순, 내림차순)
    : https://codechacha.com/ko/java-sorting-array/
 */
package sort;

import java.util.Arrays;

public class pro_42746 {
    public int solution(int[] citations) {
        int n = citations.length;
        int hMax = Arrays.stream(citations).max().getAsInt();
        int[] cnt = new int[hMax+1];
        int answer = 0;

        for (int citation: citations) {
            cnt[citation] += 1;
        }
        int gtHnum; // numbers of greater than h
        for (int h = 1; h < hMax+1; h++ ) {
            gtHnum = Arrays.stream(Arrays.copyOfRange(cnt, h, hMax+1)).sum();
            if (n - gtHnum <= h && gtHnum >= h) {
                answer = h;
            }
        }

        return answer;
    }
}


// 다른 사람 풀이
/*
* 원소 값은 점점 감소하고, 원소 값 이상인 것의 개수는 점점 감소하므로
* 이 두 값의 최소값의 변화가 증가하다가 감소하는 지점을 찾는다...
* */
/*

import java.util.Arrays;

public class pro_42746 {
    public int solution(int[] citations) {
        Arrays.sort(citations);
        int answer = 0;
        int min;

        for (int i = citations.length - 1; i > -1; i--) {
            min = Math.min(citations[i], citations.length - i);
            if (answer < min) {
                answer = min;
            }
        }

        return answer;
    }
}
*/
