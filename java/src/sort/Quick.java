package sort;

import static sort.Base.numsSetting;
import static sort.Base.show;

// 퀵 sort
public class Quick {

    public static void main(String[] args) {
        int[] nums = numsSetting();
        int x = nums.length;

        show(nums);
        quickSort(nums, 0, x-1);
        show(nums);

    }

    private static void quickSort(int[] nums, int start, int end) {
        if (start >= end) {
            return;
        }
        int pivot = start;
        int left = start+1;
        int right = end;

        while (left <= right) {
            while (left <= end && nums[pivot] >= nums[left]) {
                left++;
            }

            while (right > start && nums[pivot] <= nums[right]) {
                right--;
            }

            int temp;
            if (left > right) {
                temp = nums[pivot];
                nums[pivot] = nums[right];
            } else {
                temp = nums[left];
                nums[left] = nums[right];
            }
            nums[right] = temp;

        }
        quickSort(nums, start, right-1);
        quickSort(nums, right+1, end);

    }
}
