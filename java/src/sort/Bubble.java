package sort;

import static sort.Base.numsSetting;
import static sort.Base.show;

public class Bubble {

    public static void main(String[] args) {

        int[] nums = numsSetting();

        show(nums);

        int x = nums.length;
        for (int i = 0; i < x; i++) {
            for (int j = 0; j < x - 1 - i; j++) {
                if (nums[j] > nums[j+1]) {
                    int tmp = nums[j];
                    nums[j] = nums[j+1];
                    nums[j+1] = tmp;
                }
            }
        }

        show(nums);
    }


}
