using eShop.Domain.Entities;

namespace eShop.Application.UserApplicationService;

public interface IUserApplicationService
{
    UserDto GetUserById(Guid userId);
    IEnumerable<UserDto> GetAllUsers(
        string search = null,
        string sortBy = "Username",
        bool descending = false,
        int pageNumber = 1,
        int pageSize = 10);
    void CreateUser(string username, string password, UserRole role);
    void UpdateUser(Guid userId, string username, string password, UserRole role);
    void DeleteUser(Guid userId);
}