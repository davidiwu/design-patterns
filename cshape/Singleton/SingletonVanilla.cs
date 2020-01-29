using System;
using System.Collections.Generic;
using System.Text;

namespace Singleton
{
    public class SingletonVanilla
    {
        private static SingletonVanilla instance;

        private SingletonVanilla() { }

        public static SingletonVanilla Instance
        {
            get
            {
                //The instantiation is not performed until an object asks for an instance; 
                // this approach is referred to as lazy instantiation. 
                // Lazy instantiation avoids instantiating unnecessary singletons when the application starts.
                // Note: this is not thread safe
                if (instance == null)
                {
                    instance = new SingletonVanilla();
                }
                return instance;
            }
        }
    }
}
