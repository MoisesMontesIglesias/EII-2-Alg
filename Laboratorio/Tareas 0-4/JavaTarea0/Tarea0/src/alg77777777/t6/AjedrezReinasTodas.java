// PROBLEMA 3: LAS n REINAS
// CALCULA TODAS LAS FORMAS DE COLOCAR LAS REINAS
// EN EL TABLERO  DE AJEDREZ ( TODAS LAS SOLUCIONES )

package alg77777777.t6;

public class AjedrezReinasTodas

{

	static int n;
	static int[]sol;  //indica nº fila en que se coloca una reina 
	static boolean[]a;//indica si se puede colocar una reina en la fila i
	static boolean[]b;//indica si se puede colocar una reina en la diagonal i+j
	static boolean[]c;//indica si se puede colocar una reina en la diagonal i-j+n-1
	static int cont=0;//soluciones encontradas

	public static void main (String arg[])
	{
		n=Integer.parseInt(arg[0]);

		sol = new int [n];

		a= new boolean [n];
		for (int i=0;i<n;i++) a[i]=true;

		b= new boolean [2*n-1];
		for (int i=0;i<2*n-2;i++) b[i]=true;

		c= new boolean [2*n-1];
		for (int i=0;i<2*n-2;i++) c[i]=true;

		cont=0;

		backtracking (0);

		System.out.println ("NUMERO DE SOLUCIONES = "+cont);
	}

	static void backtracking (int j)
	{
		if (j==n)  // ya  están colocadas las n reinas 
		{
			cont ++;
			System.out.println("SOLUCION ENCONTRADA NUMERO "+cont);
			for (int k=0;k<n;k++) 
				System.out.println("COLUNNA "+k+"  ***  FILA "+sol[k]);
			System.out.println ();
		}

		else
			for (int i=0;i<n;i++)
				if (a[i] && b[i+j] && c[i-j+n-1])
				{
					sol[j] =i;
					a[i]=false;
					b[i+j]=false;
					c[i-j+n-1]=false;

					backtracking (j+1);

					a[i]=true;
					b[i+j]=true;
					c[i-j+n-1]=true;
				}
	}

} 
