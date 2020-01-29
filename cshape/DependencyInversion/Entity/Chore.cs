using System;
using System.Collections.Generic;
using System.Text;

namespace DependencyInversion.Entity
{
    public class Chore : IChore
    {
        private ILogger _logger;
        private IEmailer _emailer;

        public string ChoreName { get; set; }
        public IPerson Owner { get; set; }
        public double HoursWorked { get; private set; }
        public bool IsCompleted { get; private set; }        

        public Chore(ILogger logger, IEmailer emailer)
        {
            _logger = logger;
            _emailer = emailer;
        }

        public void CompleteChore()
        {
            IsCompleted = true;
            _logger.Log($"Completed {ChoreName}");

            _emailer.SendMessage(Owner, $"The Chore {ChoreName} is complete.");
        }

        public void PerformedWork(double hours)
        {
            HoursWorked += hours;
            _logger.Log($"Performed work on {ChoreName}");
        }
    }
}
