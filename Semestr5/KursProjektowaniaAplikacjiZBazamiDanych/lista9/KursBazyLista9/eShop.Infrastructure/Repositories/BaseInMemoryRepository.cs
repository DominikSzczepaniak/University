using eShop.Domain.Entities.Repositories;
using System.Collections.Concurrent;
using eShop.Domain.Entities;

namespace eShop.Infrastructure.Repositories;

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