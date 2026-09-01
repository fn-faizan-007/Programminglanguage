package javaOops;
import java.util.*;

 class funtion{
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        int[] makes={12,34,35,67,8};
        System.out.print("Enter a num that you want to find out:  ");
         int find=sc.nextInt();
          for(int i=0;i<=makes.length;i++){
            if (makes[i]==find){
                System.out.println(makes[i]+" And this num will be in the index of: "+i);

            }
        }

    }
 }


