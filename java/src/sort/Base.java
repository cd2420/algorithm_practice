package sort;

import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;

public class Base {

    public static int[] numsSetting() {
        Random random = new Random();
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int[] nums = new int[x];
        int[] check = new int[x];
        for (int i = 0; i < x; i ++) {
            int num = random.nextInt(x);
            while (check[num] != 0) {
                num = random.nextInt(x);
            }
            check[num] = 1;
            nums[i] = num;
        }
        return nums;
    }

    public static void show(int[] nums) {
        for(int n: nums) {
            System.out.print(n + " ");
        }
        System.out.println();
    }

    // 정렬 라이브러리 활용
    public static void sort(int[] nums) {
        Arrays.sort(nums);
    }
}
