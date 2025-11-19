import java.util.Scanner ;
public class Main {
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        System.out.println("dakika ver");
        int allTime = in.nextInt() ;
        int minutes = allTime % 60 ;
        allTime = allTime - minutes ;
        int hours = allTime / 60 ;
        System.out.println("SAAT :" + hours + "  " +"Dakika : " + minutes);
    }
}