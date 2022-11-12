package sort;

import static sort.Base.numsSetting;
import static sort.Base.show;

// 삽입정렬
public class Insert {

    public static void main(String[] args) {
        int[] nums = numsSetting();

        show(nums);

        int x = nums.length;

        for (int i = 1; i < x; i++) {
            for (int j = i; j > 0; j--) {
                if (nums[j] < nums[j-1]) {
                    int tmp = nums[j-1];
                    nums[j-1] = nums[j];
                    nums[j] = tmp;
                }
            }
        }

        show(nums);


    }
}
