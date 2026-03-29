public class multithreading_simple {
    class A extends Thread{
        @Override
        public void run(){
            for(int i=0; i<5; i++){
                System.out.println("Thread A: " + i);
            }
        }
    }

    class B extends Thread{
        @Override
        public void run(){
            for(int i=0; i<5; i++){
                System.out.println("Thread B: " + i);
            }
        }
    }

    public static void main(String[] args){
        multithreading_simple mts = new multithreading_simple();
        A t1 = mts.new A();
        B t2 = mts.new B();

        t1.start();
        t2.start();
    }
}
