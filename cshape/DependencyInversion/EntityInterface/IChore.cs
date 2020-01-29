using System;
using System.Collections.Generic;
using System.Text;

namespace DependencyInversion.Entity
{
    public interface IChore
    {
        string ChoreName { get; set; }
        IPerson Owner { get; set; }
        double HoursWorked { get;}
        bool IsCompleted { get;}

        void PerformedWork(double hours);

        void CompleteChore();
    }
}
