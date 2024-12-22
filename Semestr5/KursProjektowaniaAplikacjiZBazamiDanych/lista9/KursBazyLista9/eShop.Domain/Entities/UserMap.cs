using eShop.Domain.Entities;

namespace eShop.Domain;
using FluentNHibernate.Mapping;

public class UserMap : ClassMap<User>
{
    public UserMap()
    {
        Table("Users");
        Id(x => x.Id).GeneratedBy.GuidComb().Column("Id");
        Map(x => x.Username).Column("Username").Not.Nullable();
        Map(x => x.Password).Column("Password").Not.Nullable(); // Private setter
        Map(x => x.Role).Column("Role").CustomType<UserRole>();
    }
}
