import java.util.Scanner ;
public class Main {
    public static void main(String[] args) {
        boolean a = true ;
        Scanner in = new Scanner(System.in);
        while (a) {
            System.out.println("Bana bir sayı ver");
            int sayi = in.nextInt();
            if (sayi % 2 == 0) {
                System.out.println("sayı  :" + sayi + "  çiftir");
            } else {
                System.out.println("sayı  : " + sayi + "  tektir");
            }
            in.nextLine();
            System.out.println("çıkmak istermisiniz? : \n");
            String ask = in.next() ;
            if (ask.equals("evet")){
                System.out.println("ÇIKILIYOR");
                a = false ;
            }
        }
    }
}