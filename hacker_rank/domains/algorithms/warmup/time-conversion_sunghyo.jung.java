import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;
import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String time = in.next();
        SimpleDateFormat sdf = new SimpleDateFormat("hh:mm:ssa", Locale.ENGLISH);
        SimpleDateFormat sdf2 = new SimpleDateFormat("HH:mm:ss", Locale.ENGLISH);

        Date parse;
        try {
            parse = sdf.parse(time);
            System.out.println(sdf2.format(parse));
        } catch (ParseException e) {
            e.printStackTrace();
        }
    }
}