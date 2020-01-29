using System;
using System.Collections.Generic;
using System.Text;

namespace DependencyInversion.Entity
{
    public interface ILogger
    {
        void Log(string message);
    }
}
