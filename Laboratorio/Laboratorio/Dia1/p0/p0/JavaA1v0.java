package p0 ;

public class JavaA1v0
{

static boolean primoA1(int m)
{
boolean p=true;
for (int i=2;i<=m-1;i++)
	if (m%i==0)
          p=false;
return p;
}
 
public static void main (String arg [] )
{
long t1,t2;                  //obligatoriamente de tipo long para no desbordar
// la toma de tiempos en Java se verá con más profundidad en la sesión siguiente


t1=System.currentTimeMillis();	// milisegundos (sin decimales) 
	
System.out.println("10000="+primoA1(10000)+"****"+"10007="+primoA1(10007)) ;

t2=System.currentTimeMillis();	

System.out.println(t1+"///"+t2);

System.out.println ("tiempo = "+(t2-t1)+" milisegundos");

} // fin de main

} // fin de clase

