package backtracking;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Backtracking {

	private String[][] matriz;
	private int huecos;
	private int iHueco;//Fila en la que hay un hueco
	private int jHueco;//Columna en la que hay un hueco
	
	public Backtracking(String fichero) {
		huecos = 0;
		iHueco = -1;
		jHueco = -1;
		matriz = leerFichero(fichero);
		backtracking();
		//imprimirSolucion(matriz);
	}
	
	public String[][] leerFichero(String fichero) {
		try {
            BufferedReader reader = new BufferedReader(new FileReader(fichero));
            String linea = reader.readLine().strip();
            int size = Integer.parseInt(linea);
            String[][] matriz = new String[size * 2 + 1][size * 2 + 1];
            String[] partes;
            for(int i = 0; (linea = reader.readLine()) != null; i++) {
                partes = linea.split(" ");
                if(i % 2 == 0 && i != size * 2) {
	                for(int j = 0; j < partes.length; j++) {
	                	matriz[i][j] = partes[j];
	                	if(matriz[i][j].equals("?")) huecos++;
	                }
                } else {
                	for(int j = 0; j < partes.length * 2; j += 2) {
                		matriz[i][j] = partes[j / 2];
                	}
                }
            }
            reader.close();
            System.out.println(matriz);
            return matriz;
        } catch (IOException e) {
            e.printStackTrace();
        }
		return null;
	}
	
	public void backtracking() {
		if(!checkCaminoValido()) return; //Si el camino no es valido, abandona
		if(huecos == 0) { //Si la solución se encontró
			imprimirSolucion(matriz);
			return;
		}
		int i = iHueco;
		int j = jHueco;
		huecos--;
		for(int v = 0; v < 10; v++) {
			matriz[i][j] = String.valueOf(v);
			backtracking();
		}
		huecos++;
		matriz[i][j] = "?";
	}
	
	public boolean checkCaminoValido() {
		//Comprobamos si las filas son validas
		int total;
		String op;
		int n;
		for(int i = 0; i < matriz.length - 2; i += 2) {
			for(int j = 0; j < matriz[0].length - 2; j += 2) {
				if(matriz[i][j].equals("?")) {
					iHueco = i;
					jHueco = j;
					return true; //El camino es valido pero esta sin completar
				}
			}
			total = Integer.parseInt(matriz[i][0]);
			for(int j = 1; j < matriz[0].length - 2; j += 2) {
				op = matriz[i][j];
				n = Integer.parseInt(matriz[i][j + 1]);
				if(op.equals("+")) total += n;
				else if(op.equals("-")) total -= n;
				else if(op.equals("*")) total *= n;
				else if(op.equals("/") && n != 0) total /= n;
				else return false; //Devuelve falso al hacer una division por cero
			}
			if(total != Integer.parseInt(matriz[i][matriz[0].length - 1])) {
				return false;
			}
		}
		iHueco = -1; //Si llega hasta aqui es que no hay fila o columna con incognitas
		jHueco = -1;
		
		//Comprobamos si las columnas son validas
		for(int j = 0; j < matriz.length - 2; j += 2) {
			total = Integer.parseInt(matriz[0][j]);
			for(int i = 1; i < matriz[0].length - 2; i += 2) {
				op = matriz[i][j];
				if(op == null) return false;
				n = Integer.parseInt(matriz[i + 1][j]);
				if(op.equals("+")) total += n;
				else if(op.equals("-")) total -= n;
				else if(op.equals("*")) total *= n;
				else if(op.equals("/") && n != 0 && total % n == 0) total /= n;
				else return false;// Devuelve falso al hacer una division por cero
			}
			if(total != Integer.parseInt(matriz[matriz.length - 1][j])) {
				return false;
			}
		}
		return true;
	}
	
	public void imprimirSolucion(String[][] sol) {
		System.out.println("SOLUCIÓN ENCONTRADA");
		for(int i = 0; i < sol.length; i++) {
			for(int j = 0; j < sol[i].length; j++) {
				if(sol[i][j] != null) {
					System.out.print(sol[i][j] + "\t");
				} else {
					System.out.print("\t");
				}
			}
			System.out.println();
			System.out.println();
		}
	}
}
