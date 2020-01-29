using System;
using System.Collections.Generic;
using System.Text;

namespace Singleton
{
    public sealed class SingletonStatic
    {
        //Because the Singleton instance is referenced by a private static member variable, 
        //the instantiation does not occur until the class is first referenced by a call to the Instance property. 
        //This solution therefore implements a form of the lazy instantiation property

        // Static members are 'eagerly initialized', that is, 
        // immediately when class is loaded for the first time.
        // .NET guarantees thread safety for static initialization
        private static readonly SingletonStatic instance = new SingletonStatic();

        private SingletonStatic() { }

        public static SingletonStatic Instance
        {
            get
            {
                return instance;
            }
        }
    }
}
