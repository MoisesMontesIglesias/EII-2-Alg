// PROBLEMA 7:
// CAMINOS SIMPLES ENTRE DOS NODOS DIFERENTES DE UN GRAFO
// SE CALCULAN TODOS LOS CAMINOS POSIBLES 
// PARA IR CALCULANDO EL CAMINO SIMPLE PEOR (PEOR COSTE)
// NO SE PUEDE HACER PODA AL ESTAR CALCULANDO UN COSTE MÁXIMO
/*
Esta clase calcula en un grafo  el camino simple de mayor 
coste (peor) desde un nodo origen v[origen] hasta
un nodo destino v[destino] (origen<>destino).

Este es un problema NP, es decir, no hay solución polinómica.
Por ello vamos a resolverlo por backtracking, que aquí
se aplica sobre el grafo, desarrollando en profundidad el 
árbol de estados de dicho grafo. 

A poco que crezca n, se hace intratable por ser de 
complejidad temporal factorial.

Cuando se calcula el camino de peor coste no se puede hacer
la poda que se hace cuando se calcula el camino de mejor coste
 */

package alg77777777.t6;

import java.util.Random;

public class CaminoPeor
{
	static int n;
	static String []v;  // vector de n nodos
	static int[][]w;    // matriz de pesos de aristas
	static int origen;
	static int destino;
	static boolean [] marca;// para no repetir nodos (caminos simples)
	static int[]camino;  // trayectoria de camino que va calculando
	static int coste;    // coste acumulado del camino que va calculando 
	static int longitud; // nivel o longitud de camino que va calculando
	static int nsol;     // el número total de caminos hallados hasta destino

	static int []caminoPeor; // para anotar el camino peor
	static int costePeor;    // coste del camino peor
	static int longPeor;     // numero aristas del camino peor


	public static void main (String arg[])
	{
		n= Integer.parseInt(arg[0]);

		v= new String[n];
		darValorNodos();

		w=new int[n][n];
		darValorPesosAristas();

		Random r=new Random();
		do
		{
			origen=r.nextInt(n);
			destino=r.nextInt(n);
		}
		while (origen==destino);
		System.out.println("El NODO ORIGEN ES "+v[origen]);
		System.out.println("El NODO DESTINO ES "+v[destino]);

		marca=new boolean[n];
		for (int j=0;j<n;j++) marca[j]=false;
		marca [origen]=true;

		camino =new int [n];
		caminoPeor =new int [n];

		camino[0]=origen;
		longitud=0;  
		nsol=0;
		coste=0;
		costePeor=-1; // menor que cualquier posible 
		backtracking (origen);
		if (nsol==0) 
			System.out.println ("NO HAY NINGUN CAMINO");
		else
		{
			System.out.println("EL CAMINO PEOR ES:");
			for (int l=0;l<=longPeor;l++)
				System.out.print(v[caminoPeor[l]]+"**");
			System.out.println();
			System.out.println("SU COSTE PEOR ES="+costePeor);
		}
	} // fin de método main 


	static void darValorNodos()
	// un ejemplo de valores genericos a los nodos
	{
		for (int i=0;i<n;i++)
			v[i]= "NODO"+i;

		System.out.println ("LOS NODOS SE LLAMAN ASI:");
		for (int i=0;i<n;i++)
			System.out.println(v[i]);
	}

	static void darValorPesosAristas()
	// un ejempo de valores aleatorios a los pesos de las aristas
	{
		Random r=new Random();
		for (int i=0;i<n;i++)
			for (int j=0;j<n;j++)
			{
				int x=r.nextInt(10);
				if (x==0) x=-1; //no hay arista
				w[i][j]=x;
			}

		for (int i=0;i<n;i++)
			w[i][i]=-1;  // sin bucles    

		System.out.println ("LA MATRIZ DE PESOS ES:");
		for (int i=0;i<n;i++)
		{
			for (int j=0;j<n;j++)
				System.out.print(w[i][j]+"*");
			System.out.println();
		}   
	}

	static void backtracking (int actual) 
	{
		if (actual==destino)   // es estado solución
		{ 
			nsol++;
			if (coste>costePeor)
			{
				for (int l=0;l<=longitud;l++) 
					caminoPeor[l]=camino[l];
				costePeor=coste;
				longPeor=longitud;
			}
		}

		else
			for (int j=0;j<n;j++)
				if (!marca[j] && w[actual][j]!=-1)
				{
					longitud++;
					coste=coste+w[actual][j];
					marca[j]=true;
					camino[longitud]=j;
					backtracking(j);
					longitud--;
					coste=coste-w[actual][j];
					marca[j]=false;
				}
	} 

} // de clase

