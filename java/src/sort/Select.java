package sort;

import static sort.Base.numsSetting;
import static sort.Base.show;

// 선택정렬
public class Select {

    public static void main(String[] args) {
        int[] nums = numsSetting();

        show(nums);

        int x = nums.length;

        for (int i = 0; i < x; i++) {
            int tmp = i;
            for (int j = i; j < x; j++) {
                if (nums[tmp] > nums[j]) {
                    tmp = j;
                }
            }
            int temp = nums[i];
            nums[i] = nums[tmp];
            nums[tmp] = temp;
        }

        show(nums);


    }
}
