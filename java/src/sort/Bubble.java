package sort;

import java.util.Random;
import java.util.Scanner;

public class Bubble {

    public static void main(String[] args) {
        Random random = new Random();
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int[] nums = new int[x];
        int[] check = new int[50];
        for (int i = 0; i < x; i ++) {
            int num = random.nextInt(50);
            while (check[num] != 0) {
                num = random.nextInt(50);
            }
            check[num] = 1;
            nums[i] = num;
        }
        show(nums);

        for (int i = 0; i < x; i++) {
            for (int j = i+1; j < x; j++) {
                if (nums[i] > nums[j]) {
                    int tmp = nums[j];
                    nums[j] = nums[i];
                    nums[i] = tmp;
                }
            }
        }

        show(nums);
    }

    private static void show(int[] nums) {
        for(int n: nums) {
            System.out.print(n);
            System.out.print(" ");
        }
        System.out.println();
    }
}
