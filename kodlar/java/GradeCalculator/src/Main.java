import java.util.Scanner ;
public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in) ;
        System.out.println("numarasal gradini ver");
        double numGrade = in.nextDouble() ;

        char letter ;
        if ((numGrade >= 0)&&(numGrade <=100)){
            if (numGrade >= 90) {
                letter = 'A' ;
            }
            else if (numGrade >= 80) {
                letter = 'B' ;
            }
            else if (numGrade >= 70) {
                letter = 'C' ;
            }
            else if (numGrade >= 60){
                letter = 'D' ;
            }
            else {
                letter = 'F' ;
            }
            System.out.println("Your grade is : " + letter );
        }
        else {
            System.out.println("geçerli bir not diğil");
        }
    }

}