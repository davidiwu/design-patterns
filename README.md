# About this repo:
* concepts and implementations of common design patterns
* written in both Python and C# language
* always keeps code DRY and SOLID

# SOLID principles
1. **单一职责原则(Single Responsibility Principle, SRP)**

    一个对象应该只包含单一的职责，并且该职责被完整地封装在一个类中 
    另一种定义方式：就一个类而言，应该仅有一个引起它变化的原因。简单而言，就是一个类如果职责越多，那么它被复用的可能性就越低。即这个类中一个职责变化，可能会影响到其他的职责的运作。因此，单一职责原则就是实现高内聚，低耦合，将一个类的职责降低到最小，即类的数目很多，类中职责很少，因而类被复用的可能性被提高。

2. **开闭原则(Open Close Principle)**

    开闭原则就是说对扩展开放，对修改关闭。在程序需要进行拓展的时候，不能去修改原有的代码，实现一个热插拔的效果。所以一句话概括就是：为了使程序的扩展性好，易于维护和升级。

3. **里氏代换原则(Liskov Substitution Principle)**

    里氏代换原则(Liskov Substitution Principle LSP)面向对象设计的基本原则之一。 里氏代换原则中说，任何基类可以出现的地方，子类一定可以出现。 LSP是继承复用的基石，只有当衍生类可以替换掉基类，软件单位的功能不受到影响时，基类才能真正被复用，而衍生类也能够在基类的基础上增加新的行为。

4. **接口隔离原则(Interface Segregation Principle)**

    这个原则的意思是：使用多个隔离的接口，比使用单个接口要好。还是一个降低类之间的耦合度的意思：降低依赖，降低耦合。

5. **依赖倒转原则(Dependence Inversion Principle)**

	这个是开闭原则的基础，具体内容：真对接口编程，依赖于抽象而不依赖于具体。	
	Use Dependence Injection can do the work:
    Everything is depend on interface;
    Don't call me, I will call you.
