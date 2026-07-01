package p5;

import java.util.ArrayList;
import java.util.List;

public class Main {

	public static void main(String[] arg) {
		List<String> lista = new ArrayList<String>();
		FileUtil.loadFile(arg[0], lista);
		String texto = lista.get(0);
		String patron = lista.get(1);
		ProgDin din = new ProgDin(texto, patron);
		din.printMatriz(texto, patron);
		din.dinamico(texto, patron);
		din.printMatriz(texto, patron);
	}

}
