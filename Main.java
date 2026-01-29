import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);


        String[] nk = scan.nextLine().split(" ");
        int n = Integer.parseInt(nk[0]);
        int k = Integer.parseInt(nk[1]);

        List<String> k_mers = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            k_mers.add(scan.nextLine());
        }

        Map<String, Integer> kmerCounts = new HashMap<>();
        for (String k_mer : k_mers) {
            kmerCounts.put(k_mer, kmerCounts.getOrDefault(k_mer, 0) + 1);
        }

        int q = Integer.parseInt(scan.nextLine());

        List<String> queries = new ArrayList<>();
        for (int i = 0; i < q; i++) {
            queries.add(scan.nextLine());
        }

        for (int i = 0; i < q; i++) {
            String query = queries.get(i);
            if (query.length() < k) {
                System.out.println(-1);
            } else {
                Map<String, Integer> qKmerCounts = new HashMap<>();
                for (int j = 0; j <= query.length() - k; j++) {
                    String qKmer = query.substring(j, j + k);
                    qKmerCounts.put(qKmer, qKmerCounts.getOrDefault(qKmer, 0) + 1);
                }
                List<Integer> queryCounts = new ArrayList<>();
                for (String qK : qKmerCounts.keySet()) {
                    int count = kmerCounts.getOrDefault(qK, 0) / qKmerCounts.get(qK);
                    queryCounts.add(count);
                }
                System.out.println(Collections.min(queryCounts));
            }
        }

    }
}