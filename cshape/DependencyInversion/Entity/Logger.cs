using System;
using System.Collections.Generic;
using System.Text;

namespace DependencyInversion.Entity
{
    public class Logger : ILogger
    {
        public void Log(string message)
        {
            Console.WriteLine(message);
        }
    }
}
