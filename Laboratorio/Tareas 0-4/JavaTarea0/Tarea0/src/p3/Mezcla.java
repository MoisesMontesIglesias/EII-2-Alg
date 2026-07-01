package p3;

import java.util.Random;

import p2.Vector;

public class Mezcla {
	static int []v;
    public static void MergeSort(int[] a, int[] b, int prim, int ult) {
        if (prim < ult) {
            int mitad = (prim + ult) / 2;
            MergeSort(a, b, prim, mitad);
            MergeSort(a, b, mitad + 1, ult);
            Combinar(a, b, prim, mitad, mitad + 1, ult);
        }
    }

    public static void Combinar(int[] a, int[] b, int p1, int u1, int p2, int u2) {
        if (p1 > u1 || p2 > u2) {
            return;
        }

        for (int k = p1; k <= u2; k++) {
            b[k] = a[k];
        }

        int i1 = p1;
        int i2 = p2;
        for (int k = p1; k <= u2; k++) {
            if (i1 <= u1 && (i2 > u2 || b[i1] <= b[i2])) {
                a[k] = b[i1];
                i1++;
            } else {
                a[k] = b[i2];
                i2++;
            }
        }
    }
    
    public static int[] ordenAleatorio (int[]a)
    {
    	Random r= new Random ();
    	int n= a.length;
    	for(int i=0;i<n;i++)
       		a[i]=r.nextInt(100000);
    		// p.e valores entre 0 y 999999
    	return a;
    } 

    public static void main(String[] arg) {
    	int n=Integer.parseInt(arg[0]);  //tamanno del problema  
    	v = new int[n] ;
    	int [] tempArray = new int[v.length];
    	Vector.ordenDirecto(v);
    	System.out.println ("VECTOR A ORDENAR ES");
    	Vector.escribe(v);	
    	MergeSort(v, tempArray, 0, v.length - 1);
    	System.out.println ("VECTOR ORDENADO ES");
    	Vector.escribe (v);

    	Vector.ordenInverso(v);
    	System.out.println ("VECTOR A ORDENAR ES");
    	Vector.escribe(v);	
    	MergeSort(v, tempArray, 0, v.length - 1);
    	System.out.println ("VECTOR ORDENADO ES");
    	Vector.escribe(v);

    	Vector.ordenAleatorio(v);
    	System.out.println ("VECTOR A ORDENAR ES");
    	Vector.escribe(v);	
    	MergeSort(v, tempArray, 0, v.length - 1);
    	System.out.println ("VECTOR ORDENADO ES");
    	Vector.escribe(v);
    } // fin de main
    
}
