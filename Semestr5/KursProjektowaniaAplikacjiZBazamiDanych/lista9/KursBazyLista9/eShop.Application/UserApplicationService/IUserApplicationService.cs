using eShop.Domain.Entities;

namespace eShop.Application.UserApplicationService;

public interface IUserApplicationService
{
    User GetUserById(Guid userId);
    void CreateUser(string name, string password, UserRole role);
    void UpdateUser(Guid userId, string name, string password, UserRole role);
    void DeleteUser(Guid userId);
}
