using DependencyInversion.Entity;
using System;
using System.Collections.Generic;
using System.Text;

namespace DependencyInversion
{
    public static class Factory
    {
        public static IPerson CreatePerson()
        {
            return new Person();
        }

        public static ILogger CreateLogger()
        {
            return new Logger();
        }

        public static IEmailer CreateEmailer()
        {
            return new Emailer();
            //return new Texter();
        }

        public static IChore CreateChore()
        {
            return new Chore(Factory.CreateLogger(), Factory.CreateEmailer());
        }
    }
}
