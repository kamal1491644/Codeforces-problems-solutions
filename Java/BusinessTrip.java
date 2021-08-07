package Problems;
import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class BusinessTrip {
	static int [] reverse(int a[], int n)
    {
        int[] b = new int[n];
        int j = n;
        for (int i = 0; i < n; i++) {
            b[j - 1] = a[i];
            j = j - 1;
        }
 

        return b;
    }
	public static void main(String[] args) {
		int sum=0;
		int counter=0;
		int k;
		int[] months=new int [12];
		Scanner s =new Scanner(System.in);
		k=s.nextInt();
		for(int i=0;i<months.length;i++) {
			months[i]=s.nextInt();
		}
		
		Arrays.sort(months);
	
		System.out.println(" ");
		months=reverse(months,12);
		
		for (int i=0;i<months.length;i++) {
			if (sum>=k) {
				break;
			}else {
				sum+=months[i];
				counter+=1;
			}
		}
		
		if (sum<k) {
			System.out.println(-1);
		}else {
			System.out.println(counter);	
		}
		
		
		

		
		

	}

}
