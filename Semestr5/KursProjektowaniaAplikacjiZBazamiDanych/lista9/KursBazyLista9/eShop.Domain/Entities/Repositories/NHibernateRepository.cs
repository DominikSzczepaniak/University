using eShop.Domain.Entities.Repositories;
using NHibernate;

public class NHibernateRepository<T> : IBaseRepository<T> where T : class
{
    private readonly ISession _session;

    public NHibernateRepository(ISession session)
    {
        _session = session;
    }

    public T Find(Guid id)
    {
        return _session.Get<T>(id);
    }

    public IEnumerable<T> FindAll()
    {
        return _session.Query<T>().ToList();
    }

    public void Add(T entity)
    {
        using (var transaction = _session.BeginTransaction())
        {
            _session.Save(entity);
            transaction.Commit();
        }
    }

    public void Update(T entity)
    {
        using (var transaction = _session.BeginTransaction())
        {
            _session.Update(entity);
            transaction.Commit();
        }
    }

    public void Delete(Guid id)
    {
        using (var transaction = _session.BeginTransaction())
        {
            _session.Delete(id);
            transaction.Commit();
        }
    }
}