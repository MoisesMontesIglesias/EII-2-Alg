package p5;

public class ProgDin {
	private String texto;
	private String patron;
	private boolean[][] matriz;
	
	public ProgDin(String texto, String patron) {
		this.texto = " " + texto;
		this.patron = " " + patron;
		this.matriz = new boolean [texto.length()][patron.length()];
	}
	
	public boolean dinamico(String texto, String patron) {
		int n = texto.length();
		int m = patron.length();
		matriz[0][0] = true;
		System.out.println(n);
		System.out.println(m);
		for (int i = 1; i < n; i++) {
			for (int j = 1; j < m; j++) {
				if(texto.charAt(i) == patron.charAt(j)) {
					if(matriz[i-1][j-1] == true) {
						matriz[i][j] = true;
					}
				}
				
				if(texto.charAt(j) == '?') {
					if(matriz[i-1][j-1] == true || matriz[i][j-1] == true) {
						matriz[i][j] = true;
					}
				}
				
				if(texto.charAt(j) == '*') {
					if(matriz[i-1][j-1] == true|| matriz[i][j-1]== true || matriz[i-1][j]== true) {
						matriz[i][j] = true;
					}
				}
			}
		}
		return matriz[n-1][m-1];
	}
	
	public void printMatriz(String texto, String patron) {
		System.out.print("       ");
		for (int i = 0; i <  texto.length(); i++) {
			System.out.print(texto.charAt(i));
		}
		for (int i = 0; i < texto.length(); i++) {
			for (int j = 0; j < patron.length(); j++) {
				System.out.print(matriz[i][j] + " ");
			}
			System.out.println();
		}
	}

}
