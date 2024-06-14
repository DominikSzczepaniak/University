using SimpleTaskManager.Controllers;
using SimpleTaskManager.Infrastructure;
using SimpleTaskManager.Application;
using SimpleTaskManager.Views;

namespace SimpleTaskManager
{
    class Program
    {
        static void Main(string[] args)
        {
            var context = new MyDbContext();

            var parentRepository = new ParentRepository(context);
            var childRepository = new ChildRepository(context);

            var taskManager = new TaskManager(parentRepository, childRepository);

            var controller = new TaskManagerController(taskManager);

            var view = new TaskManagerConsoleView(controller);

            view.Run();
        }
    }
}