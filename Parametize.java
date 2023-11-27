import java.util.Scanner;

public class Parametize {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        checkpoint("Project Kickoff", "Define objectives, roles, and schedule.", scanner);
        checkpoint("Development/Implementation", "Execute plan, monitor progress.", scanner);
        checkpoint("Post-Implementation Review", "Evaluate success, gather feedback.", scanner);

        System.out.println("Project Checkpoints Simulation complete. Goodbye!");
    }

    private static void checkpoint(String name, String description, Scanner scanner) {
        System.out.printf("Checkpoint: %s%n%s%nPress Enter to continue...%n", name, description);
        scanner.nextLine();
    }
}
