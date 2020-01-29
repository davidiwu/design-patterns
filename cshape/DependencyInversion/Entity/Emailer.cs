using System;
using System.Collections.Generic;
using System.Text;

namespace DependencyInversion.Entity
{
    public class Emailer : IEmailer
    {
        public void SendMessage(IPerson person, string message)
        {
            Console.WriteLine($"send {message} to {person.EmailAddress}");
        }
    }
}
