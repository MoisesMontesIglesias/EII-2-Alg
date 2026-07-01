// PROBLEMA 4: SALTO DEL CABALLO DE AJEDREZ
// SOLO CALCULA UNA FORMA DE HACER EL RECORRIDO
// DEL TABLERO  DE AJEDREZ ( UNA SOLUCIÓN Y SALIR) 

package alg77777777.t6;

public class AjedrezCaballoUna
{
	static int n;			// tamaño tablero 
	static int[][] tab;		// tablero de ajedrez 
	static int[] hor= {1, 2, 2, 1, -1, -2, -2, -1};	// desplazamientos horizontal del caballo
	static int[] ver= {2, 1, -1, -2, -2, -1, 1, 2};	// desplazamientos vertical del caballo
	static boolean seEncontro= false;	// solución encontradas

	static void backtracking (int salto,int x,int y)
	{
		if (salto==n*n+1) // encontramos una solución
		{
			seEncontro=true;
			imprimirEstado(salto);
		}
		else
			for (int k=0; k<=7; k++)
			{
				int u= x+hor[k];
				int v= y+ver[k];

				if (!seEncontro  && u>=0 && u<=n-1 && v>=0 && v<=n-1 &&  
						tab[u][v]==0)
				{
					tab[u][v]=salto;
					/**///imprimirEstado(salto);
					backtracking (salto+1,u,v);
					if (!seEncontro)
						tab[u][v]=0;
				}
			}       
	}

	public static void main (String arg[])
	{
		n= Integer.parseInt(arg[0]);
		int salidax= Integer.parseInt(arg[1]);
		int saliday= Integer.parseInt(arg[2]);

		System.out.println("Resolución del problema salto del caballo");
		System.out.println("Tamaño tablero: "+n+" pos inicial: ("+salidax+", "+saliday+")\n");
		tab= new int [n][n];		// Crea la matriz del tablero que quedará inicializada a 0
		tab[salidax][saliday]= 1;	// posición inicial del caballo

		backtracking(2,salidax,saliday);

		if (!seEncontro)
			System.out.println ("NO HAY SOLUCION");
		else
		{
			System.out.println("Solución");
			imprimirEstado(0);
		}
	}

	/**
	 * Imprime un estado dado (puede ser intermedio)
	 * @param nivel nivel del backtracking para hacer seguimiento
	 */
	public static void imprimirEstado(int nivel) {
		System.out.println("Estado, nivel: "+nivel);
		for (int s=0;s<n;s++)
		{
			for (int t=0;t<n;t++)
				if (tab[s][t]<=9) System.out.print(" "+tab[s][t]+" ");
				else System.out.print(tab[s][t]+" ");     
			System.out.println ();
		}
		System.out.println ();
	}

} 
