// RESUELVE UN SUDOKU 9*9 QUE HAY EN UN FICHERO 
// EL NOMBRE DEL FICHERO (sin extension) ES arg[0]
// CALCULA UNA SOLUCION Y FINALIZA

package s5;

import java.io.*;
import java.util.StringTokenizer; 

public class SudokuUna
{
static int n;      // orden sudoku 
static int[][]tab; // tablero de sudoku 
static boolean seEncontro;//primera solucion encontrada

public static void main (String arg[])
{
n=9;
String nombre=arg[0]; // se captura el nombre fichero
nombre=nombre+".txt";

tab= new int [n][n];
leerFich (nombre);

System.out.println("EL SUDOKU A RESOLVER ES:");
escribeTablero();
	
seEncontro=false;
int[]nulo=new int[2];
nulo=buscarCero(0,-1);

backtracking (nulo[0],nulo[1]);

if (! seEncontro) System.out.println ("NO HAY SOLUCION");
}

static void leerFich(String nombre)
{
String linea="";
StringTokenizer palabras; 
BufferedReader lector=null;
try
{
 lector=new BufferedReader(new FileReader(nombre));        
 for (int x=0;x<n;x++)
 {
  linea=lector.readLine();
  palabras=new StringTokenizer(linea);
  for (int y=0;y<n;y++)
   tab[x][y]=Integer.parseInt(palabras.nextToken());
 }
}
catch(Exception e)
{ 
 System.out.println("NO FICHERO");
}
try
{
 if (lector != null) lector.close();
}
catch (IOException e)
{}
} // de m todo leerFich


static void backtracking(int x,int y)
{
if (x==n)  // ya  acabo el sudoku 
 {
  seEncontro=true;
  System.out.println("SOLUCION ENCONTRADA:");
  escribeTablero();
 }
else
 for (int k=1;k<=n;k++)
 {
  if(!seEncontro && fila(x,k)&&
  columna(y,k) && region(x,y,k))
   {
    tab[x][y]=k;
    int[]nulo=new int[2];
    nulo=buscarCero(x,y);
    backtracking (nulo[0],nulo[1]);
    tab[x][y]=0;
   }
 }
}

static void escribeTablero()
{
for (int i=0;i<n;i++)
 {
 for (int j=0;j<n;j++)
   System.out.print(tab[i][j]);
 System.out.println();
 }
System.out.println();
}


static int[]buscarCero(int x,int y)
{
int[]nul=new int[2];
boolean b=true;
do
 {
 y=y+1;
 if (y==n)
  {x=x+1;y=0;}
 b=(x==n)||tab[x][y]==0;
 }
while (!b);
nul[0]=x;nul[1]=y;
return nul;
}

static boolean fila(int x,int k)
{
boolean b=true;
for (int i=0;i<n;i++)
  if (tab[x][i]==k) b=false;
return b;
}

static boolean columna(int y,int k)
{
boolean b=true;
for (int i=0;i<n;i++)
  if (tab[i][y]==k) b=false;
return b;
}

static boolean region(int x,int y,int k)
{
boolean b=true;
int bx=x-x%3; int by=y-y%3;
for (int i=bx;i<bx+3;i++)
 for (int j=by;j<by+3;j++)
   if (tab[i][j]==k) b=false;
return b;
} 

}