using System;
using System.Collections.Generic;
using System.Text;

namespace Singleton
{
    public sealed class SingletonMultiThread
    {
        // volatile to ensure that assignment to the instance variable completes before the instance variable can be accessed
        private static volatile SingletonMultiThread instance;

        private static object syncLock = new Object();

        private SingletonMultiThread() { }

        public static SingletonMultiThread Instance
        {
            get
            {
                //This double-check locking approach solves the thread concurrency problems 
                //while avoiding an exclusive lock in every call to the Instance property method. 
                //It also allows you to delay instantiation until the object is first accessed. 
                //In practice, an application rarely requires this type of implementation. 
                //In most cases, the static initialization approach is sufficient.
                if (instance == null)
                {
                    lock(syncLock)
                    {
                        if(instance == null)
                        {
                            instance = new SingletonMultiThread();
                        }
                    }
                }
                return instance;
            }
        }

    }
}
