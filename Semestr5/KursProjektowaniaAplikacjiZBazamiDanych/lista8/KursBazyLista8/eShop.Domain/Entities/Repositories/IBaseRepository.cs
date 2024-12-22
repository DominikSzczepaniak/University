namespace eShop.Domain.Entities.Repositories;

public interface IBaseRepository<T> where T : class
{
    public T GetById(Guid id);
    public IEnumerable<T> GetAll();
    public void Add(T entity);
    public void Update(T entity);
    public void Delete(Guid id);
}
