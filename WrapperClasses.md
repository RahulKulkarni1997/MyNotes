1) what is a wrapper class in java?

A) In Java, a wrapper class is an object class that encapsulates a primitive data type (like int, char, or boolean) into an object form, allowing primitives to be used where objects are required—such as in collections, generics, and APIs. Each primitive type has a corresponding wrapper class, e.g., Integer for int, Double for double, and Character for char

Key Points About Wrapper Classes

- Purpose: Convert primitive types into objects so they can be used in object-oriented contexts.

- Examples:
 int → Integer
 double → Double
 char → Character
 boolean → Boolean

-Autoboxing: Automatic conversion of a primitive to its wrapper class.
int num = 10;
Integer obj = num; // Autoboxing

- Unboxing: Automatic conversion of a wrapper object back to its primitive.
Integer obj = 20;
int num = obj; // Unboxing


Why Wrapper Classes Are Useful

- Collections: Java collections (like ArrayList) can only store objects, not primitives.
ArrayList<Integer> list = new ArrayList<>();
list.add(5); // Works with Integer, not int directly

- Generics: Generics require objects, so wrapper classes make primitives compatible.

- Utility Methods: Wrapper classes provide useful methods like Integer.parseInt("123") or Double.valueOf(3.14).

int a = 100; //Primtive Type
Integer obj = Integer.valueOf(a); // Manual boxing
int b = obj; // Unboxing

So, wrapper classes bridge the gap between primitive types and object-oriented features in Java. They’re essential when working with collections, generics, or APIs that demand objects.




2)  how autoboxing and unboxing work internally in Java.

🔄 Autoboxing (Primitive → Wrapper)

When you assign a primitive value to a wrapper class variable, the compiler automatically inserts a call to the appropriate valueOf() method.

Example:

int num = 10;
Integer obj = num; // Autoboxing

What the compiler actually does:

Integer obj = Integer.valueOf(num);

So, behind the scenes, it’s not magic—it’s just the compiler rewriting your code to use valueOf().

🔄 Unboxing (Wrapper → Primitive)

When you assign a wrapper object to a primitive variable, the compiler inserts a call to the corresponding xxxValue() method (like intValue(), doubleValue(), etc.).

Example:

Integer obj = 20;
int num = obj; // Unboxing

What the compiler actually does:

int num = obj.intValue();

⚙️ Why This Matters

Performance: Autoboxing/unboxing introduces extra method calls, which can affect performance in tight loops.

Null Safety: If you try to unbox a null wrapper, you’ll get a NullPointerException.

Integer obj = null;
int num = obj; // Throws NullPointerException

Collections: Autoboxing makes it seamless to store primitives in collections without manually converting them.

🚀 Example with Collections

import java.util.ArrayList;

public class AutoBoxingDemo {
    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<>();
        
        list.add(5); // Autoboxing: Integer.valueOf(5)
        int val = list.get(0); // Unboxing: list.get(0).intValue()
        
        System.out.println("Value: " + val);
    }
}

👉 In short, autoboxing/unboxing is just compiler sugar: it rewrites your code to call valueOf() and xxxValue() methods, making primitives and objects interchangeable in many contexts.




3) so we use wrapper classes instead of primitive as wrapper provide extra functionality


Exactly — that’s the main reason wrapper classes exist. They don’t just “wrap” primitives; they **add methods and functionality** that primitives don’t have.  

---

## ⚡ Extra Functionality Provided by Wrapper Classes
- **Utility Methods**:  
  - `Integer.parseInt("123")` → converts a string to an `int`.  
  - `Double.valueOf("3.14")` → converts a string to a `Double`.  
  - `Character.isDigit('5')` → checks if a character is a digit.  
- **Constants**:  
  - `Integer.MAX_VALUE` and `Integer.MIN_VALUE` give the range of `int`.  
  - `Double.NaN`, `Double.POSITIVE_INFINITY`, etc.  
- **Type Conversion**:  
  - `Integer.toString(42)` → `"42"`  
  - `Double.intValue()` → converts a `Double` to `int`.  
- **Collections Compatibility**:  
  - Collections like `ArrayList` can’t store primitives, but they can store wrapper objects.  
- **Generics Compatibility**:  
  - Generics require objects, so wrappers make primitives usable in generic classes.  

---

## 🚀 Example
```java
public class WrapperDemo {
    public static void main(String[] args) {
        Integer num = Integer.valueOf(100); // Wrapper object
        String str = num.toString();        // Extra functionality
        int parsed = Integer.parseInt("200"); // Convert String to int

        System.out.println("Wrapper object: " + num);
        System.out.println("String value: " + str);
        System.out.println("Parsed int: " + parsed);
    }
}
```

---

👉 So yes, we use wrapper classes instead of primitives when we need **methods, constants, conversions, or compatibility with collections/generics**. Primitives are faster and lighter, but wrappers give you **powerful tools and flexibility**.  



