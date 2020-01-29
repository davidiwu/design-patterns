using DependencyInversion.Entity;
using System;
using System.Collections.Generic;
using System.Text;

namespace DependencyInversion
{
    public class Application : IApplication
    {
        private IPerson _person;
        private IChore _chore;
        public Application(IPerson person, IChore chore)
        {
            _person = person;
            _chore = chore;
        }

        public void Run()
        {
            _person.FirstName = "David";
            _person.LastName = "Wu";
            _person.EmailAddress = "david@company.com";
            _person.Age = 18;

            _chore.ChoreName = "Take out the trash";
            _chore.Owner = _person;

            _chore.PerformedWork(3);
            _chore.PerformedWork(2.1);
            _chore.CompleteChore();
        }
    }
}
