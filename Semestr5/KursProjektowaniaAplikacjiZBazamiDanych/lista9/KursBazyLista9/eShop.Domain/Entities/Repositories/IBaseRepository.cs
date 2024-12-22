namespace eShop.Domain.Entities.Repositories;

public interface IBaseRepository<T> where T : class
{
    public T Find(Guid id);
    public IEnumerable<T> FindAll();
    public void Add(T entity);
    public void Update(T entity);
    public void Delete(Guid id);
}
