using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;

namespace POOLista7
{
    [AttributeUsage(AttributeTargets.Constructor, AllowMultiple = false)]
    public class DependencyConstructorAttribute : Attribute { }

    public class SimpleContainer
    {
        private class Registration
        {
            public Type ImplementationType { get; }
            public bool Singleton { get; }
            public object Instance { get; set; }

            public Registration(Type implementationType, bool singleton)
            {
                ImplementationType = implementationType;
                Singleton = singleton;
                Instance = null;
            }
        }

        private readonly Dictionary<Type, Registration> _registrations = new Dictionary<Type, Registration>();
        private readonly Dictionary<Type, object> _instances = new Dictionary<Type, object>();
        private readonly HashSet<Type> _resolvingTypes = new HashSet<Type>();

        public void RegisterType<T>(bool singleton) where T : class
        {
            _registrations[typeof(T)] = new Registration(typeof(T), singleton);
        }

        public void RegisterType<From, To>(bool singleton) where To : From
        {
            _registrations[typeof(From)] = new Registration(typeof(To), singleton);
        }

        public void RegisterInstance<T>(T instance)
        {
            _instances[typeof(T)] = instance;
        }

        public T Resolve<T>()
        {
            return (T)Resolve(typeof(T));
        }

        private object Resolve(Type type)
        {
            if (_resolvingTypes.Contains(type))
            {
                throw new InvalidOperationException($"Cyclic dependency detected for type {type.Name}.");
            }

            if (_instances.TryGetValue(type, out var instance))
            {
                return instance;
            }

            if (!_registrations.TryGetValue(type, out var registration))
            {
                if (!type.IsAbstract && !type.IsInterface)
                {
                    return CreateInstance(type);
                }
                throw new InvalidOperationException($"Type {type.Name} is not registered.");
            }

            if (registration.Singleton && registration.Instance != null)
            {
                return registration.Instance;
            }

            _resolvingTypes.Add(type);
            instance = CreateInstance(registration.ImplementationType);
            _resolvingTypes.Remove(type);

            if (registration.Singleton)
            {
                registration.Instance = instance;
            }

            return instance;
        }

        private object CreateInstance(Type type)
        {
            var constructors = type.GetConstructors();
            ConstructorInfo selectedConstructor = null;

            var markedConstructors = constructors.Where(c => c.GetCustomAttribute<DependencyConstructorAttribute>() != null).ToArray();
            if (markedConstructors.Length > 1)
            {
                throw new InvalidOperationException($"Type {type.Name} has multiple constructors marked with [DependencyConstructor] attribute.");
            }
            else if (markedConstructors.Length == 1)
            {
                selectedConstructor = markedConstructors[0];
            }
            else
            {
                selectedConstructor = constructors.OrderByDescending(c => c.GetParameters().Length).FirstOrDefault();
            }

            if (selectedConstructor == null)
            {
                throw new InvalidOperationException($"Type {type.Name} does not have a public constructor.");
            }

            var parameters = selectedConstructor.GetParameters();
            var parameterInstances = new object[parameters.Length];

            for (int i = 0; i < parameters.Length; i++)
            {
                if (_instances.TryGetValue(parameters[i].ParameterType, out var paramInstance))
                {
                    parameterInstances[i] = paramInstance;
                }
                else
                {
                    parameterInstances[i] = Resolve(parameters[i].ParameterType);
                }
            }

            return selectedConstructor.Invoke(parameterInstances);
        }
    }
}
