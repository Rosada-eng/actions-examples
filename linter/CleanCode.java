package linter;
/**
 * CleanCode class for linter testing.
 *
 * <p>This class is not designed for extension.
 */
public final class CleanCode {

    /**
     * Main method to execute the calculator operations.
     *
     * @param args The command line arguments (should be final).
     */
    public static void main(final String[] args) {
        final int a = 10;  // Magic number, consider using constants if needed
        final int b = 20;  // Magic number, consider using constants if needed
        int result = 0;

        result = a + b;
        System.out.println("Result: " + result);
    }

    /**
     * Adds two integers.
     *
     * @param x The first integer (should be final).
     * @param y The second integer (should be final).
     * @return The sum of the two integers.
     */
    public int add(final int x, final int y) {
        return x + y;
    }

    /**
     * Subtracts the second integer from the first.
     *
     * @param x The first integer (should be final).
     * @param y The second integer (should be final).
     * @return The result of subtracting y from x.
     */
    public int subtract(final int x, final int y) {
        return x - y;
    }
}
