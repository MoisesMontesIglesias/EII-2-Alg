package p5;

import java.io.*;
import java.util.*;

public abstract class FileUtil {

	public static void loadFile(String nombreFicheroEntrada, List<String> textoPatron) {

		String linea;
		String texto = null;
		String patron = null;

		try {
			BufferedReader fichero = new BufferedReader(new FileReader(nombreFicheroEntrada));
			while (fichero.ready()) {
				linea = fichero.readLine();
				String [] nuevaLinea = linea.split(" ");
				textoPatron.add(nuevaLinea[0]);
				textoPatron.add(nuevaLinea[1]);
			}
			fichero.close();
		} catch (FileNotFoundException fnfe) {
			System.out.println("El archivo no se ha encontrado.");
		} catch (IOException ioe) {
			new RuntimeException("Error de entrada/salida.");
		}
	}

	public static void saveToFile(String nombreFicheroSalida, String txPedido) {
		try {
			BufferedWriter fichero = new BufferedWriter(new FileWriter("files/" + nombreFicheroSalida + ".dat"));
			fichero.write(txPedido);
			fichero.close();
		}

		catch (FileNotFoundException fnfe) {
			System.out.println("El archivo no se ha podido guardar");
		} catch (IOException ioe) {
			new RuntimeException("Error de entrada/salida");
		}
	}
}
