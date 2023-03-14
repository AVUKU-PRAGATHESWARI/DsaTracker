class Parent{
    int a=12;
}
class Child extends Parent{
    int b=1;
}
class Child1 extends Child{
    int c=2;
    int sum(){
        return a+b+c;
    }
}

public class Secondday {
    public static void main(String args[]){
        Child1 c1=new Child1();
        System.out.println(c1.sum());
    }
}
