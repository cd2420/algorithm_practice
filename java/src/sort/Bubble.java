package sort;

import static sort.Base.numsSetting;
import static sort.Base.show;

public class Bubble {

    public static void main(String[] args) {

        int[] nums = numsSetting();

        show(nums);

        int x = nums.length;
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


}
