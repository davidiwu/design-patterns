using System;
using System.Collections.Generic;
using System.Text;

namespace Singleton
{
    public class SingletonLazy
    {
        //The code implicitly uses LazyThreadSafetyMode.ExecutionAndPublication 
        //as the thread safety mode for the Lazy<Singleton>. 
        private static readonly Lazy<SingletonLazy> instanceLazy = 
            new Lazy<SingletonLazy>(() => new SingletonLazy());

        private SingletonLazy()
        {

        }

        public static SingletonLazy Instance
        {
            get { return instanceLazy.Value; }
        }
    }
}
