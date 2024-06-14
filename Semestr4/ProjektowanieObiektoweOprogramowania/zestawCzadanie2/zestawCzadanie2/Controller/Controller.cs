using SimpleTaskManager.Domain;
using SimpleTaskManager.Application;
using System;

namespace SimpleTaskManager.Controllers
{
    public class TaskManagerController
    {
        private readonly TaskManager _taskManager;

        public TaskManagerController(TaskManager taskManager)
        {
            _taskManager = taskManager;
        }

        public void AddParent(string firstName, string lastName)
        {
            _taskManager.AddParent(firstName, lastName);
        }

        public void AddChild(string firstName, string lastName, int parentId)
        {
            _taskManager.AddChild(firstName, lastName, parentId);
        }

        public void ShowParentsWithChildren()
        {
            var parentsWithChildren = _taskManager.GetParentsWithChildren();
            foreach (var parent in parentsWithChildren)
            {
                if (parent.Children != null && parent.Children.Count > 0)
                {
                    Console.WriteLine($"Parent: {parent.imie} {parent.nazwisko}");
                    foreach (var child in parent.Children)
                    {
                        Console.WriteLine($"  - Child: {child.imie} {child.nazwisko}");
                    }
                }
            }
        }

        public void UpdateParent(int parentId, string newFirstName, string newLastName)
        {
            _taskManager.UpdateParent(parentId, newFirstName, newLastName);
        }

        public void DeleteParent(int parentId)
        {
            _taskManager.DeleteParent(parentId);
        }
    }
}