Employee → Manager (Simple Code)

import java.util.*;

class Employee {
    String name;
    int age;

    void input() {
        Scanner sc = new Scanner(System.in);
        System.out.print("Name: ");
        name = sc.next();
        System.out.print("Age: ");
        age = sc.nextInt();
    }

    void display() {
        System.out.println(name + " " + age);
    }
}

class Manager extends Employee {
    double salary;

    void inputManager() {
        input();
        Scanner sc = new Scanner(System.in);
        System.out.print("Salary: ");
        salary = sc.nextDouble();
    }

    void displayManager() {
        display();
        System.out.println("Salary: " + salary);
    }
}

public class Main {
    public static void main(String[] args) {
        Manager m = new Manager();

        m.inputManager();
        m.displayManager();
    }
}


2. Library Management (Simple Menu Code)

import java.util.*;

class Library {
    ArrayList<String> books = new ArrayList<>();

    void addBook(String b) {
        books.add(b);
    }

    void showBooks() {
        System.out.println(books);
    }

    void issueBook(String b) {
        if (books.contains(b)) {
            books.remove(b);
            System.out.println("Issued");
        } else {
            System.out.println("Not available");
        }
    }

    void returnBook(String b) {
        books.add(b);
        System.out.println("Returned");
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Library lib = new Library();

        int ch;
        do {
            System.out.println("\n1 Add 2 Show 3 Issue 4 Return 5 Exit");
            ch = sc.nextInt();
            sc.nextLine();

            switch (ch) {
                case 1:
                    lib.addBook(sc.nextLine());
                    break;
                case 2:
                    lib.showBooks();
                    break;
                case 3:
                    lib.issueBook(sc.nextLine());
                    break;
                case 4:
                    lib.returnBook(sc.nextLine());
                    break;
            }
        } while (ch != 5);
    }
}
