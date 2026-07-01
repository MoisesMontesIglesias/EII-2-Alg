// PROBLEMA 5 : 
// ASIGNACIÓN n TRABAJADORES - n TAREAS
// CÁLCULO DE TIEMPOS:SE PODA PARA BAJAR TIEMPOS

package alg77777777.t6;

import java.util.Random;

public class AsignacionTiempos
{
	static int n;
	static int[][]w;
	static boolean [] marca;

	static int[]asig;// ir calculando la asignación
	static int coste;// su coste 

	static int[]asigMejor;// para anotar la mejor
	static int costeMejor;// coste de la mejor


	public static void main (String arg[])
	{
		long t1,t2;

		for (int tam=6;tam<=30;tam++)
		{
			n=tam; 
			w=new int[n][n];
			darValorCostes();

			marca=new boolean[n];
			for (int j=0;j<n;j++) marca[j]=false;

			asig=new int[n];
			asigMejor=new int[n];
			costeMejor=100000000; // infinito
			t1=System.currentTimeMillis();
			backtrackingPoda(0); 
			t2=System.currentTimeMillis();
			System.out.println ("n="+n+"**TIEMPOPODA="+(t2-t1));
		}
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
	}

	static void backtrackingPoda (int nivel)
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
		{ for (int j=0;j<n;j++)
			if (!marca[j]
					&& coste<costeMejor) //PODA LÓGICA
			{ 
				asig[nivel]=j;
				coste=coste+w[nivel][j];
				marca[j]=true;
				backtrackingPoda (nivel+1);
				coste=coste-w[nivel][j];
				marca[j]=false;
			}
		}  
	}
} // de clase

