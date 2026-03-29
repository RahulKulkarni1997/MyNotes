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
