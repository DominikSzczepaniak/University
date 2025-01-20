using System;
using System.Collections.Generic;
using System.Linq;
using System.Linq.Expressions;

namespace eShop.Domain.Entities.Repositories
{
    public interface IBaseRepository<T> where T : class
    {
        T Find(Guid id);
        IEnumerable<T> FindAll();
        IEnumerable<T> FindAll(
            Expression<Func<T, bool>> filter = null,
            Func<IQueryable<T>, IOrderedQueryable<T>> orderBy = null,
            int? pageNumber = null,
            int? pageSize = null);
        void Add(T entity);
        void Update(T entity);
        void Delete(Guid id);
    }
}