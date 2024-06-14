using NUnit.Framework;
using Moq;
using System.Collections.Generic;
using NUnit.Framework.Legacy;
using SimpleTaskManager.Domain;
using SimpleTaskManager.Application;

namespace SimpleTaskManager.Tests
{
    [TestFixture]
    public class TaskManagerTests
    {
        [Test]
        public void GetParentsWithChildren_Returns_ParentsWithChildren()
        {
            var parentRepositoryMock = new Mock<IParentRepository>();
            parentRepositoryMock.Setup(repo => repo.GetAllWithChildren())
                .Returns(new List<Parent>
                {
                    new Parent
                    {
                        id = 1,
                        imie = "John",
                        nazwisko = "Doe",
                        Children = new List<Child>
                        {
                            new Child { id = 1, imie = "Alice", nazwisko = "Doe", id_parent = 1 },
                            new Child { id = 2, imie = "Bob", nazwisko = "Doe", id_parent = 1 }
                        }
                    },
                    new Parent
                    {
                        id = 2,
                        imie = "Jane",
                        nazwisko = "Smith",
                        Children = new List<Child>
                        {
                            new Child { id = 3, imie = "Charlie", nazwisko = "Smith", id_parent = 2 }
                        }
                    }
                });

            var taskManager = new TaskManager(parentRepositoryMock.Object, null);

            var parentsWithChildren = taskManager.GetParentsWithChildren();

            ClassicAssert.IsNotNull(parentsWithChildren);
            ClassicAssert.AreEqual(2, parentsWithChildren.Count());

            var johnDoe = parentsWithChildren.ToList()[0];
            ClassicAssert.AreEqual(1, johnDoe.id);
            ClassicAssert.AreEqual("John", johnDoe.imie);
            ClassicAssert.AreEqual("Doe", johnDoe.nazwisko);
            ClassicAssert.IsNotNull(johnDoe.Children);
            ClassicAssert.AreEqual(2, johnDoe.Children.Count);

            var janeSmith = parentsWithChildren.ToList()[1];
            ClassicAssert.AreEqual(2, janeSmith.id);
            ClassicAssert.AreEqual("Jane", janeSmith.imie);
            ClassicAssert.AreEqual("Smith", janeSmith.nazwisko);
            ClassicAssert.IsNotNull(janeSmith.Children);
            ClassicAssert.AreEqual(1, janeSmith.Children.Count);
        }
    }
}
