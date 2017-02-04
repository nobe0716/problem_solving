package Algorithm;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class N_2589 {

	public static Queue<Integer> queue = new LinkedList<Integer>();
	public static int[][] check;
	public static int max = 0;
	public static int rowSize;
	public static int colSize;

	static class Cell {
		private int x;
		private int y;

		public Cell(int x, int y) {
			this.x = x;
			this.y = y;
		}

		public int getX() {
			return x;
		}

		public int getY() {
			return y;
		}

	}

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		String[] input = bf.readLine().split(" ");
		int r = Integer.parseInt(input[0]);
		int c = Integer.parseInt(input[1]);
		int[][] map = new int[r][c];
		check = new int[r][c];
		rowSize = r;
		colSize = c;

		for (int i = 0; i < r; i++) {
			String val = bf.readLine();
			for (int j = 0; j < c; j++) {
				check[i][j] = -1;
				if (val.charAt(j) == 'W') {
					map[i][j] = 0;
				} else {
					map[i][j] = 1;
				}
			}
		}

		for (int i = 0; i < rowSize; i++) {
			for (int j = 0; j < colSize; j++) {
				initCheckArr();
				conquer(map, i, j);
			}
		}
		System.out.println(max);

	}

	public static void conquer(int[][] map, int i, int j) {
		Queue<Cell> queue = new LinkedList<Cell>();
		check[i][j] = 0;
		queue.add(new Cell(i, j));

		while (!queue.isEmpty()) {
			Cell cell = queue.poll();
			int x = cell.getX();
			int y = cell.getY();

			if (isAcceptable(map, x - 1, y)) {
				check[x - 1][y] = check[x][y] + 1;
				checkMax(check[x - 1][y]);
				queue.add(new Cell(x - 1, y));
			}
			if (isAcceptable(map, x + 1, y)) {
				check[x + 1][y] = check[x][y] + 1;
				checkMax(check[x + 1][y]);
				queue.add(new Cell(x + 1, y));
			}
			if (isAcceptable(map, x, y - 1)) {
				check[x][y - 1] = check[x][y] + 1;
				checkMax(check[x][y - 1]);
				queue.add(new Cell(x, y - 1));
			}
			if (isAcceptable(map, x, y + 1)) {
				check[x][y + 1] = check[x][y] + 1;
				checkMax(check[x][y + 1]);
				queue.add(new Cell(x, y + 1));
			}
		}

	}

	public static boolean isAcceptable(int[][] map, int i, int j) {
		if (i < 0 || i > rowSize - 1 || j < 0 || j > colSize - 1) {
			return false;
		}
		if (map[i][j] == 0) { // 육지가 아니면
			return false;
		}
		if (check[i][j] != -1) { // 이미 방문했으면
			return false;
		}
		return true;

	}

	public static void initCheckArr() {
		for (int[] row : check) {
			Arrays.fill(row, -1);
		}

	}

	public static void checkMax(int n) {
		if (n > max) {
			max = n;
		}
	}
}