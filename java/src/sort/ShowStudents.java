package sort;

import java.util.*;

// 성적이 낮은 순서로 학생 출력하기
public class ShowStudents {

    private static List<Students> studentsList = new ArrayList<>();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        for(int i = 0; i < n; i++) {
            String[] m = sc.nextLine().split(" ");
            Students students = new Students(m[0], Integer.parseInt(m[1]));
            studentsList.add(students);
        }
        Collections.sort(studentsList);
        for (Students students: studentsList) {
            System.out.print(students.getName() + " ");
        }
    }

}

class Students implements Comparable<Students> {

    private String name;
    private int score;

    public Students(String name, int score) {
        this.name = name;
        this.score = score;
    }

    @Override
    public int compareTo(Students o) {
        if (this.score < o.score) {
            return -1;
        }
        return 1;
    }

    public String getName() {
        return name;
    }
}
