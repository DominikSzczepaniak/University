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
            var context = new MyDbContext(); // Inicjalizacja kontekstu bazy danych

            // Inicjalizacja repozytoriów
            var parentRepository = new ParentRepository(context);
            var childRepository = new ChildRepository(context);

            // Inicjalizacja managera z repozytoriami
            var taskManager = new TaskManager(parentRepository, childRepository);

            // Inicjalizacja kontrolera z managerem
            var controller = new TaskManagerController(taskManager);

            // Inicjalizacja widoku z kontrolerem
            var view = new TaskManagerConsoleView(controller);

            // Uruchomienie widoku
            view.Run();
        }
    }
}