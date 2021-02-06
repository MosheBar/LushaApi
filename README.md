# Lusha API Testing 
Welcome to Lusha API infrastructure and Testing

# Pre-Installation 
Please check and install the bin\requirements.txt file
```
pip3 install bin/requirements.txt
``` 

# Adding Tests
In-Order to run your tests you will need to add the Json into test_suites.json
The format is Json format

# Running the tests
From the Main directory in the command line please run: 
```
pytest --alluredir=allure-results lusha_test_api.py
```

# viewing the resuls in allure
From the Main directory in the command line please run:
```
allure serve
```