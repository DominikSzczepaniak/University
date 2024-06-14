using NUnit.Framework;
using NUnit.Framework.Legacy;
using System;

namespace POOLista7
{
    public interface IFoo { }
    public class Foo : IFoo { }
    public class Bar : IFoo { }
    public class A
    {
        public B b;
        public Z z;
        public A(B b, Z z)
        {
            this.b = b;
            this.z = z;
        }
    }

    public class C
    {
        public B b;

        public C(B b)
        {
            this.b = b;
        }
    }
    public class B { }
    public class X
    {
        public X(Y y, string s) { }
    }
    public class Y { }
    public class Z
    {
        public A a;
        public Z(A a)
        {
            this.a = a;
        }
    }

    public class AA
    {
        public BB b;
        public IC c;

        public AA(BB b, IC c)
        {
            this.b = b;
            this.c = c;
        }
    }

    public class BB { }

    public interface IC{}

    public class CC : IC{}



    public class przyklad1a
    {
        public przyklad1b b;

        public przyklad1a(przyklad1b b)
        {
            this.b = b;
        }
    }
    public class przyklad1b{}

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

        [Test]
        public void RegisterInstance_ShouldReturnSameInstance_WhenResolved()
        {
            SimpleContainer container = new SimpleContainer();
            IFoo foo1 = new Foo();
            container.RegisterInstance<IFoo>(foo1);
            IFoo foo2 = container.Resolve<IFoo>();
            ClassicAssert.AreSame(foo1, foo2);
        }

        [Test]
        public void RegisterInstance_ShouldOverridePreviousRegistration()
        {
            SimpleContainer container = new SimpleContainer();
            IFoo foo1 = new Foo();
            container.RegisterInstance<IFoo>(foo1);
            IFoo foo2 = new Bar();
            container.RegisterInstance<IFoo>(foo2);
            IFoo resolvedInstance = container.Resolve<IFoo>();
            ClassicAssert.AreSame(foo2, resolvedInstance);
            ClassicAssert.AreNotSame(foo1, resolvedInstance);
        }

        [Test]
        public void Resolve_ShouldInjectDependencies()
        {
            SimpleContainer container = new SimpleContainer();
            container.RegisterType<B>(false);
            C a = container.Resolve<C>();
            ClassicAssert.IsNotNull(a);
            ClassicAssert.IsNotNull(a.b);
        }

        [Test]
        public void Przyklad1()
        {

            SimpleContainer c = new SimpleContainer();
            przyklad1a a = c.Resolve<przyklad1a>();
            ClassicAssert.IsNotNull(a.b);
        }

        [Test]
        public void Przyklad2()
        {
            SimpleContainer container = new SimpleContainer();
            container.RegisterInstance("ala ma kota");
            container.RegisterType<Y>(false);
            X x = container.Resolve<X>();
            ClassicAssert.IsNotNull(x);
        }

        [Test]
        public void Przyklad3()
        {
            SimpleContainer c = new SimpleContainer();
            c.RegisterType<IC, CC>(false);
            AA a = c.Resolve<AA>();
            ClassicAssert.IsNotNull(a.b);
            ClassicAssert.IsNotNull(a.c);
        }

        [Test]
        public void Resolve_ShouldThrowException_WhenDependencyCannotBeResolved()
        {
            SimpleContainer container = new SimpleContainer();
            Assert.Throws<InvalidOperationException>(() => container.Resolve<X>());
        }

        [Test]
        public void Resolve_ShouldThrowException_WhenCyclicDependencyDetected()
        {
            SimpleContainer container = new SimpleContainer();
            container.RegisterType<A, A>(false);
            container.RegisterType<Z, Z>(false);
            Assert.Throws<InvalidOperationException>(() => container.Resolve<A>());
        }
    }
}
