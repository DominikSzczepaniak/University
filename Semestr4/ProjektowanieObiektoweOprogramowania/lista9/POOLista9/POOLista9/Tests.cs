using NUnit.Framework;
using NUnit.Framework.Legacy;

namespace POOLista7;

public interface IFoo { }
public class Foo : IFoo { }
public class Bar : IFoo { }

[TestFixture]
public class SimpleContainerTests
{
    [Test]
    public void Resolve_ShouldReturnNewInstance_WhenTypeIsNotRegistered()
    {
        SimpleContainer container = new SimpleContainer();
        Foo foo = container.Resolve<Foo>();
        ClassicAssert.IsNotNull(foo);
        ClassicAssert.IsInstanceOf<Foo>(foo);
    }

    [Test]
    public void Resolve_ShouldReturnSingletonInstance_WhenRegisteredAsSingleton()
    {
        SimpleContainer container = new SimpleContainer();
        container.RegisterType<Foo>(true);
        Foo foo1 = container.Resolve<Foo>();
        Foo foo2 = container.Resolve<Foo>();
        ClassicAssert.AreSame(foo1, foo2);
    }

    [Test]
    public void Resolve_ShouldReturnDifferentInstances_WhenNotRegisteredAsSingleton()
    {
        SimpleContainer container = new SimpleContainer();
        container.RegisterType<Foo>(false);
        Foo foo1 = container.Resolve<Foo>();
        Foo foo2 = container.Resolve<Foo>();
        ClassicAssert.AreNotSame(foo1, foo2);
    }

    [Test]
    public void Resolve_ShouldReturnImplementationInstance_WhenInterfaceRegistered()
    {
        SimpleContainer container = new SimpleContainer();
        container.RegisterType<IFoo, Foo>(false);
        IFoo ifoo = container.Resolve<IFoo>();
        ClassicAssert.IsNotNull(ifoo);
        ClassicAssert.IsInstanceOf<Foo>(ifoo);
    }

    [Test]
    public void Resolve_ShouldReturnDifferentImplementations_WhenRegisteredMultipleTimes()
    {
        SimpleContainer container = new SimpleContainer();
        container.RegisterType<IFoo, Foo>(false);
        IFoo ifoo1 = container.Resolve<IFoo>();
        container.RegisterType<IFoo, Bar>(false);
        IFoo ifoo2 = container.Resolve<IFoo>();
        ClassicAssert.IsInstanceOf<Foo>(ifoo1);
        ClassicAssert.IsInstanceOf<Bar>(ifoo2);
    }

    [Test]
    public void Resolve_ShouldThrowException_WhenInterfaceNotRegistered()
    {
        SimpleContainer container = new SimpleContainer();
        Assert.Throws<InvalidOperationException>(() => container.Resolve<IFoo>());
    }
}