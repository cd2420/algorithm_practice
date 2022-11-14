package dfs_bfs;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class FreezingJuice {


    static ArrayList<ArrayList<Integer>> graph = new ArrayList();
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        for (int i = 0; i < 4; i++) {
            String nums = sc.nextLine();
            ArrayList<Integer> rows = new ArrayList<>();
            for (int j = 0; j < 5; j++) {
                rows.add(Integer.valueOf(String.valueOf(nums.charAt(j))));
            }
            graph.add(rows);
        }
        int count = 0;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 5; j++) {
                if (graph.get(i).get(j) == 0) {
                    bfs(i, j);
                    count++;
                }
            }
        }

        System.out.println(count);
        for(ArrayList list: graph) {
            System.out.println(list);
        }

    }

    private static void bfs(int i, int j) {
        Queue<int[]> queue = new LinkedList();
        graph.get(i).set(j, 1);
        queue.offer(new int[]{i, j});

        while (!queue.isEmpty()) {
            int[] xy = queue.poll();
            int x = xy[0];
            int y = xy[1];
            for (int idx = 0; idx < 4; idx++) {
                int nx = x + dx[idx];
                int ny = y + dy[idx];
                if (nx >= 0 && nx < 4 && ny >= 0 && ny < 5 && graph.get(nx).get(ny) == 0) {
                    graph.get(nx).set(ny, 1);
                    queue.offer(new int[]{nx, ny});
                }
            }
        }
    }
}
