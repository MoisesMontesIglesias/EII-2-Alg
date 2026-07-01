// PROBLEMA : VIAJANTE DE COMERCIO
// VAMOS A MEDIR TIEMPOS EN DOS CASOS:
// SIN PODA Y CON PODA

package s5;

import java.util.Random;

public class ViajanteMejorTiempos
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
static int costeMejor;   // coste del ciclo mejor


public static void main (String arg[])
{
long t1,t2;
n= Integer.parseInt(arg[0]);
v= new String[n];

darValorNodos();

w=new int[n][n];

darValorPesosAristas();

origen=0; // un nodo cualquiera

camino =new int [n+1];
caminoMejor =new int [n+1];
marca=new boolean[n];

// AHORA CON PODA 
for (int j=0;j<n;j++) marca[j]=false;
camino[0]=origen;
longitud=0;  
coste=0;
costeMejor=10000000; // infinito 

t1=System.currentTimeMillis();
backtrackingPoda (origen);
t2=System.currentTimeMillis();
System.out.println("***TIEMPO CON PODA="+(t2-t1)+" MILISEGUNDOS");

// AHORA SIN PODA
for (int j=0;j<n;j++) marca[j]=false;
camino[0]=origen;
longitud=0;  
coste=0;
costeMejor=10000000; // infinito 

t1=System.currentTimeMillis();
backtracking (origen);
t2=System.currentTimeMillis();
System.out.println();
System.out.println("***TIEMPO SIN PODA="+(t2-t1)+" MILISEGUNDOS");

} // fin main 


static void darValorNodos()
{
for (int i=0;i<n;i++)
   v[i]= "NODO"+i;
}

static void darValorPesosAristas()
// grafo no dirigido completo, por lo tanto
// matriz de pesos simetrica
{
Random r=new Random();
for (int i=0;i<n;i++)
 for (int j=0;j<i;j++)
  {
   w[i][j]=r.nextInt(99)+1;
   w[j][i]=w[i][j]; 
  }
for (int i=0;i<n;i++)
    w[i][i]=Integer.MAX_VALUE;  
}

static void backtracking (int actual)
{
if (actual==origen && longitud>0)
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
    if( !marca[j]) 
     {
      longitud++;
      coste=coste+w[actual][j];
      marca[j]=true;
      camino[longitud]=j;
      backtracking(j); 
      longitud--;
      coste=coste-w[actual][j];
      marca[j]=false;
     }
}  // fin de backtracking
 

static void backtrackingPoda (int actual) 
{
if (actual==origen&&longitud>0)
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
   if( !marca[j]
        && coste< costeMejor) //PODA LOGICA
     {
      longitud++;
      coste=coste+w[actual][j];
      marca[j]=true;
      camino[longitud]=j;
      backtrackingPoda(j);
      longitud--;
      coste=coste-w[actual][j];
      marca[j]=false;
     }
} 
  
} // de clase

