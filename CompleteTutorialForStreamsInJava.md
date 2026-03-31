Streams in Java

-- The addition of the Stream API was a significant enhancement in Java, introducing a powerful way to handle collections with functional-style operations

-- Java Streams, distinct from Java I/O streams (e.g., FileInputStream), are designed to facilitate efficient data processing operations. They act as wrappers around data sources, enabling functional-style operations without modifying the underlying data.

-- Streams are not data structures but tools for performing operations like map-reduce transformations on collections. This functionality—java.util.stream—supports functional-style operations on streams of elements.



Java Stream Creation

1) //Stream from an array 
	System.out.println("Stream from an array \n");
	Employee[] emps= {
			new Employee(1,"Rahul Kulkarni",1100000.00f),
			new Employee(2,"Venkat D",800000.00f),
			new Employee(3,"Gopinath G",2200000.00f)
	};
	Stream.of(emps).forEach(e->System.out.println("Emp Details = "+e.eId+" - "+e.ename+" - "+e.eSalary));
		
2) //Stream from a List
		
		System.out.println("\nStream from a List \n");
		List<Employee> lst =Arrays.asList(emps);
		
		lst.stream()
        .forEach(e->System.out.println("Emp Details = "+e.eId+" - "+e.ename+" - "+e.eSalary));
		
3) //Stream from individual objects
		
		System.out.println("\nStream from individual objects\n");
		Stream.of(emps[0],emps[1],emps[2])
        .forEach(e->System.out.println("Emp Details = "+e.eId+" - "+e.ename+" - "+e.eSalary));;
			
4) //Stream from Stream Builder
		
		System.out.println("\nStream from Stream Builder\n");
		
		Stream.Builder<Employee> stb=Stream.builder();
		
		stb.accept(emps[0]);
		stb.accept(emps[1]);
		stb.accept(emps[2]);
		
		Stream<Employee> sb=stb.build();
		
		sb.forEach(e->System.out.println("Emp Details = "+e.eId+" - "+e.ename+" - "+e.eSalary));
		


Java Stream Operations

1) forEach()

Syntax : void forEach(Consumer<? super T> action)

forEach() is the simplest and most common operation; it loops over the stream elements, calling the supplied function on each element.

Example:
            List<Employee> lst =Arrays.asList(emps);
            lst.stream().forEach(e->System.out.println("Emp Details = "+e.eId+" - "+e.ename+" - "+e.eSalary));
		
forEach() is a terminal operation, which means that, after the operation is performed, the stream pipeline is considered consumed, and can no longer be used. 

2) map()

Syntax:

<R> Stream<R> map(Function<? super T, ? extends R> mapper)

map() produces a new stream after applying a function to each element of the original stream. The new stream could be of a different type.

The following example converts the stream of Integers into the stream of Employees:

@Test
public void whenMapIdToEmployees_thenGetEmployeeStream() {
    Integer[] empIds = { 1, 2, 3 };
    
    List<Employee> employees = Stream.of(empIds)
      .map(employeeRepository::findById)
      .collect(Collectors.toList());
    
    assertEquals(employees.size(), empIds.length);
}
Here, we obtain an Integer stream of employee IDs from an array. Each Integer is passed to the function employeeRepository::findById()—which returns the corresponding Employee object. This effectively forms an Employee stream.


Example :
        //map()
		
        System.out.println("\n Map \n");
		List<Integer> alst = Arrays.asList(1,5,77,76,12,65,13);
		alst.stream().peek(x->System.out.print(x)).map(x->x*3).forEach(x->System.out.println(" - "+x));
		
//Output 

Map 

1 - 3
5 - 15
77 - 231
76 - 228
12 - 36
65 - 195
13 - 39



3) collect()
Syntax :
<R, A> R collect(Collector<? super T, A, R> collector)


 It is one of the common ways to get stuff out of the stream once we are done with all the processing:

 @Test
