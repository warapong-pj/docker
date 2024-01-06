### download sonar-scanner-cli
- https://docs.sonarsource.com/sonarqube/latest/analyzing-source-code/scanners/sonarscanner/

### example sonar-project.properties
```
# must be unique in a given SonarQube instance
sonar.projectKey=<PROJECT_KEY> 

# --- optional properties ---

# defaults to project key
sonar.projectName=<PROJECT_NAME>
sonar.sources=<PATH/TO/SRC>
# sonar.tests=<PATH/TO/TEST>

sonar.host.url=<SONARQUBE_HOST>
sonar.token=<SONARQUBE_PROJECT_TOKEN>
```