using Autofac;
using DependencyInversion.Entity;
using System;

namespace DependencyInversion
{
    class Program
    {
        static void Main(string[] args)
        {
            FactoryTest();
            ContainerTest();
            Console.WriteLine("Hello World!");
        }

        static void FactoryTest()
        {
            IPerson owner = Factory.CreatePerson();
            owner.FirstName = "David";
            owner.LastName = "Wu";
            owner.EmailAddress = "david@company.com";
            owner.Age = 18;

            IChore chore = Factory.CreateChore();
            chore.ChoreName = "Take out the trash";
            chore.Owner = owner;

            chore.PerformedWork(3);
            chore.PerformedWork(2.1);
            chore.CompleteChore();
        }

        static void ContainerTest()
        {
            var container = ContainerConfig.Configure();
            using (var scope = container.BeginLifetimeScope())
            {
                var app = scope.Resolve<IApplication>();
                app.Run();
            }
        }
    }
}