public void whenCollectStreamToList_thenGetList() {
    List<Employee> employees = empList.stream().collect(Collectors.toList());
    
    assertEquals(empList, employees);
}
collect() performs mutable fold operations (repackaging elements to some data structures and applying some additional logic, concatenating them, etc.) on data elements held in the Stream instance.

The strategy for this operation is provided via the Collector interface implementation. In the example above, we used the toList collector to collect all Stream elements into a List instance.

Example :1)
            alst.stream().filter(x->x%2!=0).collect(Collectors.toList()).forEach(System.out::println);
         2)  
            alst.stream().filter(x->x%2!=0).peek(System.out::println).collect(Collectors.toList());


4) filter()

Syntax:
Stream<T> filter(Predicate<? super T> predicate)

 This produces a new stream that contains elements of the original stream that pass a given test (specified by a predicate).

 @Test
public void whenFilterEmployees_thenGetFilteredStream() {
    Integer[] empIds = { 1, 2, 3, 4 };
    
    List<Employee> employees = Stream.of(empIds)
      .map(employeeRepository::findById)
      .filter(e -> e != null)
      .filter(e -> e.getSalary() > 200000)
      .collect(Collectors.toList());
    
    assertEquals(Arrays.asList(arrayOfEmps[2]), employees);
}
In the example above, we first filter out null references for invalid employee ids and then again apply a filter to only keep employees with salaries over a certain threshold.
	
Example :

List<Integer> alst = Arrays.asList(1,5,77,76,12,65,13,1);
alst.stream().filter(x->x%2!=0).peek(System.out::println).collect(Collectors.toList());
	

5) findFirst()

Syntax:
Optional<T> findFirst()

findFirst() returns an Optional for the first entry in the stream. The Optional can, of course, be empty:

@Test
public void whenFindFirst_thenGetFirstEmployeeInStream() {
    Integer[] empIds = { 1, 2, 3, 4 };
    
    Employee employee = Stream.of(empIds)
      .map(employeeRepository::findById)
      .filter(e -> e != null)
      .filter(e -> e.getSalary() > 100000)
      .findFirst()
      .orElse(null);
    
    assertEquals(employee.getSalary(), new Double(200000));
}
Here, the first employee with a salary greater than 100000 is returned. If no such employee exists, then null is returned.

Example:
List<Integer> alst = Arrays.asList(1,5,77,76,12,65,13,1);

Optional<Integer> k =alst.stream().filter(x->x%9==0).findFirst();
		System.out.println(k);

Optional.empty

Optional<Integer> k =alst.stream().filter(x->x%5==0).findFirst();
		System.out.println(k);

Optional[5]


6) toArray()

If we need to get an array out of the stream, we can simply use toArray():

@Test
public void whenStreamToArray_thenGetArray() {
    Employee[] employees = empList.stream().toArray(Employee[]::new);

    assertThat(empList.toArray(), equalTo(employees));
}

The syntax Employee[]::new creates an empty array of Employee—which is then filled with elements from the stream.


Example:

Object[] ass = alst.stream().toArray();

	for (int i = 0; i < ass.length; i++)
		System.out.println(ass[i]);

7) flatMap()

A stream can hold complex data structures like Stream<List<String>>. In cases like this, flatMap() helps us to flatten the data structure to simplify further operations:

List<List<String>> nestedLists=Arrays.asList(
			Arrays.asList("Rahul","Kulkarni"),
			Arrays.asList("Manoj","Akula"),
			Arrays.asList("Anvesh","Penchala"),
			Arrays.asList("Guptha","Gullapudi"),
			Arrays.asList("Venkateswarlu","Devireddy")
	);

nestedLists.stream().flatMap(Collection::stream).filter(x->(x.startsWith("R")||x.endsWith("a")||x.contains("war"))).collect(Collectors.toList()).forEach(i->System.out.println(i));
		

Notice how we were able to convert the Stream<List<String>> to a simpler Stream<String>—using the flatMap()


