package sort;

// 계수정렬
public class Counting {

    public static void main(String[] args) {
        int[] nums = {7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2};
        int maxNum = 0;
        for(int n: nums) {
            if (maxNum < n) {
                maxNum = n;
            }
        }
        int[] check = new int[maxNum + 1];
        for(int n: nums) {
            check[n] += 1;
        }

        for(int i = 0; i < maxNum; i++) {
            for (int j = check[i]; j > 0; j--) {
                System.out.print(i + " ");
            }
        }
    }

}
