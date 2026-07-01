package p0;

import java.util.ArrayList;
import java.util.List;

public class JavaA1 {
	public static void main (String arg [] ){
			System.out.println("TIEMPOS DEL ALGORITMO A1");
			int repeticiones = Integer.parseInt (arg[0]);	// veces que se repite la operación
		    for (int i = 0; i < 8; i++) {
		    	long t1 = System.currentTimeMillis() / 1000L;
		    	@SuppressWarnings("unused")
				List<Integer> lPrimos=listadoPrimos(repeticiones);
		    	long t2 = System.currentTimeMillis() / 1000L;
		    	System.out.println("n= " + repeticiones + " ***" + " tiempo = " + ((int) (1000*(t2-t1))) + "milisegundos)");
		    	//System.out.println(lPrimos);
		    	repeticiones=repeticiones*2;
			}
		}
		
		private static List<Integer> listadoPrimos(int n) {
		    //calcula y devuelve todos los primos hasta n
		    List<Integer> lSal= new ArrayList<>();
		    for (int i = 2; i < n+1; i++) {
		    	if (primoA1(i)) {
		        	lSal.add(i);
		        }
		    }
		    return lSal;
		}
		    		
		private static boolean primoA1(int m) {
		//Devuelve si m es primo o no, mediante un algorirmo sencillo que etiquetamos como A1"""
		boolean p = true;
		for (int i = 2; i < m; i++) {
			if (m%i==0) {
				p = false;
			}
		}
			return p;
		}
	}