8)peek()
We saw forEach() earlier in this section, which is a terminal operation. However, sometimes we need to perform multiple operations on each element of the stream before any terminal operation is applied.

peek() can be useful in situations like this. Simply put, it performs the specified operation on each element of the stream and returns a new stream that can be used further. peek() is an intermediate operation:

List<Integer> alst = Arrays.asList(1,5,77,76,12,65,13,1);
alst.stream().peek(x->System.out.print(x)).map(i->i*2).forEach(s->System.out.println(" - "+s));



9) mapToInt , mapToLong and mapToDouble 

- These methods transform a stream’s elements into an IntStream, LongStream, or DoubleStream respectively, which are specialized streams for handling primitive data types efficiently. 

- By using these methods, you can avoid the overhead associated with boxing and unboxing objects.

a) mapToInt

Transforms elements to an IntStream.

Example 1:
List<String> strLst = Arrays.asList("140483","6554","56424");
strLst.stream().mapToInt(Integer::parseInt).forEach(x->System.out.println(x));

140483
6554
56424

Example 2:
List<String> strLst = Arrays.asList("140483","6554","56424","54.5345");
strLst.stream().mapToInt(Integer::parseInt).forEach(x->System.out.println(x));
		
140483
6554
56424
Exception in thread "main" java.lang.NumberFormatException: For input string: "54.5345"

b) mapToLong

Transforms elements to a LongStream.

Example 1:
List<String> strLst = Arrays.asList("14048335454","655413124354","5642465464634","54.5345");
strLst.stream().mapToLong(Long::parseLong).forEach(System.out::println);

//Output
14048335454
655413124354
5642465464634
Exception in thread "main" java.lang.NumberFormatException: For input string: "54.5345"

c) mapToDouble

Transforms elements to a DoubleStream.

Example 1:
List<String> strLst = Arrays.asList("140483","655413","5642465","54.5345");
strLst.stream().mapToDouble(Double::parseDouble).forEach(System.out::println);
		
140483.0
655413.0
5642465.0
54.5345

10) flatMapToInt , flatMapToLong , flatMapToDouble 

These operations are used when each element of a stream should be mapped to a stream of primitive values (IntStream, LongStream, or DoubleStream). They flatten the resulting streams into a single stream.

a) flatMapToInt

Maps each element to an IntStream and flattens the result.

Example 1:

List<String> strLst = Arrays.asList("140,483","655,413","5642,465","5,4.5345");
strLst.stream().flatMapToInt(x->Arrays.stream(x.split(",")).mapToInt(Integer::parseInt)).forEach(x->System.out.println(x));


140
483
655
413
5642
465
5
Exception in thread "main" java.lang.NumberFormatException: For input string: "4.5345"


b)flatMapToLong

flatMapToLong produces a LongStream.

List<String> strLst = Arrays.asList("1453453450,423423483","65664365,41323434","5646346342,46232345","52441,412412.145345");
strLst.stream().flatMapToLong(x->Arrays.stream(x.split(",")).mapToLong(Long::parseLong)).forEach(x->System.out.println(x));


1453453450
423423483
65664365
41323434
5646346342
46232345
52441
Exception in thread "main" java.lang.NumberFormatException: For input string: "412412.145345"


c) flatMapToDouble

Maps each element to a DoubleStream and flattens the result.

List<String> strLst = Arrays.asList("1453453450,423423483","65664365,41323434","5646346342,46232345","52441,412412.145345");
strLst.stream().flatMapToDouble(x->Arrays.stream(x.split(",")).mapToDouble(Double::parseDouble)).forEach(x->System.out.println(x));
		

1.45345345E9
4.23423483E8
6.5664365E7
4.1323434E7
5.646346342E9
4.6232345E7
52441.0
412412.145345


11) mapMulti

Introduced in Java 9, the mapMulti methods provide a powerful way to perform multi-level mappings, allowing you to handle more complex transformations that yield multiple results from a single input element.

