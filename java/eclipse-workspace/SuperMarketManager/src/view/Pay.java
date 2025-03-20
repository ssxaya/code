package view;
import java.util.Scanner;

public class Pay {
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		
		final double DI =0.8;
		
		System.out.println("请输入衬衣的价格:");
		double shirtPrice = s.nextDouble();
		System.out.println("请输入衬衣的数量：");
		int shirtNu = s.nextInt();
		System.out.println("请输入运动鞋的价格：");
		double shoePrice = s.nextDouble();
		System.out.println("请输入运动鞋的数量");
		int shoeNu = s.nextInt();
		
		// 计算
		double finalPay = DI * (shirtPrice * shirtNu + shoePrice * shoeNu);
		// 自适应付款（人机？）
		double payMoney = ((int)(finalPay/100)+1)*100;
		double returnMoney = payMoney - finalPay;
		int score = (int)(finalPay/100*3);
		
		// 输出
		System.out.println("\n\n***********消费清单***********\n");
		System.out.println("购买物品\t单价\t数量");
		System.out.println("衬衣\t￥"+shirtPrice + "\t" +shirtNu);
		System.out.println("运动鞋\t￥"+shoePrice + "\t" +shoeNu);
		System.out.println("折扣\t"+DI);
		System.out.println("金额总计:\t￥"+(double)Math.round(finalPay*100/100));
		System.out.println("实付余额:\t￥"+(double)Math.round(payMoney*100/100));
		System.out.println("找钱:\t\t￥"+(double)Math.round(returnMoney*100/100));
		System.out.println("购物积分:"+score);
		System.out.println("\n*****************************");



	}
}
