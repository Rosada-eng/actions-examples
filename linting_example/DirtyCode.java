public class DirtyCode {
    public static void main(String[] args) {
     int a=10;
     int b = 20; int result=0;
     
    if (a >b) {System.out.println("a is greater");}
    else{System.out.println("b is greater");}
     
     result = a + b;
    System.out.println("Result:" + result);}
    
    public int add(int x, int y){
        return x+y;}
    public int subtract(int x, int y){return x-y;}
        }
    