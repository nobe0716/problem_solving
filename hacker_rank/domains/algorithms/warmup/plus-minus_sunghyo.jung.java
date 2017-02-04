import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int arr[] = new int[n];
        int nPositive = 0;
        int nNegative = 0;
        int nZero = 0;
        for(int arr_i=0; arr_i < n; arr_i++){
            arr[arr_i] = in.nextInt();

            if(arr[arr_i] > 0) {
                ++nPositive;
            } else if(arr[arr_i] < 0) {
                ++nNegative;
            } else {
                ++nZero;
            }
        }
        System.out.printf("%f\n%f\n%f\n", (double) nPositive / n, (double) nNegative / n, (double) nZero / n);
    }
}
