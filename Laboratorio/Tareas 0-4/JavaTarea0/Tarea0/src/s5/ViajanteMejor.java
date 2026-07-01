// PROBLEMA : VIAJANTE DE COMERCIO
// SE CALCULAN TODOS LOS CICLOS POSIBLES, 
// PARA ASI SABER EL MEJOR U OPTIMO
// TIEMPO FACTORIAL (INTRATABLE)

package s5;

public class ViajanteMejor
{
static int n;
static String []v;
static int[][]w;
static int origen;
static boolean [] marca;
static int[] camino;
static int coste;
static int longitud;

static int[]caminoMejor;// para anotar el ciclo mejor
static int costeMejor;  // coste del ciclo mejor


public static void main (String arg[])
{
n= 7;

v= new String[n];
darValorNodos();

w=new int[n][n];
darValorPesos();
escribePesos();

origen=0; // un nodo cualquiera

marca=new boolean[n];
for (int j=0;j<n;j++) marca[j]=false;

camino =new int [n+1];
caminoMejor =new int [n+1];
camino[0]=origen;
longitud=0;  
coste=0;
costeMejor=10000000; // infinito 

backtracking (origen);
System.out.println("El CICLO DE HAMILTON ES:");
for (int l=0;l<=n;l++)
  System.out.print(v[caminoMejor[l]]+"**");
System.out.println();
System.out.println("SU COSTE ES ="+ costeMejor);

} // fin main 


public static void  darValorPesos()
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

static void darValorNodos()
{
for (int i=0;i<n;i++)
   v[i]= "NODO"+i;

System.out.println ("LOS NODOS SE LLAMAN ASI:");
for (int i=0;i<n;i++)
   System.out.println(v[i]);
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
   if (coste<costeMejor)
    {
     for (int l=0;l<=longitud;l++) 
       caminoMejor[l]=camino[l];
     costeMejor=coste;
    }
   }  
 }
else
  for (int j=0;j<n;j++)
   if(!marca[j]) // hijo j de actual
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

