// PROBLEMA 7:
// CAMINOS SIMPLES ENTRE DOS NODOS DIFERENTES DE UN GRAFO

// SE CALCULAN TODOS LOS CAMINOS POSIBLES Y
// ESE NÚMERO DE CAMINOS ES DE ORDEN FACTORIAL,
// POR LO QUE EL TIEMPO ES INTRATABLE
/*
Esta clase calcula por backtracking todos los caminos simples
que hay en un grafo desde un nodo origen v[origen] hasta
un nodo destino v[destino] (origen<>destino).

Este es un problema NP, es decir, no hay solución polinómica.
Por ello vamos a resolverlo por backtracking, que aquí
se aplica sobre el grafo, desarrollando en profundidad el 
árbol de estados de dicho grafo. 
 */

package alg77777777.t6;

import java.util.Random;

public class CaminoTodos
{
	static int n;       // numero de nodos 
	static String []v;  // vector de n nodos
	static int[][]w;    // matriz de pesos de aristas
	static int origen;
	static int destino;
	static boolean [] marca;// para no repetir nodos (caminos simples)
	static int[]camino;  // trayectoria de camino que va calculando
	static int coste;    // coste acumulado del camino que va calculando 
	static int longitud; // nivel o longitud de camino que va calculando
	static int nsol;     // el número total de caminos hallados hasta destino


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
		System.out.println("LOS CAMINOS SON:");

		marca=new boolean[n];
		for (int j=0;j<n;j++) marca[j]=false;
		marca [origen]=true;

		camino =new int [n];
		camino[0]=origen;
		longitud=0;  
		nsol=0; 
		coste=0;

		backtracking (origen);

		if (nsol==0) 
			System.out.println ("NO HAY NINGUN CAMINO");
		else  System.out.println ("NUMERO DE CAMINOS CALCULADOS="+nsol);

	} // fin de método main 


	static void darValorNodos()
	// un ejemplo de valores genéricos a los nodos
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


	static void backtracking (int actual)  // es recursivo
	{
		if (actual==destino)   // es estado solución
		{ 
			nsol++;
			for (int l=0;l<=longitud;l++) 
				System.out.print(v[camino[l]]+"*");
			System.out.println();
			System.out.println("SU COSTE ES="+coste);
			System.out.println();
		}
		else
			for (int j=0;j<n;j++)
				if (!marca[j] && w[actual][j]!=-1) // hijo j deactual
				{
					longitud++;
					coste=coste+w[actual][j];
					marca[j]=true;
					camino[longitud]=j;
					backtracking(j);  // llamada sobre el hijo j
					longitud--;
					coste=coste-w[actual][j];
					marca[j]=false;
				}
	}  // fin de backtracking

} // de clase

