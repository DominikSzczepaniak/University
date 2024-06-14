using System;
using SimpleTaskManager.Controllers;

namespace SimpleTaskManager.Views
{
    public class TaskManagerConsoleView
    {
        private readonly TaskManagerController _controller;

        public TaskManagerConsoleView(TaskManagerController controller)
        {
            _controller = controller;
        }

        public void Run()
        {
            Console.WriteLine("Welcome to Simple Task Manager!");

            while (true)
            {
                Console.WriteLine("\nMenu:");
                Console.WriteLine("1. Add Parent");
                Console.WriteLine("2. Add Child");
                Console.WriteLine("3. Show Parents with Children");
                Console.WriteLine("4. Update Parent");
                Console.WriteLine("5. Delete Parent");
                Console.WriteLine("6. Exit");
                Console.Write("Enter your choice: ");

                string choice = Console.ReadLine();

                switch (choice)
                {
                    case "1":
                        AddParent();
                        break;
                    case "2":
                        AddChild();
                        break;
                    case "3":
                        ShowParentsWithChildren();
                        break;
                    case "4":
                        UpdateParent();
                        break;
                    case "5":
                        DeleteParent();
                        break;
                    case "6":
                        Console.WriteLine("Exiting...");
                        return;
                    default:
                        Console.WriteLine("Invalid choice. Please try again.");
                        break;
                }
            }
        }

        private void AddParent()
        {
            Console.Write("Enter parent's first name: ");
            string firstName = Console.ReadLine();
            Console.Write("Enter parent's last name: ");
            string lastName = Console.ReadLine();
            _controller.AddParent(firstName, lastName);
            Console.WriteLine("Parent added successfully!");
        }

        private void AddChild()
        {
            Console.Write("Enter child's first name: ");
            string firstName = Console.ReadLine();
            Console.Write("Enter child's last name: ");
            string lastName = Console.ReadLine();
            Console.Write("Enter parent's ID: ");
            int parentId = int.Parse(Console.ReadLine());
            _controller.AddChild(firstName, lastName, parentId);
            Console.WriteLine("Child added successfully!");
        }

        private void ShowParentsWithChildren()
        {
            _controller.ShowParentsWithChildren();
        }

        private void UpdateParent()
        {
            Console.Write("Enter parent's ID: ");
            int parentId = int.Parse(Console.ReadLine());
            Console.Write("Enter new first name: ");
            string newFirstName = Console.ReadLine();
            Console.Write("Enter new last name: ");
            string newLastName = Console.ReadLine();
            _controller.UpdateParent(parentId, newFirstName, newLastName);
            Console.WriteLine("Parent updated successfully!");
        }

        private void DeleteParent()
        {
            Console.Write("Enter parent's ID: ");
            int parentId = int.Parse(Console.ReadLine());
            _controller.DeleteParent(parentId);
            Console.WriteLine("Parent deleted successfully!");
        }
    }
}
