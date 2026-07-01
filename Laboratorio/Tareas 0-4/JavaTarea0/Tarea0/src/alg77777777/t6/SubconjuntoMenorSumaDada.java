// PROBLEMA 2: SUBCONJUNTOS DE UNA SUMA DADA
// CALCULA TODOS LOS SUBCONJUNTOS QUE SUMEN c

package alg77777777.t6;

public class SubconjuntoMenorSumaDada
{
	static int n;			// número de elementos en el conjunto de partida
	static int sumaDada;	// valor de la suma
	
	static int[]v;			//n números positivos diferentes      
	static boolean[]marca;	// marca True si se elige un elemento
	static int sumaParcial;	// suma parcial acumulada hasta un estado 
	private static int numEle;	// número de elemtos del subconjunto
	static int contSol;		// número soluciones
	private static int numEleSol;	// número de elementos de la solución encontrada hasta el momento


	public static void main (String arg[])
	{
		// lee en línea de comandos los dos parámetros de entrada
//		n= Integer.parseInt(arg[0]);	// números del conjunto de partida
//		sumaDada= Integer.parseInt(arg[1]); 	// suma buscada
		n= 100;
		sumaDada= 370;

		v = new int [n];		// espacio para guardar el estado
		marca= new boolean [n];	// para comprobar que los elementos se utilizan en el subconjunto

		// ejemplo 1 utilizando los n primeros números naturales empezando en 1
		System.out.println("Conjunto formado por los n primeros números naturales (empezando en 1)");
		supuesto1(v);
		inicilizarEstado();
		// método backtracking
		backtracking (0);
		System.out.println ("Número de subconjuntos encontrados= "+contSol);
		System.out.println();

		// ejemplo 2 utilizando los n primeros cuadrados naturales (empezando en 1
		System.out.println("Conjunto formado por los n primeros cuadrados naturales (empezando en 1)");
		supuesto2(v);
		inicilizarEstado();  
		// método backtracking
		backtracking (0);
		System.out.println ("Número de subconjuntos encontrados= "+contSol);

	}

	/**
	 * Inicializa variables de estado para el backtracking: marca, cont, s
	 */
	private static void inicilizarEstado() {
		for (int i=0;i<n;i++) 
			marca[i]=false;
		numEle= 0;
		numEleSol= n;
		contSol=0;
		sumaParcial=0;
	}

	/**
	 * un ejemplo: los n primeros naturales, empezando en 1
	 * @param v
	 */
	static void supuesto1(int[]v)
	{
		for (int i=0;i<n;i++) 
			v[i]=i+1;
	}

	/**
	 * otro ejemplo:los primeros cuadrados
	 * @param v
	 */
	static void supuesto2(int[]v)
	{
		for (int i=0;i<n;i++) 
			v[i]=(i+1)*(i+1);
	}

	private static void imprimirEstado() {
		System.out.print("Subconjunto suma= "+sumaDada+" --> ");
		for (int k=0;k<n;k++)
			if (marca[k]) System.out.print(v[k]+"+");
		System.out.println();
	}

	/**
	 * Realiza el backtracking para buscar todos los subconjuntos que sumen c
	 * @param nivel nivel del árbol del backtracking
	 */
	static void backtracking (int nivel)
	{
		if (nivel==n)  //hay ya un conjunto que analizar 
		{ 
			if (sumaParcial==sumaDada) 
			{
				contSol++; 
				if (numEle<numEleSol) {
					numEleSol= numEle;
					imprimirEstado();
				}
			}          
		}    
		else
			if (sumaParcial<=sumaDada && numEle<numEleSol) 
				//if sumaDada>sumaParcial se puede podar al ser positivos los valores 
				for (int j=0;j<=1;j++)
				{   
					if (j==1)
					{ 
						sumaParcial=sumaParcial+v[nivel];
						marca[nivel]=true;
						numEle++;
					}    
					backtracking (nivel+1);
					if (j==1)
					{
						sumaParcial=sumaParcial-v[nivel];
						marca[nivel]=false;
						numEle--;
					}
				}  
	}

} 
