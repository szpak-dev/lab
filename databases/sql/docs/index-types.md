# Indexing Data In Tables (Lesson: Indexes)
When it comes to huge amounts of data, a properly **indexed** tables are crucial for overall system efficiency. You can 
use the fastest programming language out there, but it's all in vain when the data source becomes a bottleneck. Before
you start creating indexes, do some experiment first. Using **db_sql**, insert a significant numbers of records to one
of the tables (clients or cars) and try to select some rows using **WHERE** clause. Observe how much time will it take
for a Postgres to return a result. Then, index a column which was used in a query you've run and observe how much faster
it gets. Remember, that all necessary SQL commands are there in **data** directory. Also, in case of any problems, you 
can always start a new Issue in the Lab repository. Good luck.