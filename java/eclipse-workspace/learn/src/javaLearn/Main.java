package javaLearn;

import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.print("Hello");
		System.out.println("World");
		
		//圆面积与周长
		final double PI = 3.1415926;
		double r,s,p;
		System.out.print("r=");
		r = input.nextDouble();
		s = PI*r*r;
		p = PI*r*2;
		System.out.println("s="+s+"\np="+p);
	}
}
