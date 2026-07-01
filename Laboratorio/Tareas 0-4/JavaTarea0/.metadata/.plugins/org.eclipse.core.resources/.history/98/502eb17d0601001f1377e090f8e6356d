// PROBLEMA 1: PERMUTACIONES DE n ELEMENTOS
// MEDICION DE TIEMPOS: COMPORTAMIENTO FACTORIAL
/* este programa calcula tiempos de generar las
   permutaciones de n elementos.
   El tiempo es factorial, esto es, intratable */

package alg77777777.t6;

public class PermutacionesTiempos
{
	static int n;
	static int[]v;
	static int[]sol;
	static boolean[]marca; 
	static int cont=0;

	public static void main (String arg[])
	{
		long t1,t2;
		for (int dim=5;dim<=30;dim++)
		{
			n=dim;
			v = new int [n];
			for (int i=0;i<n;i++) v[i]=i;

			marca= new boolean [n];
			for (int i=0;i<n;i++) marca[i]=false;

			sol=new int[n];

			t1=System.currentTimeMillis();
			backtracking (0);
			t2=System.currentTimeMillis();
			System.out.println ("NUMERO="+n+" **TIEMPO="+(t2-t1));
		}
	}

	static void backtracking (int nivel)
	{
		if (nivel==n)  //hay ya una permutación completa 
		{
			//for (int k=0;k<n;k++) 
			//  System.out.print(sol[k]+"*");
			//System.out.println ();
			cont++;
		}
		else
			for (int j=0;j<n;j++)
				if (!marca[j])
				{ 
					sol[nivel] =v[j];
					marca[j]=true;
					backtracking (nivel+1);
					marca[j]=false;
				}
	}
} 
