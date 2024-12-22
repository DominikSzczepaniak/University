using eShop.Domain.Entities;
using NHibernate.Mapping.ByCode;
using NHibernate.Mapping.ByCode.Conformist;

public class UserMapping : ClassMapping<User>
{
    public UserMapping()
    {
        Table("Users");
        Id(x => x.Id, m =>
        {
            m.Generator(Generators.GuidComb);
            m.Column("Id");
        });
        Property(x => x.Username, m =>
        {
            m.Column("Username");
            m.NotNullable(true);
        });
        Property(x => x.Password, m =>
        {
            m.Column("Password");
            m.NotNullable(true);
            m.Access(Accessor.Field); // To allow NHibernate to access private field
        });
        Property(x => x.Role, m =>
        {
            m.Column("Role");
            m.Type<NHibernate.Type.EnumStringType<UserRole>>(); // Map enum as string
        });
    }
}