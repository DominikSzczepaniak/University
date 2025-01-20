namespace eShop.Domain.Entities;

public class User(string username, string password, UserRole role) : IEntity
{
    public Guid Id { get; private set; } = Guid.NewGuid();
    public string Username { get; private set; } = username;
    public string Password { get; private set; } = password;
    public UserRole Role { get; private set; } = role;

    public void Update(string newName, string newPassword, UserRole newRole)
    {
        Username = newName;
        Password = password;
        Role = newRole;
    }
}