## Signature Expiration Validator - AWS Lambda Function

A new AWS Lambda function was introduced to process and validate HMAC-SHA256 signatures with expiration logic. The function takes a list of test cases, each specifying payload, timestamp, current time, and expected expiration status. It generates signatures, checks if they are expired based on a 5-minute window, and returns results indicating whether each test case passes or fails. Additionally, a JSON file was added containing structured test cases for signature expiration validation, covering various scenarios including valid, expired, boundary, and skewed timestamps.

## Changes

| File(s)                                         | Change Summary                                                                                      |
|-------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| lambda_function.py                        | Added a Lambda function to process test cases for signature expiration validation, including helpers for signature generation and expiration checking. |
| event.json                                | Added a JSON file containing an array of test cases for signature expiration, each with relevant fields for validation. |

## Sequence Diagram(s)

```mermaid
sequenceDiagram
    participant User
    participant AWSConsole
    participant LambdaFunctionList
    participant Lambda
    participant SignatureLogic

    %% User interaction
    User->>AWSConsole: Log in to AWS Console
    User->>AWSConsole: Search for "Lambda" in AWS services
    AWSConsole->>LambdaFunctionList: Display list of Lambda functions
    User->>LambdaFunctionList: Click on target Lambda function (e.g., SignatureValidator)
    AWSConsole->>User: Show Lambda function dashboard

    %% Invocation
    User->>AWSConsole: Trigger Lambda function (Test tab / API Gateway / CLI)
    AWSConsole->>Lambda: Invoke lambda_handler(event, context)

    %% Lambda execution logic
    Lambda->>Lambda: Parse event and extract test cases
    loop For each test case
        Lambda->>SignatureLogic: generate_signature(payload + timestamp, secret)
        Lambda->>SignatureLogic: is_signature_expired(timestamp, current_time)
        Lambda->>Lambda: Compare actual vs expected expiration
    end

    %% Return results
    Lambda->>AWSConsole: Return results (pass/fail array)
    AWSConsole->>User: Display result logs/output

```


## Prerequisites ;)

Before you begin, make sure the following tools are installed on your system:

<p align="left">
  <img src="https://img.shields.io/badge/AWS%20CLI-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="AWS CLI"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git"/>
  <img src="https://img.shields.io/badge/AWS%20Account-FF9900?style=for-the-badge&logo=amazon&logoColor=white" alt="AWS Account"/>
</p>

---

### Required

| Tool        | Description                                  | Install Link                                                                 |
|-------------|----------------------------------------------|------------------------------------------------------------------------------|
| AWS CLI     | For deploying and managing AWS services      | [Install AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) |
| Python 3.8+ | To run/test the Lambda function locally       | [Download Python](https://www.python.org/downloads/)                         |
| Git         | For version control and cloning repos        | [Install Git](https://git-scm.com/downloads)                                 |
| AWS Account | To access AWS Lambda Console & Cloud Services| [Sign Up for AWS](https://aws.amazon.com/free/)                              |

---

### IAM Permissions

Make sure your user or role has the following permissions:

- `AWSLambda_FullAccess`
- `CloudWatchLogsFullAccess`


## How to Use this Lambda Function

### Step-by-Step Guide (AWS Console)

1. **Login to AWS Console**
   - Go to [https://console.aws.amazon.com](https://console.aws.amazon.com)

2. **Search for "Lambda"**
   - In the top search bar, type `"Lambda"` and select the **Lambda service**.

3. **Select Your Lambda Function**
   - Click on the name of your deployed Lambda function (e.g., `SignatureValidatorFunction`).

4. **Upload the Code**
   - Use the AWS Console editor or upload a `.zip` containing:
     - `lambda_function.py`
     - `event.json` (optional for testing)

5. **Configure a Test Event**
   - Go to the **Test tab**.
   - Create a new test event using the `event.json` structure provided below.

6. **Run the Function**
   - Click **"Test"** to invoke the function.
   - View the results in the **Logs/Output section**.



## Lambda Function Logic (`lambda_function.py`)

### For each test case:
1. **Input**:  
   - `payload`: The data used in the signature.
   - `timestamp`: Time the signature was generated.
   - `current_time`: Simulated "now" to check expiration.
   - `expected_expired`: Boolean flag indicating expected result.
  
    ![Screenshot 2025-04-14 171551](https://github.com/user-attachments/assets/47c63d1e-31d4-47f8-9162-728c5aed18bd)


2. **Signature Generation**:
   - Combines `payload + timestamp` as the message.
   - Uses a **secret key** to generate an HMAC-SHA256 signature.

3. **Expiration Check**:
   - Compares the `timestamp` with `current_time`.
   - If the timestamp is more than **5 minutes older**, it's expired.

4. **Validation**:
   - Compares actual expiration status with `expected_expired`.
   - Appends result (`pass` or `fail`) to the final output.

5. **Returns**:
   - A JSON object listing the result of each test case.

   ![Screenshot 2025-04-14 171601](https://github.com/user-attachments/assets/864eb8e4-c3d2-4fd8-aa75-4d99c7e1302b)


   ![Screenshot 2025-04-14 171648](https://github.com/user-attachments/assets/ad91cebd-639f-455f-8d91-fc22e9dc30c1)

   



