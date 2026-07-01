// PROBLEMA 5 : 
// ASIGNACIÓN n TRABAJADORES - n TAREAS
// SE CALCULAN TODOS LAS ASIGNACIONES POSIBLES, 
// PARA ASÍ SABER LA MEJOR U ÓPTIMA
// TIEMPO FACTORIAL (INTRATABLE)
/* El problema de la asignación es un problema NP,
   es decir, no hay solución polinómica */

package alg77777777.t6;

import java.util.Random;

public class Asignacion
{
	static int n;
	static int[][]w;  // matriz de costes
	static boolean [] marca;

	static int[]asig;// ir calculando la asignación
	static int coste;// su coste 

	static int[]asigMejor;// para anotar la mejor
	static int costeMejor;// coste de la mejor

	
	static void backtracking (int nivel)
	{
		if (nivel==n)  //hay ya una asignación completa 
		{
			if (coste<costeMejor)
			{
				for (int k=0;k<n;k++) 
					asigMejor[k]=asig[k];
				costeMejor=coste;
			}
		}
		else
		{ 
			for (int i=0;i<n;i++)
				if (!marca[i] && coste<costeMejor) 		
				{ 
					asig[nivel]=i;
					coste=coste+w[nivel][i];
					marca[i]=true;
					
					backtracking (nivel+1);
					
					coste=coste-w[nivel][i];
					marca[i]=false;
				}
		}  
	}
	
	public static void main (String arg[])
	{
		n= Integer.parseInt(arg[0]);

		w=new int[n][n];
		darValorCostes();

		marca=new boolean[n];
		for (int j=0;j<n;j++) marca[j]=false;

		asig=new int[n];
		asigMejor=new int[n];
		costeMejor=100000000; // infinito

		backtracking (0); // como Permutaciones

		System.out.println("LA MEJOR ASIGNACION ES:");
		for (int l=0;l<n;l++)
			System.out.print(asigMejor[l]+"*");
		System.out.println();
		System.out.println("SU COSTE ES ="+ costeMejor);
	} // fin de método main 


	static void darValorCostes()
	// aleatoriamente
	{
		Random r=new Random();
		for (int i=0;i<n;i++)
			for (int j=0;j<n;j++)
			{
				w[i][j]=r.nextInt(99)+1;
			}
		System.out.println ("LA MATRIZ DE PESOS ES:");
		for (int i=0;i<n;i++)
		{
			for (int j=0;j<n;j++)
				System.out.print(w[i][j]+"*");
			System.out.println();
		}   
	}




} // de clase
