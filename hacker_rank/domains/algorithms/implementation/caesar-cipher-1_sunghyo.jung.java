import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        String s = in.next();
        int k = in.nextInt();
        char[] r = new char[s.length()];
        for(int i = 0 ; i < n ; ++i) {
            char charAt = s.charAt(i);
            if('A' <= charAt && charAt <= 'Z') {
                int val = ((charAt - 'A' + k) % 26) + 'A';
                charAt = (char)val;
            } else if('a' <= charAt && charAt <= 'z') {
                int val = ((charAt - 'a' + k) % 26) + 'a';
                charAt = (char)val;
            }
            r[i] = charAt;
            System.out.print(r[i]);
        }
        System.out.println();
    }
}
