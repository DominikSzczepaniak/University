using eShop.Domain.Entities;
using eShop.Domain.Entities.Repositories;

namespace eShop.Application.UserApplicationService;

public class UserApplicationService(IBaseRepository<User> userRepository) : IUserApplicationService
{
    public User GetUserById(Guid userId)
    {
        return userRepository.GetById(userId);
    }

    public void CreateUser(string name, string password, UserRole role)
    {
        var user = new User(name, password, role);
        userRepository.Add(user);
    }

    public void UpdateUser(Guid userId, string name, string password, UserRole role)
    {
        var user = userRepository.GetById(userId);
        if (user == null) throw new InvalidOperationException("User not found.");

        user.Update(name, password, role);
        userRepository.Update(user);
    }

    public void DeleteUser(Guid userId)
    {
        userRepository.Delete(userId);
    }
}
