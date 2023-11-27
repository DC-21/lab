public class Calculator {
    public int add (int a, int b){
        return a+b;
    }
    public int subtract (int a, int b){
        return a+b;
    }
    public int multiply (int a, int b){
        return a+b;
    }
    public int divide (int a, int b){
        if(b==0){
            throw new IllegalArgumentException("cant divide by zero");
        }
        return a/b;
    }
    public static void main(String[] args) {
        int a=2;
        int b=3;
        System.out.println(a+b);
        System.out.println(a-b);
        System.out.println(a*b);
        System.out.println(a/b);
    }
}
