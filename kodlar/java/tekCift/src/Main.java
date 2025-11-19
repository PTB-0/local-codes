import java.util.Scanner ;
public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("Bana bir sayı ver");
        int sayi = in.nextInt() ;
        if ( sayi % 2 == 0 ) {
            System.out.println("sayı  :" + sayi  + "  çiftir") ;
        }
        else {
            System.out.println("sayı  : " + sayi + "  tektir");
        }
    }
}