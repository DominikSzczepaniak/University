// See https://aka.ms/new-console-template for more information

using eShop.Domain;
using eShop.Domain.Entities;
using FluentNHibernate.Cfg;
using FluentNHibernate.Cfg.Db;
using NHibernate.Cfg;
using NHibernate.Mapping.Attributes;
using NHibernate.Mapping.ByCode;

class Program
{
    public static void Main()
    {
        
        
        //Mapping by code
        // var mapper = new ModelMapper();
        // mapper.AddMapping<UserMapping>();
        // var configuration = new Configuration();
        // configuration.AddMapping(mapper.CompileMappingForAllExplicitlyAddedEntities());

        //Fluent
        // var configuration = Fluently.Configure()
        //     .Database(
        //         MsSqlConfiguration.MsSql2012
        //             .ConnectionString(@"Server=tcp:SQLSERVERURL,1433;Initial Catalog=Test;Persist Security Info=False;User ID=USERNAME;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;Password=PASSWORD;")
        //             .ShowSql() 
        //     )
        //     .Mappings(m =>
        //             m.FluentMappings.AddFromAssemblyOf<UserMap>() 
        //     )
        //     .BuildSessionFactory();
        
        
        //Attributes
        // var configuration = new Configuration();
        // HbmSerializer.Default.Validate = true;
        // configuration.AddInputStream(HbmSerializer.Default.Serialize(typeof(User)));

    }
}