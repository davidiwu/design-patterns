using System;
using System.Collections.Generic;
using System.Text;

namespace DependencyInversion.Entity
{
    public interface IEmailer
    {
        void SendMessage(IPerson person, string message);
    }
}
