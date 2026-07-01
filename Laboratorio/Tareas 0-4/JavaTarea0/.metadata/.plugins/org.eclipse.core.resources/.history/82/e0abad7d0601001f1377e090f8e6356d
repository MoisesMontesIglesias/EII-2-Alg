// PROBLEMA 3: LAS n REINAS
// SOLO CALCULA UNA FORMA DE COLOCAR LAS n REINAS
// EN EL TABLERO  DE AJEDREZ n*n
// (UNA SOLUCIÓN Y SALIR) 

package alg77777777.t6;


public class AjedrezReinasUna
{

	static int n;
	static int[]sol;  //indica nº fila en que se coloca una reina 
	static boolean[]a;//indica si se puede colocar una reina en la fila i
	static boolean[]b;//indica si se puede colocar una reina en la diagonal i+j
	static boolean[]c;//indica si se puede colocar una reina en la diagonal i-j+n-1
	static boolean seEncontro; // ¿solución encontrada?

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

		seEncontro=false;

		backtracking (0);

		if (!seEncontro) System.out.println ("NO HAY SOLUCION");
	}

	static void backtracking (int j)
	{
		if (j==n)  // ya  están colocadas las n reinas 
		{
			seEncontro=true;
			System.out.println("SOLUCION ENCONTRADA");
			for (int k=0;k<n;k++) 
				System.out.println("COLUNNA "+k+" **  FILA "+sol[k]);
			System.out.println ();
		}

		else
			for (int i=0;i<n;i++)
				if (a[i] && b[i+j] && c[i-j+n-1]

						&& !seEncontro)  // CORTOCIRCUITO
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
