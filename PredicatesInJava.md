In Java, a Predicate is a functional interface that represents a boolean-valued function of a 
single argument. In simple terms, it’s a condition or test that returns either true or false.


🔹 Meaning of 

- Definition: Predicate<T> is part of the java.util.function package. It defines a single abstract method test(T t) 
that evaluates a condition on the input and returns a boolean.
- Purpose: Used to represent conditions, filters, or rules in a clean and reusable way.
- Functional Interface: Since it has only one abstract method, it can be used with lambda expressions and method references.


🔹 Example Usage


import java.util.function.Predicate;

public class PredicateDemo {
    public static void main(String[] args) {
        Predicate<Integer> isEven = x -> x % 2 == 0;

        System.out.println(isEven.test(4)); // true
        System.out.println(isEven.test(7)); // false
    }
}

- Here, isEven is a predicate that checks if a number is even.
- test(4) returns true, test(7) returns false.


🔹 Common Methods
- test(T t) → Evaluates the condition.
- and(Predicate other) → Combines two predicates with logical AND (short-circuiting).
- or(Predicate other) → Combines two predicates with logical OR (short-circuiting).
- negate() → Returns the opposite of the predicate.
- isEqual(Object targetRef) → Tests if input equals a given object.


🔹 Practical Example with Streams

Output:
Rahul
Ravi


🔹 Why Predicates Are Useful
• 	Cleaner code: Replace verbose  checks with reusable conditions.
• 	Functional style: Work seamlessly with streams (, , ).
• 	Composability: Combine multiple conditions using , , .
• 	Testing: Useful for unit tests where conditions need to be checked repeatedly.

👉 In short: A  is a functional interface for conditions that return true/false, widely used in filtering, 
validation, and stream operations.
