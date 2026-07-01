package p11;

import java.util.Random;

public class Vector6 {
	static int []v;
	static int []w;

	public static void main (String arg [] )
	{
		int repeticiones = Integer.parseInt (arg[0]);	// veces que se repite la operación
		long t1,t2;

		System.out.println("repeticiones = "+ repeticiones);
		System.out.println ("Tamaño\tTiempo");   
		for ( int n= 10000; n<= 81920000; n*=2) // n se va duplicando   
		{
			v = new int [n] ;
			w = new int[n];
			Vector1.rellena (v);
			Vector1.rellena(w);
			t1=System.currentTimeMillis();

			// hay que repetir todo el proceso a medir (lo que que estaba entre t1 y t2) 
			for (int r= 1; r<=repeticiones; r++)
			{  	
				Vector1.coincidencias1 (v,w);
			}

			t2=System.currentTimeMillis();
			System.out.println (n+"\t"+(t2-t1));   

		} // fin de for
			
		System.out.println("\nFin de la medición de tiempos *****");

	} // fin de main
	/** Este mÃ©todo da valores aleatorios a un vector de enteros, 
    utiliza para ello la clase Random del paquete java.util  
 **/
public static void rellena (int[]a)
{
	Random r= new Random ();
	int n= a.length;
	for(int i=0;i<n;i++)
		a[i]=r.nextInt (199)-99;//valores entre -99 y 99

}  // fin de rellena   


/** Escribe el contenido del vector que se le pasa  
**/
public static void escribe (int[]a)
{
	int n= a.length;
	for (int i=0; i<n; i++ )
		System.out.println ("Elemento "+i+" = "+a[i]);
	System.out.println();

}
public static int coincidencias1 (int[]a,int[]b)
{
	int c=0;
	int n= a.length;
	for (int i=0;i<n;i++)
	    for (int j=0;j<n;j++)
               if (i==j && a[i]==b[j])
             c++;
        return c;
}  // fin de coincidencias1

}
