package repaso.java;

import java.util.Map;
import java.util.HashMap;
import java.util.ArrayList;
import java.util.Random;

/**
 *
 * @author jose
 */

public class RepasoJava {
    
    public static class ListaInteligente extends ArrayList<Integer>{
        public Integer moda(){
            int maxApar = 0;
            Integer numMasRep = null;
            Map<Integer, Integer> apariciones = new HashMap<>();
            for(int i = 0; i < this.size(); i++){
                if(apariciones.containsKey(this.get(i))){ // si existe en el mapa
                    Integer aparicionesActuales = apariciones.get(this.get(i));
                    apariciones.put(this.get(i), aparicionesActuales + 1);
                }else{ // primera vez que lo veo
                    apariciones.put(this.get(i), 1);
                }
                if(apariciones.get(this.get(i)) > maxApar){ // nuevo máximo
                    numMasRep = this.get(i);
                    maxApar = apariciones.get(this.get(i));
                }
            }
            return numMasRep;
        }
    }
    
    public static void main(String[] args) {
        Random rn = new Random();
        rn.setSeed(0);
        System.out.println(rn.nextInt(0, 10));
        Map<String, Integer> precios = new HashMap<>();
        precios.put("coche", 30000);
        precios.put("moto", 8000);
        System.out.println("El tamaño del mapa es: " + precios.size());
        
        System.out.println(precios.containsKey("coche"));
        Integer precioBarco = precios.get("barco");
        if(precioBarco == null){
            precioBarco = 100000;
        }
        System.out.println("El precio del coche es:" + precioBarco);
                        
        ListaInteligente li = new ListaInteligente();
        for(int i = 0; i < 10; i++){
            li.add(rn.nextInt(0,10));
        }
        System.out.println(li);
        System.out.println(li.moda());
        li.sort((a,b) -> {return a.compareTo(b);});
        System.out.println(li);
    }
}