mapMulti
mapMulti is a flexible version of flatMap, allowing more control over the mapping and the elements’ addition to the output.

Example :

Stream.of(1,2,3).mapMulti((nu,cons)->{
		cons.accept(nu+"a");
		cons.accept(nu+"b");
		cons.accept(nu+"c");
}).forEach(System.out::println);

1a
1b
1c
2a
2b
2c
3a
3b
3c

This example demonstrates generating three strings from each integer and adding them to the resulting stream.


a) mapMultiToInt

Stream.of("1,2,3","5,23").mapMultiToInt((s,cond)->{Arrays.stream(s.split(",")).mapToInt(Integer::parseInt).forEach(cond);}).forEach(System.out::println);
	
1
2
3
5
23

This example splits each string and maps them to integers, collecting them into an IntStream.

b) mapMultiToLong

Stream.of("12343243,54335,65446546","765757,74345").mapMultiToLong((s,cond)->{Arrays.stream(s.split(",")).mapToLong(Long::parseLong).forEach(cond);}).forEach(System.out::println);

12343243
54335
65446546
765757
74345

It splits strings and maps the parts to a LongStream

c)mapMultiToDouble 

For creating a DoubleStream.

Stream.of("1,3.34,234.43","65.3,765.46").mapMultiToDouble((s,cons)->{Arrays.stream(s.split(",")).mapToDouble(Double::parseDouble).forEach(cons);}).forEach(System.out::println);

1.0
3.34
234.43
65.3
765.46


Here, each input string is split and converted into a DoubleStream.

These operations offer greater flexibility and efficiency, particularly when dealing with primitive data types or complex data transformations. They enhance the Java Streams API by providing more granular control over data processing, allowing for more concise and expressive code.


Method Types and Pipelines

- Java stream operations are divided into intermediate and terminal operations.

- Intermediate operations such as filter() return a new stream on which further processing can be done. Terminal operations, such as forEach(), mark the stream as consumed, after which point it can no longer be used further.

- A stream pipeline consists of a stream source, followed by zero or more intermediate operations, and a terminal operation.

Here’s a sample stream pipeline, where empList is the source, filter() is the intermediate operation and count is the terminal operation:

Long empCount = empList.stream()
      .filter(e -> e.getSalary() > 200000)
      .count();

- Some operations are deemed short-circuiting operations. Short-circuiting operations allow computations on infinite streams to be completed in finite time:

Example :

Stream<Integer> infiniteStream = Stream.iterate(2, i -> i * 2);

List<Integer> collect = infiniteStream
    .skip(3)
    .limit(5)
    .collect(Collectors.toList());

Here, we use short-circuiting operations skip() to skip first three elements, and limit() to limit to five elements from the infinite stream generated using iterate().

**-****-** Lazy Evaluation **-****-**
One of the most important characteristics of Java streams is that they allow for significant optimizations through lazy evaluations.

Computation on the source data is only performed when the terminal operation is initiated, and source elements are consumed only as needed.

All intermediate operations are lazy, so they’re not executed until a result of processing is needed.


For example, consider the findFirst() example we saw earlier. How many times is the map() operation performed here? four times since the input array contains four elements?

Integer[] empIds = { 1, 2, 3, 4 };
    
    Employee employee = Stream.of(empIds)
      .map(employeeRepository::findById)
      .filter(e -> e != null)
      .filter(e -> e.getSalary() > 100000)
      .findFirst()
      .orElse(null);

Stream performs the map and two filter operations, one element at a time.

It first performs all the operations on ID 1. Since the salary of ID 1 is not greater than 100000, the processing moves on to the next element.

ID 2 satisfies both of the filter predicates and hence the stream evaluates the terminal operation findFirst() and returns the result.

No operations are performed on IDs 3 and 4.

Processing streams lazily allows for avoiding examining all the data when that’s not necessary. This behavior becomes even more important when the input stream is infinite and not just very large.


