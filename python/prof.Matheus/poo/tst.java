import java.util.Arrays;

public class tst {
    public static void main(String[] args) {

    }

    public static int[] twoSum(int[] nums, int target) {
        int[] somaNums = new int[2];
        for (int i = 0; i < nums.length; i++) {
            for (int j = 0; j < nums.length; j++) {
                if (i == j) {
                    continue;
                }
                int soma = nums[i] + nums[j];
                if (soma == target) {
                    somaNums[0] = i;
                    somaNums[1] = j;
                    return somaNums;
                }
            }
        }
        return somaNums;
    }
}