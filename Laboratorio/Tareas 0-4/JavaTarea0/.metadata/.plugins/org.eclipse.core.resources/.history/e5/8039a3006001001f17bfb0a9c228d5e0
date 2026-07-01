package s5;
/* Este programa sirve para crecer el tamanno del
problema y medir tiempos para comprobar el 
comportamiento cuadratico O(n**2) del devorador1
y el comportamiento cubico =(n**3) del devorador2
*/

import java.util.Random;

public class ViajanteDevoradorTiempos
{
static int [][]w;
static int[]sol;

public static void main (String arg [] )
{
 
long t1,t2,t3,t4;
int c1=0;int c2=0;

for (int n=100;n<=1000000;n*=2)
{
w=new int[n][n] ;
sol=new int[n+1];
 
rellena(w);

t1=System.currentTimeMillis();
for (int nveces=1;nveces<=1000;nveces++)
  c1=ViajanteDevorador.devorador1(w,sol);
t2=System.currentTimeMillis();

t3=System.currentTimeMillis();
  c2=ViajanteDevorador.devorador2(w,sol);
t4=System.currentTimeMillis();

System.out.print("n="+"**"+n+"**"+c1+"**"+c2);
System.out.print("Tdevorador1="+(t2-t1)+" MICROSEGUNDOS");
System.out.println("**"+"Tdevorador2="+(t4-t3)+" MILISEGUNDOS");

}  // de for
}  // fin de main

public static void rellena(int[][]w)
{
Random r= new Random();
int n=w.length;
for(int i=0;i<n;i++)
 { w[i][i]=Integer.MAX_VALUE;
   for(int j=0;j<i;j++)
   {
    w[i][j]=r.nextInt(99)+1; // valores entre 1 y 99
    w[j][i]=w[j][i]; //simetrica   
   }
 }
} 
 
}
