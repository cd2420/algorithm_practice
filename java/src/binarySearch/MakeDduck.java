package binarySearch;

import java.util.Scanner;

// 떡볶이 떡 만들기
public class MakeDduck {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        int[] dducks = new int[n];
        for (int i = 0; i < n; i++) {
            dducks[i] = sc.nextInt();
        }

        int result = 0;
        int start = 0;
        int end = (int) 1e9;
        while (start <= end) {
            int mid = (start + end) / 2;
            int cnt = 0;
            for (int i = 0; i < n; i++) {
                if (mid <= dducks[i]) {
                    cnt += dducks[i] - mid;
                }
            }

            if (cnt < m) {
                end = mid - 1;
            } else {
                result = mid;
                start = mid + 1;
            }
        }

        System.out.println(result);

    }
}
