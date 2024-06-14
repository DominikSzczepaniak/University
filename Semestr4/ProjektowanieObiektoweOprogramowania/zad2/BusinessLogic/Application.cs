using SimpleTaskManager.Domain;
using System.Collections.Generic;

namespace SimpleTaskManager.Application
{
    public class TaskManager
    {
        private readonly IParentRepository _parentRepository;
        private readonly IChildRepository _childRepository;

        public TaskManager(IParentRepository parentRepository, IChildRepository childRepository)
        {
            _parentRepository = parentRepository;
            _childRepository = childRepository;
        }

        public void AddParent(string firstName, string lastName)
        {
            var parent = new Parent { imie = firstName, nazwisko = lastName };
            _parentRepository.Add(parent);
        }

        public void AddChild(string firstName, string lastName, int parentId)
        {
            var parent = _parentRepository.GetById(parentId);
            if (parent == null)
            {
                throw new Exception("Parent not found");
            }

            var child = new Child { imie = firstName, nazwisko = lastName, Parent = parent };
            _childRepository.Add(child);
        }

        public IEnumerable<Parent> GetParentsWithChildren()
        {
            return _parentRepository.GetAllWithChildren();
        }

        public void UpdateParent(int parentId, string newFirstName, string newLastName)
        {
            var parent = _parentRepository.GetById(parentId);
            if (parent == null)
            {
                throw new Exception("Parent not found");
            }

            parent.imie = newFirstName;
            parent.nazwisko = newLastName;
            _parentRepository.Update(parent);
        }

        public void DeleteParent(int parentId)
        {
            var parent = _parentRepository.GetById(parentId);
            if (parent == null)
            {
                throw new Exception("Parent not found");
            }

            _parentRepository.Delete(parent);
        }
    }

    public interface IParentRepository
    {
        void Add(Parent parent);
        void Update(Parent parent);
        void Delete(Parent parent);
        Parent GetById(int id);
        IEnumerable<Parent> GetAllWithChildren();
    }

    public interface IChildRepository
    {
        void Add(Child child);
    }
}
