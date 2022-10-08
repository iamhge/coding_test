// 타겟 넘버
package Graph;

import java.util.Deque;
import java.util.ArrayDeque;

class Solution {
    public int dfs(int[] root, int target, int[] numbers) {
        int answer = 0;
        int n = numbers.length;
        
        Deque<int[]> stack = new ArrayDeque<>();
        stack.push(root);
        
        while (stack.size() > 0) {
            int[] idxRst = stack.pop();
            if (idxRst[0] >= n) {
                if (idxRst[1] == target) {
                    answer += 1;
                }
                continue;
            }
            stack.push(new int[] {idxRst[0] + 1, idxRst[1] - numbers[idxRst[0]]});
            stack.push(new int[] {idxRst[0] + 1, idxRst[1] + numbers[idxRst[0]]});
        }
        return answer;
    }
    
    public int bfs(int[] root, int target, int[] numbers) {
        int answer = 0;
        int n = numbers.length;
        
        Deque<int[]> queue = new ArrayDeque<>();
        queue.add(root);
        
        while (queue.size() > 0) {
            int[] idxRst = queue.pop();
            if (idxRst[0] >= n) {
                if (idxRst[1] == target) {
                    answer += 1;
                }
                continue;
            }
            queue.add(new int[] {idxRst[0] + 1, idxRst[1] - numbers[idxRst[0]]});
            queue.add(new int[] {idxRst[0] + 1, idxRst[1] + numbers[idxRst[0]]});
        }
        return answer;
    }
    
    public int solution(int[] numbers, int target) {
        // return dfs(new int[2], target, numbers);
        return bfs(new int[2], target, numbers);
    }
}