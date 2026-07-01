// PROBLEMA 8:
// CICLOS DE UN NODO DE UN GRAFO
// SE CALCULAN TODOS LOS CICLOS SIMPLES Y
// ESE NÚMERO DE CICLOS ES DE ORDEN FACTORIAL,
// POR LO QUE EL TIEMPO ES INTRATABLE
/*
Esta clase calcula por backtracking todos los ciclos simples
que hay en un grafo sobre un nodo v[origen]

Es un problema NP, es decir, no hay solución polinómica. 

A poco que crezca n, se hace intratable por ser de 
complejidad temporal factorial. 
 */

package alg77777777.t6;

import java.util.Random;


public class CicloTodos
{
	static int n;
	static String []v;
	static int[][]w;
	static int origen;
	static boolean [] marca;//para no repetir nodos, por pedirse ciclo simple
	static int[]camino;     //trayectoria del ciclo que va calculando
	static int coste;       //coste acumulado del ciclo que va calculando 
	static int longitud;    //nivel o longitud de ciclo que va calculando
	static int nsol;        //el número total de ciclos hallados hasta destino


	public static void main (String arg[])
	{
		n= Integer.parseInt(arg[0]);
		v= new String[n];
		darValorNodos();

		w=new int[n][n];
		darValorPesosAristas();

		Random r=new Random();
		origen=r.nextInt(n);
		System.out.println("EL NODO ORIGEN ES  "+v[origen]); 
		System.out.println("LOS CICLOS SOBRE ESE NODO SON:"); 

		marca=new boolean[n];
		for (int j=0;j<n;j++) marca[j]=false;

		camino =new int [n+1];
		camino[0]=origen;
		longitud=0; 
		coste=0; 
		nsol=0; 

		backtracking (origen);

		if (nsol==0) 
			System.out.println ("NO HAY NINGUN CICLO");
		else  System.out.println ("NUMERO DE CICLOS CALCULADOS="+nsol);

	} // fin de metodo main 


	static void darValorNodos()
	// Ejemplo posible generico
	{
		for (int i=0;i<n;i++)
			v[i]= "NODO"+i;

		System.out.println ("LOS NODOS SE LLAMAN ASI:");
		for (int i=0;i<n;i++)
			System.out.println(v[i]);
	}

	static void darValorPesosAristas()
	// matriz de pesos ejemplo aleatoria 
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
		if (actual==origen && longitud>0)   // es estado solución
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
				if( !marca[j] && w[actual][j]!=-1) // hijo j de actual
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

