
import java.util.Scanner;

public class CalculationCircles {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        //计算圆面积与周长
        final double PI = 3.1415926;
        double r,s,p;
        System.out.print("r=");
        r = input.nextDouble();
        s = PI*r*r;
        p = PI*r*2;
        System.out.println("s="+s+"\np="+p);
    }
}

//