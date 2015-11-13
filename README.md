# fibonacci-rest-app
* To set up app clone the project
* Install flask **sudo pip install flask-restful**
* Run the application using **python app.py**
* Run individual test files test.py and func_test.py or use **python -m unittest discover**

**USAGE**
* By default the app runs on 5000
* Set **debug=False** in production
* Once the app is running access the app using the following REST APIs
     * http://[ip or hostname]:5000/fibonacci/get/[num]

This App can be extended to more features by using specific class handlers for each task or if the functionality is too complex Django will be better suited in future.
I have run sample benchmarks for 100000 requests and 10 concurrent connections. This looks good. But Production is a different story where we need to perform load balancing to handle heavy requests.

Tests
* There are two tests one is a functional test and other is a unittest that i have writter for this project. I have tested the status code and json payload in functional testing. And fibonacci logic in unit testing.
* other tests that might help are Liveserver test, Code coverage, and If there is going to be continous integration, respective build integration tests will serve this project well.
