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

// using NHibernate.Mapping.Attributes;
//
// [Class(Table = "Users")]
// public class User(string username, string password, UserRole role) : IEntity
// {
//     [Id(Name = "Id", Column = "Id")]
//     [Generator(1, Class = "guid.comb")]
//     public Guid Id { get; private set; } = Guid.NewGuid();
//
//     [Property(Column = "Username", NotNull = true)]
//     public string Username { get; private set; } = username;
//
//     [Property(Column = "Password", NotNull = true, Access = "field")]
//     private string Password { get; set; } = password;
//
//     [Property(Column = "Role", Type = "eShop.Domain.Entities.UserRole, eShop.Domain")]
//     public UserRole Role { get; private set; } = role;
//
//     public void Update(string newName, string newPassword, UserRole newRole)
//     {
//         Username = newName;
//         Password = newPassword;
//         Role = newRole;
//     }
// }
