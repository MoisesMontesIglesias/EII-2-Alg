package p2;

public class RapidoInsercionTiempos {
	static int []v;

	public static void main (String arg [])
	{
	long t1,t2;
	int k= Integer.parseInt(arg[0]);
	int n = 16000000;
	
	v=new int [n];
	Vector.ordenAleatorio(v);	
	
	t1 = System.currentTimeMillis(); 	
	RapidoInsercion.rapidoInsercion(v, k);  
	t2 = System.currentTimeMillis();
	
	System.out.println (n+"\t"+(t2-t1));
	}
}
