using System;
using System.Collections.Generic;
using System.Text;

namespace DependencyInversion.Entity
{
    public interface IPerson
    {
        string FirstName { get; set; }
        string LastName { get; set; }
        string EmailAddress { get; set; }
        int Age { get; set; }
    }
}
