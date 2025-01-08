using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.Linq;
using System.Linq.Expressions;
using eShop.Domain.Entities;
using eShop.Domain.Entities.Repositories;

namespace eShop.Infrastructure.Repositories
{
    public abstract class BaseInMemoryRepository<T> : IBaseRepository<T> where T : class, IEntity
    {
        protected readonly ConcurrentDictionary<Guid, T> DataStore = new();

        public T Find(Guid id)
        {
            if (DataStore.TryGetValue(id, out var entity))
            {
                return entity;
            }
            throw new KeyNotFoundException($"Entity with id {id} was not found.");
        }

        public IEnumerable<T> FindAll()
        {
            return DataStore.Values;
        }

        public IEnumerable<T> FindAll(
            Expression<Func<T, bool>> filter = null,
            Func<IQueryable<T>, IOrderedQueryable<T>> orderBy = null,
            int? pageNumber = 1,
            int? pageSize = 10)
        {
            IQueryable<T> query = DataStore.Values.AsQueryable();

            if (filter != null)
            {
                query = query.Where(filter);
            }

            if (orderBy != null)
            {
                query = orderBy(query);
            }

            int skip = ((pageNumber ?? 1) - 1) * (pageSize ?? 10);
            int take = pageSize ?? 10;

            return query
                .Skip(skip)
                .Take(take)
                .ToList();
        }

        public void Add(T entity)
        {
            var id = entity.Id;

            if (!DataStore.TryAdd(id, entity))
            {
                throw new InvalidOperationException($"Entity with id {id} already exists.");
            }
        }

        public void Update(T entity)
        {
            var id = entity.Id;

            if (!DataStore.ContainsKey(id))
            {
                throw new KeyNotFoundException($"Entity with id {id} does not exist.");
            }

            DataStore[id] = entity;
        }

        public void Delete(Guid id)
        {
            if (!DataStore.TryRemove(id, out _))
            {
                throw new KeyNotFoundException($"Entity with id {id} does not exist.");
            }
        }
    }
}