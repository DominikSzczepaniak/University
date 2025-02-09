using NHibernate;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Linq.Expressions;

namespace eShop.Domain.Entities.Repositories
{
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

        public IEnumerable<T> FindAll(
            Expression<Func<T, bool>> filter = null,
            Func<IQueryable<T>, IOrderedQueryable<T>> orderBy = null,
            int? pageNumber = null,
            int? pageSize = null)
        {
            IQueryable<T> query = _session.Query<T>();

            if (filter != null)
            {
                query = query.Where(filter);
            }

            if (orderBy != null)
            {
                query = orderBy(query);
            }

            if (pageNumber.HasValue && pageSize.HasValue)
            {
                query = query.Skip((pageNumber.Value - 1) * pageSize.Value).Take(pageSize.Value);
            }

            return query.ToList();
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
                var entity = _session.Get<T>(id);
                if (entity != null)
                {
                    _session.Delete(entity);
                    transaction.Commit();
                }
            }
        }
    }
}