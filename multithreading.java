import java.util.*;

public class multithreading {

    public static void methodOne(){
        Thread t1 = new Thread(new Runnable() {
            @Override
            public void run() {
                for(int i=0; i<5; i++){
                    System.out.println("Thread 1: " + i);
                }
            }
        });

        Thread t2 = new Thread(new Runnable() {
            @Override
            public void run() {
                for(int i=0; i<5; i++){
                    System.out.println("Thread 2: " + i);
                }
            }
        });

        t1.start();
        t2.start();
    }
    public static void main(String[] args){
        methodOne();
        // methodTwo();
    }
}