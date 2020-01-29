using Autofac;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using System.Text;

namespace DependencyInversion
{
    public static class ContainerConfig
    {
        public static IContainer Configure()
        {
            var builder = new ContainerBuilder();

            builder.RegisterType<Application>().As<IApplication>();

            var assembly = Assembly.Load(nameof(DependencyInversion));

            //builder.RegisterAssemblyTypes(assembly)
            //    .Where(t => t.Namespace.Contains("Entity"))
            //    .As(t => t.GetInterfaces().FirstOrDefault(i => i.Name == "I" + t.Name));

            // Texter is implemented from IEmailer, so cannot use above code
            builder.RegisterAssemblyTypes(assembly)
                .Where(t => t.Namespace.Contains("Entity"))
                .AsImplementedInterfaces();

            return builder.Build();
        }
    }
}
