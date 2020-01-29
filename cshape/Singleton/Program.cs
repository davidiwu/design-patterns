using System;

namespace Singleton
{
    class Program
    {
        static void Main(string[] args)
        {
            SingletonStatic ss = SingletonStatic.Instance;

            var ss2 = SingletonStatic.Instance;

            Console.WriteLine(ss);
            Console.WriteLine(ss2);

            Console.WriteLine("Hello World!");
        }
    }
}
