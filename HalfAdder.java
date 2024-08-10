public class HalfAdder {

	// Method to perform half adder operation
	public static int[] halfAdd(int a, int b) {
		int sum = a ^ b; // XOR operation for sum
		int carry = a & b; // AND operation for carry
		return new int[]{sum, carry};
	}

	public static void main(String[] args) {
		int a = 0; // First input
		int b = 1; // Second input

		int[] result = halfAdd(a, b);
		System.out.println("Sum: " + result[0]);
		System.out.println("Carry: " + result[1]);
	}
}