

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/*
 * GRUPO N 2
 * 
 * INTEGRANTES:
 * DNI			APELLIDO Y NOMBRE
 * 43520743 	Mallia Leandro Raul
 * 4456058		Reggio Matina Julian Ezequiel
 * 39208705		Pascual	Pablo Ezequiel
 * 
*/
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
package unlam.edu.un;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;


public class App {
																
	public static Map<String,CriptoMoneda> criptomonedas = new HashMap<>();									//VARIABLES GLOBALES QUE SE ACTUALIZAN CON EL DESARROLLO DEL PROGRAMA
	public static Map<String,Mercado> mercados = new HashMap<>();
	public static Map<String,Usuario> usuarios = new HashMap<>();
	
	
	public static void main(String[] args) {																//MAIN													

	    Scanner scan = new Scanner(System.in);
	    String nombreUsuario;
	    Usuario u1 = null;
	    boolean entradaValida = true;
	    
	    																									
		Archivo.crearArchivoCriptomonedas("criptomonedas.csv");												//CREACION DE ARCHIVOS (DENTRO SE VERIFICAN SI YA EXISTEN)
		Archivo.crearArchivoMercados("mercados.csv");
        Archivo.crearArchivoUsuarios("usuarios.csv");
		
		
        try {
        	
        	criptomonedas = Archivo.cargarArchivoCriptomonedas("criptomonedas.csv");						//CARGA DE ARCHIVOS YA EXISTENTES
        	mercados= Archivo.cargarArchivoMercados("mercados.csv");
            usuarios=Archivo.cargarArchivoUsuarios("usuarios.csv");

        } catch (IOException e) {
            e.printStackTrace();
            System.out.println(e.getMessage());
        }
        
        
        System.out.println("Ingrese el nombre de usuario para inicar el sistema:");
        
        do {
        
	        nombreUsuario = scan.next();	  																//INGRESO DE NOMBRE DE USUARIO      
	        scan.nextLine();																				//LIMPIEZA DE BUFFER
	        
	        try {	
	        	
	        	if (nombreUsuario == null || !nombreUsuario.matches("[a-zA-Z]+")) {							//VERIFICACION DE CARACTERES
	                throw new MiExcepcion("El valor ingresado no es alfabético.");
	            }
	        	
		        if(usuarios.containsKey(nombreUsuario)) {													//VERIFICACION DE EXISTENCIA DE USUARIO
		        	u1 = usuarios.get(nombreUsuario);
		        }else {
		        	System.out.println("Usuario no regisrado en el sistema, pasando a crear usuario.");
		        	u1 = UsuarioTrader.crearUsuario(scan, nombreUsuario);  									//SI NO EXISTE SE PASA A SU CREACION
		        }
		        entradaValida = true;
		        
	        } catch (MiExcepcion e) {
                System.out.println(e.getMessage());
            }
	        
        } while (!entradaValida);
        
        
        System.out.println(u1);																				//SE MUESTRA LOS DETALLES DEL USUARIO
        u1.getMenu(scan);																					//SE PASA AL MENU DEL CORRESPONDIENTE USUARIO
        
      
        Archivo.guardarArchivoCriptomonedas(criptomonedas, "criptomonedas.csv");							//GUARDADO DE ARCHIVOS CON LAS MODIFICACIONES CREADAS
        Archivo.guardarArchivoMercados(mercados, "mercados.csv");
        Archivo.guardarArchivoUsuarios(usuarios, "usuarios.csv");
        
        System.out.println("Se guardo el archivo de criptomonedas, se procede a salir del sistema");

	}
}


