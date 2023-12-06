import java.io.*;
import java.util.*;

public class Main {
    static long g(long a, long b) {
        return a-1-2*(long)((a-Math.pow(a*a-4*b,0.5))/2);
    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter writer = new PrintWriter(System.out);
        List<List<String>> data = new ArrayList<List<String>>();
        for (int i = 0; i < 2; i++) {
            data.add(new ArrayList<String>());
            for (String s : br.readLine().split(":\\s+")[1].split("\\s+")) {
                data.get(i).add(s);
            }
        }
        long p = 1L;
        String a = "", b = "";
        for (int i = 0; i < data.get(0).size(); i++) {
            String x = data.get(0).get(i), y = data.get(1).get(i);
            p *= g(Long.parseLong(x), Long.parseLong(y));
            a += x;
            b += y;
        }
        writer.println("Part 1: " + p);
        writer.println("Part 2: " + g(Long.parseLong(a), Long.parseLong(b)));
        writer.flush();
    }
}