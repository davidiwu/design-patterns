using System;
using System.Collections.Generic;
using System.Text;

namespace DependencyInversion.Entity
{
    public class Person : IPerson
    {
        public string FirstName { get; set; }
        public string LastName { get; set; }
        public string EmailAddress { get; set; }
        public int Age { get; set; }
    }
}
