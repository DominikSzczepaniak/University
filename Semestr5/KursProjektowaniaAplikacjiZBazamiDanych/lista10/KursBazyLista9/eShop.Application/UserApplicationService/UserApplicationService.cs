using eShop.Domain.Entities;
using eShop.Domain.Entities.Repositories;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Linq.Expressions;

namespace eShop.Application.UserApplicationService;

public class UserApplicationService : IUserApplicationService
{
    private readonly IBaseRepository<User> userRepository;

    public UserApplicationService(IBaseRepository<User> userRepository)
    {
        this.userRepository = userRepository;
    }

    public UserDto GetUserById(Guid userId) => MapToDto(userRepository.Find(userId));

    public IEnumerable<UserDto> GetAllUsers(
        string search = null,
        string sortBy = "Username",
        bool descending = false,
        int pageNumber = 1,
        int pageSize = 10)
    {
        Expression<Func<User, bool>> filter = null;

        if (!string.IsNullOrEmpty(search))
        {
            filter = u => u.Username.Contains(search) ||
                          u.Role.ToString().Contains(search);
        }

        Func<IQueryable<User>, IOrderedQueryable<User>> orderBy = query =>
            sortBy switch
            {
                "Username" => descending ? query.OrderByDescending(u => u.Username) : query.OrderBy(u => u.Username),
                "Role" => descending ? query.OrderByDescending(u => u.Role) : query.OrderBy(u => u.Role),
                _ => query.OrderBy(u => u.Username)
            };

        return userRepository.FindAll(filter, orderBy, pageNumber, pageSize).Select(MapToDto);
    }

    public void CreateUser(string username, string password, UserRole role)
    {
        var user = new User(username, password, role);
        userRepository.Add(user);
    }

    public void UpdateUser(Guid userId, string username, string password, UserRole role)
    {
        var user = userRepository.Find(userId);
        if (user == null) throw new InvalidOperationException("User not found.");

        user.Update(username, password, role);
        userRepository.Update(user);
    }

    public void DeleteUser(Guid userId) => userRepository.Delete(userId);

    private static UserDto MapToDto(User user) => new()
    {
        Id = user.Id,
        Username = user.Username,
        Role = user.Role.ToString(),
    };
}