using System;
using System.Collections.Generic;
using System.Text;

namespace DependencyInversion.Entity
{
    public class Texter : IEmailer
    {
        public void SendMessage(IPerson person, string message)
        {
            Console.WriteLine($"I am texting to {person.FirstName}, for {message}");
        }
    }
}
