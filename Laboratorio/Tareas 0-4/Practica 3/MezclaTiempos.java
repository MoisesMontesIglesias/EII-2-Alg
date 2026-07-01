package p3;

import p2.Vector;
public class MezclaTiempos {
	static int []v;

	public static void main (String arg [])
	{
	long t1,t2;
	String opcion=arg[0];

		
	for (int n= 31250; n<=1000000000; n*= 2)
	{
		v=new int [n];
		int [] tempArray = new int[v.length];
	   	if (opcion.compareTo("ordenado")==0)
			Vector.ordenDirecto(v);
	   	else if (opcion.compareTo("inverso")==0)
			Vector.ordenInverso(v);
	   	else
			Vector.ordenAleatorio(v);
			
	  	t1 = System.currentTimeMillis();
		
		Mezcla.MergeSort(v, tempArray, 0, v.length - 1);
	         
		t2 = System.currentTimeMillis();

	  	System.out.println (n+"\t"+(t2-t1));
	}
	}
	}