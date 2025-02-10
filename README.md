1️⃣ Install Dependencies : pip install -r requirements.txt

2️⃣ Configuration Setup (config/config.json)

2️⃣ Authentication Manager (src/core/auth_manager.py) : 💡 SOLID Principle: Singleton Pattern ensures only one instance of AuthManager is used.

3️⃣ Abstract API Class (src/api/base_api.py) : 💡 SOLID Principle: Dependency Injection - BaseAPI ensures all API services get an auth token.

3️⃣ Abstract API Class (src/api/base_api.py) : 💡 SOLID Principle: This follows the Interface Segregation principle, ensuring that all API services implement these methods.

4️⃣ API Client (src/core/api_client.py) : 💡 SOLID Principle: The Single Responsibility Principle ensures APIClient only handles API requests.

5️⃣ User Service (src/api/user_service.py) : 💡 SOLID Principle:
✅ Liskov Substitution Principle: UserService extends BaseAPI without modifying behavior.
✅ Dependency Injection: UserService depends on APIClient, which can be replaced for testing.

6️⃣ Factory Pattern for Services (src/core/service_factory.py) : 💡 SOLID Principle: Open/Closed Principle – New services can be added without modifying existing code.

7️⃣ Test Data (data/test_data.json)

8️⃣ Config Reader (src/utils/config_reader.py)

9️⃣ Logging Utility (src/utils/logger.py) : 
✅ Singleton Logger - Prevents multiple logger instances
✅ Creates logs/ directory if missing
✅ Logs to both File (test_log.log) and Console

🔟 Test Fixtures (conftest.py)

1️⃣1️⃣ CRUD API Tests (tests/test_users.py)

1️⃣2️⃣ Run Tests : 
pytest -v --html=reports/pytest-html-report.html --self-contained-html
pytest -m smoke
pytest -n auto

1️⃣3️⃣ Docker Support :
docker build -t pytest-api-framework .
docker run pytest-api-framework
