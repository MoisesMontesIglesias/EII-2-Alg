// PROBLEMA 6 : VIAJANTE DE COMERCIO
// SE CALCULAN TODOS LOS CICLOS POSIBLES Y
// ESE NÚMERO DE CICLOS ES DE ORDEN FACTORIAL,
// POR LO QUE EL TIEMPO ES INTRATABLE

// El problema de viajante es un problema NP, 
// es decir, no hay solucion polinomica. 
// Esta clase calcula por backtracking todos los ciclos 
// que puede seguir el viajante. Son los ciclos simples
// de longitud n, esto es, que recorren todos los nodos. 

// El número total de ciclos es (n-1)!,pero son iguales 2 a 2.


package s5;

public class ViajanteTodos
{
static int n;
static String []v;
static int[][]w;
static int origen;      // donde vive el viajante
static boolean [] marca;// para no repetir nodos (ciclos simples)
static int[]camino;     // trayectoria de ciclo que va calculando
static int coste;       // coste acumulado del ciclo que va calculando 
static int longitud;    // nivel o longitud de ciclo que va calculando
static int nsol;        // el numero total de ciclos 


public static void main (String arg[])
{
n=7;                // mismo ejemplo tratado en devorador

v= new String[n];
darValorNodos();

w=new int[n][n];
darValorPesosAristas();
escribePesos();

origen=0; // un nodo cualquiera
System.out.println("LOS CICLOS DE LONGITUD n SON:");

marca=new boolean[n];
for (int j=0;j<n;j++) marca[j]=false;

camino =new int [n+1];
camino[0]=origen;
longitud=0;
coste=0;  
nsol=0; 

backtracking (origen);

if (nsol==0) System.out.println ("NO HAY NINGUN CICLO");
else  System.out.println ("NUMERO DE CICLOS CALCULADOS="+nsol);

} // fin main 


static void darValorNodos()

{
for (int i=0;i<n;i++)
   v[i]= "NODO"+i;

System.out.println ("LOS NODOS SE LLAMAN ASI:");
for (int i=0;i<n;i++)
   System.out.println(v[i]);
}


public static void  darValorPesosAristas()
/* carga la matriz de costes ejemplo */
{
w[0][1]=12;w[1][0]=12;w[0][2]=43;w[2][0]=43;
w[0][3]=99;w[3][0]=99;w[0][4]=57;w[4][0]=57;
w[0][5]=32;w[5][0]=32;w[0][6]=78;w[6][0]=78;
w[1][2]=10;w[2][1]=10;w[1][3]=80;w[3][1]=80;
w[1][4]=93;w[4][1]=93;w[1][5]=33;w[5][1]=33;
w[1][6]=11;w[6][1]=11;w[2][3]=60;w[3][2]=60;
w[2][4]=43;w[4][2]=43;w[2][5]=20;w[5][2]=20;
w[2][6]=22;w[6][2]=22;w[3][4]=50;w[4][3]=50;
w[3][5]=18;w[5][3]=18;w[3][6]=31;w[6][3]=31;
w[4][5]=31;w[5][4]=31;w[4][6]=73;w[6][4]=73;
w[5][6]=22;w[6][5]=22;
for (int i=0;i<w.length;i++)
  w[i][i]=Integer.MAX_VALUE;
}   

static void escribePesos()
{
System.out.println ("LA MATRIZ DE PESOS ES:");
for (int i=0;i<n;i++)
   {
   for (int j=0;j<n;j++)
     System.out.print(w[i][j]+"*");
   System.out.println();
   }   
}


static void backtracking (int actual)  // es recursivo
{
if (actual==origen && longitud>0)  // es estado solucion
 {  
  if (longitud==n)
   {
   nsol++;
   for (int l=0;l<=longitud;l++) 
     System.out.print(v[camino[l]]+"*");
   System.out.println();
   System.out.println("SU COSTE ES="+coste);
   System.out.println();
   }
 }
else
 for (int j=0;j<n;j++)
  if (!marca[j])     //hijo j de actual
    {
     longitud++;
     coste=coste+w[actual][j];
     marca[j]=true;
     camino[longitud]=j;
     backtracking(j);  // llamada sobre el hijo j 
     longitud--;
     coste=coste-w[actual][j];
     marca[j]=false;
    }
}  // fin de backtracking
  
} // de clase

