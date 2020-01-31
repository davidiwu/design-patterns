using System;

namespace Singleton
{
    class Program
    {
        static void Main(string[] args)
        {
            SingletonLazy ss = SingletonLazy.Instance;

            var ss2 = SingletonLazy.Instance;

            Console.WriteLine(ss);
            Console.WriteLine(ss2);

            Console.WriteLine("Hello World!");
        }
    }
}
