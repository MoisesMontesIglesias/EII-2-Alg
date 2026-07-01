package p12;

public class Bucle5 {

	public static long bucle5(int n)
	{
		long cont = 0;
		long  n1=n;
	        do
	         {
	           for (long i=1;i<=n;i++)
	        	   for (long k = 1; k <= n; k*=3)
		              for (long j=n;j>=0;j-=2)
		               	cont++;
		   n1=n1/3;
	         }        
	         while (n1>=1);        

	        return cont;

	}

	public static void main(String arg[]) 
	{
		long c = 0;
		long t1, t2;

		int nVeces = Integer.parseInt(arg[0]);

		System.out.println("n\ttiempo\trepeticiones\tcontador");

		for (int n = 100; n <= 819200; n *= 2) 
		{
		t1 = System.currentTimeMillis();

		for (int repeticiones = 1; repeticiones <= nVeces; repeticiones++) 
			c = bucle5(n);
				

		t2 = System.currentTimeMillis();

		System.out.println(n+"\t"+(t2-t1)+"\t"+nVeces+"\t\t"+c);		

		} // for

	} // main

	} // clase