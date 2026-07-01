// PROBLEMA 1: PERMUTACIONES DE n ELEMENTOS

package alg77777777.t6;

public class Permutaciones
{
	static int n;
	static int[]v;  // elementos a permutar
	static int[]sol;// para ir generando las permutaciones
	static boolean[]marca;// para no repetir elementos 
	static int cont=0; // cuenta permutaciones generadas

	public static void main (String arg[])
	{
		n=Integer.parseInt(arg[0]);

		v = new int [n];
		for (int i=0;i<n;i++) v[i]=i;

		marca= new boolean [n];
		for (int i=0;i<n;i++) marca[i]=false;

		sol =new int[n];

		backtracking (0);

		System.out.println ("NUMERO DE PERMUTACIONES= "+cont);
	}

	static void backtracking (int nivel)
	{
		if (nivel==n)  //hay ya una permutación completa 
		{
			for (int k=0;k<n;k++) 
				System.out.print(sol[k]+"*");
			System.out.println ();
			cont++;
		}
		else
			for (int i=0;i<n;i++)
				if (!marca[i])
				{ 
					sol[nivel] =v[i];
					marca[i]=true;
					backtracking (nivel+1);
					marca[i]=false;
				}
	}

} 
