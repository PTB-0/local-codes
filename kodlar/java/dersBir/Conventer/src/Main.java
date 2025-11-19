import java.util.Scanner ;
public class Main {
    public static void main(String[] args){
        Scanner in = new Scanner(System.in) ;
        System.out.println("bana ilk sayıyı ver");
        double ilk = in.nextDouble();
        System.out.println(ilk);
        System.out.println("başka bir sayı giriniz");
        double ikinci = in.nextDouble() ;
        double toplam = ikinci + ilk ;
        System.out.println("3. numara");
        double ucuncu = in.nextDouble() ;
        System.out.println("toplam :" + toplam);
        in.nextLine() ;
        System.out.println("toplama , çıkarma, bölme , çarpma");
        String islem = in.toString();
        in.nextLine() ;
        double average = (ilk + ikinci + ucuncu) / 3 ;

        System.out.printf("verilenlerde ortalama %.2f%n" , average);
        if (islem == "toplama" ) {
            System.out.println(toplam);
        }
        else if (islem == "çıkarma") {
            double sonuc = ilk - ikinci ;
            System.out.println(sonuc) ;
        }
        else if (islem == "çarpma") {
            double sonuc = ilk * ikinci ;
            System.out.println(sonuc);
        }
        else {
            if (ikinci != 0) {
                double sonuc = ilk / ikinci;
                System.out.println(sonuc);
            }
            else {
                calculate() ;
            }
        }

    }
    public static double calculate() {
        double result = 1.0 ;
        return result ;
    }
}