**In Java, `BaseStream` is the root interface for all stream types, while `Stream`, `IntStream`, `LongStream`, and `DoubleStream` are specialized implementations for object and primitive data processing.**  

---

## 🔹 BaseStream
- **Definition**: `BaseStream<T, S extends BaseStream<T, S>>` is the **base interface** for all streams.  
- **Purpose**: Provides common functionality like sequential/parallel execution, closing streams, and pipeline management.  
- **Key Features**:
  - Extends `AutoCloseable` (so streams can be closed).
  - Defines operations shared by all streams (like `iterator()`, `spliterator()`, `isParallel()`).  
- **Known Subinterfaces**: `Stream<T>`, `IntStream`, `LongStream`, `DoubleStream`.   

---

## 🔹 Stream<T>
- **Definition**: A stream of **object references** (generic type `T`).  
- **Usage**: Works with collections like `List`, `Set`, `Map`.  
- **Example**:
  ```java
  List<String> names = List.of("Rahul", "Priya", "Arjun");
  names.stream().filter(s -> s.startsWith("R")).forEach(System.out::println);
  ```
- **Output**:
  ```
  Rahul
  ```

---

## 🔹 IntStream
- **Definition**: Specialized stream for **primitive `int` values**.  
- **Purpose**: Avoids boxing overhead when working with integers.  
- **Example**:
  ```java
  IntStream.range(1, 5).forEach(System.out::println);
  ```
- **Output**:
  ```
  1
  2
  3
  4
  ```
- **Special Methods**: `sum()`, `average()`, `max()`, `min()`.   

---

## 🔹 LongStream
- **Definition**: Specialized stream for **primitive `long` values**.  
- **Usage**: Efficient for large numeric ranges or counters.  
- **Example**:
  ```java
  LongStream.of(100L, 200L, 300L).map(x -> x / 10).forEach(System.out::println);
  ```
- **Output**:
  ```
  10
  20
  30
  ```
- **Special Methods**: Similar to `IntStream` but for `long`.   

---

## 🔹 DoubleStream
- **Definition**: Specialized stream for **primitive `double` values**.  
- **Usage**: Ideal for mathematical and statistical computations.  
- **Example**:
  ```java
  DoubleStream.of(2.5, 3.5, 4.5).average().ifPresent(System.out::println);
  ```
- **Output**:
  ```
  3.5
  ```
- **Special Methods**: `average()`, `sum()`, `summaryStatistics()`.   

---

## 🔹 Comparison Table

| Stream Type   | Works With | Example Use | Special Features |
|---------------|------------|-------------|------------------|
| **BaseStream** | All streams | Common operations | Parallel/sequential control |
| **Stream<T>** | Objects | `List<String>` | Flexible, generic |
| **IntStream** | `int` | Ranges, sums | `sum()`, `average()` |
| **LongStream** | `long` | Large counters | Efficient for big ranges |
| **DoubleStream** | `double` | Math/statistics | `summaryStatistics()` |

---

✅ **Key Takeaway**:  
- Use **`Stream<T>`** for objects.  
- Use **`IntStream`, `LongStream`, `DoubleStream`** for primitives to avoid boxing and gain specialized numeric operations.  
- All of them inherit from **`BaseStream`**, which defines the common stream behavior.  

