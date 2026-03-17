public class Main {
    public static void main(String[] args) {
        StringBuilder s = new StringBuilder("Vaibhav");
        check(s);
        System.out.println(s);
    }

    void check(StringBuilder s) {
        s.append(" Kumar");
    }
}