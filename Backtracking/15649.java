import java.util.*;
public class Main {
	private static int n,m;
	private static int[] arr = new int[9];
	private static boolean [] isused = new boolean [9];
	
	
	public static void refunc(int k) {
		if(k==m) {
			for(int i=0; i<m;i++) {
				System.out.print(arr[i]+" ");
			}
			System.out.println();
			return;
		}
		for(int i=1;i<=n;i++) {
			if(!isused[i]) {
				arr[k] = i;
				isused[i] = true;
				refunc(k+1);
				isused[i] = false;
			}
		}
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		m = sc.nextInt();
		refunc(0);
	}
}
