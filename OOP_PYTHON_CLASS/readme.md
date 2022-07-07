"""
07-07-2022

OOP - Object Oriented Programming

###################################################################################################################

A class is a used to create objects that have specific as well as general properties and behaviours.
It is the layout of an object specifying the characteristics of that object.

A class is a wrapper that can be used to describe objects of the same kind having distinct characteristics. Example:
A red square shaped bread, a brown circle shaped bread.

In this example: OBJECT - Bread, Characteristics - Color, Shape.

An Object is an instance of a class; it is a defined by values passed as arguments to the method of a class.

Terms:

        1. ATTRIBUTE:       This is a property that can either be specific to a classe's method
                            (instance attribute) or general to a class (class attribute).
                          
        2. METHOD:          A function defined inside a class is called a function. Example -
                            dundeer methods (__init__, __str__), user defined functions, e.t.c.

        3. INITIALIZATION:  The process of setting the initial state of an object. A dunder method
                            .__init__() is defined and initialized with a variable self -> __init__(self).
                            On creating an object (instantiation), the instance is automatically passed
                            to the self parameter in .__init__() so that new attributes can be defined
                            on the object.
        
        4. INSTANTIATION:   Refers to the process of creating an object (creating an instance of a class);
                            a region in memory is allocated to an instantiated object.
                            
                            To check that an object is an instance of a class use : isinstance(<object>, <class>)
                            To check the class of an object use : type(object)
                          
        5. INHERITANCE:     The process of creating a child class from a parent class. The former
                            takes on all properties of the latter, and may extend the functionality
                            of the latter.


#######################################################################################################################

Read more: https://realpython.com/python3-object-oriented-programming/

"""
