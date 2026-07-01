package s5;


/* Este programa sirve resolver el problema del viajante
mediante dos algoritmos devoradores  y probar su
funcionamiento en el ejemplo del guion de practicas
*/

public class ViajanteDevorador
{
static String[]v;  // vector de vodos
static int [][]w;  // matriz de pesos de aristas
static int [] sol; // solucion

public static void main (String arg [] )
{
int n=7;
v=new String[n];
for (int i=0;i<n;i++)
  v[i]="NODO"+i;

w=new int[n][n];

sol= new int [n+1];

rellenaPesos(w);
escribePesos(w); 

sol[0]=0;
int coste1=devorador1(w,sol);
System.out.println ("EL COSTE DEL CICLO DEVORADOR1 ES="+coste1); 
System.out.println ("EL CICLO ES");
escribeSolucion(sol);

int coste2=devorador2(w,sol);
System.out.println ("EL COSTE DEL CICLO DEVORADOR2 ES="+coste2);
System.out.println ("EL CICLO ES"); 
escribeSolucion(sol);
} // fin de main

public static int devorador1 (int[][]w,int[]sol)
/* este metodo es iterativo y su complejidad temporal 
   cuadrática O(n**2) */ 
{
int n=w.length;
boolean[]marca = new boolean[n];
for (int k=0;k<n;k++) marca[k]=false; 
marca[sol[0]]=true;
int actual=sol[0];
int coste=0;
 
for (int i=1;i<=n-1;i++)
 {
  int min=Integer.MAX_VALUE;
  int pos=-1;
  for (int j=0;j<n;j++)
   if (!marca[j] && w[actual][j]<min)
     {
      min=w[actual][j];
      pos=j;
     }
  coste=coste+min;
  sol[i]=pos;
  marca[pos]=true;
  actual=pos;
 } 
sol[n]=sol[0]; // cierra ciclo
return coste+w[sol[n-1]][sol[0]];
// retorma coste del ciclo
}     

public static int devorador2 (int[][]w,int[]sol)
/* metodo iterativo de complejidad cubica O(n**3)*/ 
{
int n=w.length;
int[]solparcial=new int [n+1];
int costemin=Integer.MAX_VALUE;

for (int i=0;i<n;i++)   
 {
  solparcial[0]=i;
  int coste=devorador1(w,solparcial);
//System.out.println(i+"***"+coste);
//for (int j=0;j<=n;j++)
//System.out.println (solparcial[j]);
  if (coste<costemin)
   {costemin=coste;
    for (int j=0;j<=n;j++)
      sol[j]=solparcial[j];
   }
 }
return costemin;
}

public static void  rellenaPesos(int[][]w)
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

public static void escribePesos (int[][]w)
/* escribe la matriz de costes */
{
int n=w.length;
for (int i=0; i<n; i++)
 {
  for (int j=0; j<n; j++)
    System.out.print (w[i][j]+"//");
  System.out.println ();
 }
System.out.println ();
}  


public static void escribeSolucion(int[]sol)
/* escribe el ciclo a seguir */
{
int m=sol.length;
for (int i=0; i<m;i++)
  System.out.print (v[sol[i]]+"--");
System.out.println ();
System.out.println ();
}   
}