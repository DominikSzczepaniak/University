namespace POOLista7;

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

    public void RegisterType<T>(bool singleton) where T : class
    {
        _registrations[typeof(T)] = new Registration(typeof(T), singleton);
    }

    public void RegisterType<From, To>(bool singleton) where To : From
    {
        _registrations[typeof(From)] = new Registration(typeof(To), singleton);
    }

    public T Resolve<T>()
    {
        return (T)Resolve(typeof(T));
    }

    private object Resolve(Type type)
    {
        if (!_registrations.TryGetValue(type, out var registration))
        {
            // Jesli typ nie jest zarejestrowany i jest to typ konkretny robimy instajncje
            if (!type.IsAbstract && !type.IsInterface)
            {
                return Activator.CreateInstance(type);
            }
            throw new InvalidOperationException($"Type {type.Name} is not registered.");
        }

        // Jesli singleton i instacja istnieje
        if (registration.Singleton && registration.Instance != null)
        {
            return registration.Instance;
        }

        // Nowa instancja implementowanego typu
        var instance = Activator.CreateInstance(registration.ImplementationType);

        // Jesli singleton to zapisujemy
        if (registration.Singleton)
        {
            registration.Instance = instance;
        }

        return instance;
    }
}