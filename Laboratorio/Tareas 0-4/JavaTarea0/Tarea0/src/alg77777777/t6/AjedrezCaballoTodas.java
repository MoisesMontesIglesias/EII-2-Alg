// PROBLEMA 4: SALTOS DEL CABALLO DE AJEDREZ
// CALCULA TODAS LAS FORMAS DE HACER EL RECORRIDO
// DEL TABLERO  DE AJEDREZ ( TODAS LAS SOLUCIONES)

package alg77777777.t6;


public class AjedrezCaballoTodas

{
	static int n;      // tamaño tablero 
	static int[][]tab; // tablero de ajedrez 
	static int[]a; // desplazamientos x del caballo
	static int[]b; // desplazamientos y del caballo
	static int cont=0; // soluciones encontradas


	public static void main (String arg[])
	{
		n=Integer.parseInt(arg[0]);
		int salidax= Integer.parseInt(arg[1]);
		int saliday= Integer.parseInt(arg[2]);

		tab= new int [n][n];
		for (int i=0;i<n;i++)
			for (int j=0;j<n;j++)
				tab[i][j]=0;

		tab[salidax][saliday]=1;// posición inicial del caballo

		a= new int [8];
		b= new int [8];
		a[0]=1;b[0]=2;a[1]=2;b[1]=1;a[2]=2;b[2]=-1;a[3]=1;b[3]=-2;
		a[4]=-1;b[4]=-2;a[5]=-2;b[5]=-1;a[6]=-2;b[6]=1;a[7]=-1;b[7]=2;

		cont=0;

		backtracking (2,salidax,saliday);

		System.out.println ("NUMERO DE SOLUCIONES = "+cont);
	}


	static void backtracking (int salto,int x,int y)
	{
		if (salto==n*n+1)  // ya  acabo recorrer tablero 
		{
			cont ++;
			System.out.println("SOLUCION ENCONTRADA NUMERO "+cont);
			for (int s=0;s<n;s++)
			{
				for (int t=0;t<n;t++)
					if (tab[s][t]<=9) System.out.print(" "+tab[s][t]+"*");
					else System.out.print(tab[s][t]+"*");   
				System.out.println ();
			}
		}

		else
			for (int k=0;k<=7;k++)
			{
				int u=x+a[k];
				int v=y+b[k];

				if (u>=0 && u<=n-1 && v>=0 && v<=n-1 && tab[u][v]==0)
				{
					tab[u][v]=salto;

					backtracking (salto+1,u,v);

					tab[u][v]=0;
				}
			}       
	}

} 
