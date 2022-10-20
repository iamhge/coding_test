// 올바른 괄호
// 이것도 시간초과나긴 함..
package Stack_Queue;

public class pro_12909 {
    boolean solution(String s) {
        String[] strArr = s.split("");
        int open = 0;

        for (String str : strArr) {
            if (str.equals("(")) {
                open += 1;
            }
            else {
                open -= 1;
            }
            if (open < 0) {
                return false;
            }
        }
        return open == 0;
    }
}

// 시간 초과
/*
import java.util.ArrayDeque;
import java.util.Deque;

public class pro_12909 {
    boolean solution(String s) {
        if (s.length() % 2 != 0) {
            return false;
        }
        String[] strArr = s.split("");
        Deque<String> stack = new ArrayDeque<>();

        for (String str : strArr) {
            if (str.equals("(")) {
                stack.push(str);
            }
            else {
                if (stack.size() == 0) {
                    return false;
                }
                stack.pop();
            }
        }
        if (stack.size() != 0) {
            return false;
        }
        return true;
    }
}

* */