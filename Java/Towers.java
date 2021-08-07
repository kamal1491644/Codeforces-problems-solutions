package Problems;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;
public class Towers {
	static int countDistinct(int arr[], int n)
	{
	    int res = 1;
	    // Pick all elements one by one
	    for (int i = 1; i < n; i++)
	    {
	        int j = 0;
	        for (j = 0; j < i; j++)
	            if (arr[i] == arr[j])
	                break;
	        if (i == j)
	            res++;
	    }
	    return res;
	}
	
	
	static int largest(int[]arr)
    {
        int i;
          
        // Initialize maximum element
        int max = arr[0];
       
        // Traverse array elements from second and
        // compare every element with current max  
        for (i = 1; i < arr.length; i++)
            if (arr[i] > max)
                max = arr[i];
       
        return max;
    }
	public static int[] countFreq(int arr[], int n) 
	{
	    boolean visited[] = new boolean[n];
	    int []count=new int[n];
	    Arrays.fill(visited, false);
	 
	    for (int i = 0; i < n; i++) {

	        if (visited[i] == true)
	            continue;
	 
	        // Count frequency
	        int c = 1;
	        for (int j = i + 1; j < n; j++) {
	            if (arr[i] == arr[j]) {
	                visited[j] = true;
	                c++;
	            }
	        }
	        if (c==1) {
	        	continue;
	        }else {
	        	count[i]=c;
	        }
	    }
	    return count;
	}
	
	public static void main(String[] args) {
		int numberOfBars;
		int Distinct;
		int counter=0;
		ArrayList<Integer> tempArray = new ArrayList<>();
		Scanner s=new Scanner(System.in);
		numberOfBars=s.nextInt();
		int [] bars=new int[numberOfBars];
		
		for (int i=0;i<bars.length;i++) {
			bars[i]=s.nextInt();
		}
		Arrays.sort(bars);
		int []count=countFreq(bars,bars.length);	
		int finalTowerLength=largest(count);
		if (finalTowerLength==0) {
			finalTowerLength+=1;
		}
		Distinct=countDistinct(bars,numberOfBars);
		System.out.println(finalTowerLength+" "+Distinct);	
	}
}
