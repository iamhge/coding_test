// 테트로미노
/*
<풀이 방법>
00 01 02
10 11 12
회전하면
10 00
11 01
12 02
인덱스
00 01
10 11
20 21
<개념 참고 링크>
  자바 String 배열을 int 배열로 변환
  : https://zetawiki.com/wiki/%EC%9E%90%EB%B0%94_String_%EB%B0%B0%EC%97%B4%EC%9D%84_int_%EB%B0%B0%EC%97%B4%EB%A1%9C_%EB%B3%80%ED%99%98
* */
package Simulation;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class boj_14500 {
    static int tetNum = 7;
    static int[][] tetrominoDx = {
            {0, 0, 0}, // I
            {0, 1, 0}, // O
            {0, 0, 1}, // T
            {0, 0, 1}, // J
            {1, 1, 0}, // L
            {1, 0, 1}, // S
            {0, 1, 0}, // Z
    };
    static int[][] tetrominoDy = {
            {1, 1, 1}, // I
            {1, 0, -1}, // O
            {1, 1, -1}, // T
            {1, 1, 0}, // J
            {0, 0, 1}, // L
            {0, 1, 0}, // S
            {1, 0, 1} // Z
    };

    static int[] tetrominoHeight = {1, 2, 2, 2, 3, 3, 2};
    static int[] tetrominoWidth = {4, 2, 3, 3, 2, 2, 3};

    public static int[][] rotate(int[][] paper) {
        int n = paper.length;
        int m = paper[0].length;
        int[][] rotated = new int[m][n];
        for (int i = 0; i < n; i ++) {
            for (int j = 0; j < m; j ++) {
                rotated[j][n-1-i] = paper[i][j];
            }
        }
        return rotated;
    }

    public static int getMaxi(int n, int m, int[][] paper){
        int result = 0;
        int now;
        for (int k = 0; k < tetNum; k++) {
            for (int i = 0; i <= n - tetrominoHeight[k]; i++) {

                for (int j = 0; j <= m - tetrominoWidth[k]; j++) {
                    now = 0;
                    int x = i;
                    int y = j;
                    now += paper[x][y];
                    for (int l = 0; l < 3; l++) {
                        x += tetrominoDx[k][l];
                        y += tetrominoDy[k][l];
                        now += paper[x][y];
                    }
                    if (now > result) {
                        result = now;
                    }
                }
            }
        }

        return result;
    }

    public static void main(String[] args) throws Exception {
        int answer = 0;
        int result;

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int [] input = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int [][] paper = new int[input[0]][input[1]];
        for (int i = 0; i < input[0]; i ++) {
             paper[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        }

        for (int i = 0; i < 4; i++) {
            result = getMaxi(paper.length, paper[0].length, paper);
            if (result > answer) {
                answer = result;
            }
            paper = rotate(paper);
        }

        System.out.println(answer);
    }
}
