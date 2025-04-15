# AWS Deployment Guide: S3 Upload & CodePipeline Setup

This guide walks you through the process of uploading files to an S3 bucket and triggering a deployment through AWS CodePipeline.

---

## Prerequisites

<p align="left">
  <img src="https://img.shields.io/badge/AWS%20CLI-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="AWS CLI"/>
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git"/>
  <img src="https://img.shields.io/badge/AWS%20Account-FF9900?style=for-the-badge&logo=amazon&logoColor=white" alt="AWS Account"/>
</p>

- AWS CLI installed and configured (`aws configure`)
- S3 bucket already created
- CodePipeline already configured to trigger on S3 changes

---


```mermaid

sequenceDiagram
    participant User
    participant AWSConsole
    participant S3Bucket
    participant CodePipeline
    participant DeploymentTarget

    %% Step 1: AWS Console Login
    User->>AWSConsole: Login to AWS Management Console

    %% Step 2: Upload to S3
    User->>AWSConsole: Navigate to S3
    AWSConsole->>S3Bucket: Open desired bucket
    User->>S3Bucket: Upload deployment files (e.g., zip or HTML)

    %% Step 3: CodePipeline Trigger
    S3Bucket-->>CodePipeline: Trigger Source stage on file change
    CodePipeline->>CodePipeline: Run Build stage
    CodePipeline->>DeploymentTarget: Deploy to target (e.g., S3, EC2, etc.)

    %% Step 4: Completion
    CodePipeline-->>User: Notify success or failure

```

## Step 1: Upload File to S3 Bucket

1. Go to the **AWS Console**.
2. Navigate to the **S3** service.
3. Choose the desired **S3 bucket**.
4. Click **Upload**, then drag and drop your build/deployment files (e.g. `build.zip` or `index.html`).
5. Click **Upload**.

Screenshot:

![Screenshot 2025-04-15 211023](https://github.com/user-attachments/assets/da113ac4-cda5-4a2e-b053-0cae5733519a)

<br>

![Screenshot 2025-04-15 211008](https://github.com/user-attachments/assets/fc267726-9400-4ade-b5a8-003cf6d3cb3d)

---

## Step 2: Trigger CodePipeline

If your pipeline is configured to detect changes in the S3 bucket:

1. Once the file is uploaded, go to **CodePipeline** in AWS Console.
2. Select your pipeline.
3. It should start automatically. If not, click **"Release Change"** manually.

Screenshot:

![Screenshot 2025-04-15 215153](https://github.com/user-attachments/assets/847e149c-2479-4d51-b370-796cc7432988)


---

## Success Criteria

- Files uploaded to correct S3 bucket
- Pipeline automatically or manually triggered
- All stages (Source → Build → Deploy) pass successfully

---

## Notes

- Ensure your S3 bucket has proper triggers configured in the **CodePipeline source stage**.
- For large files, compress them before uploading.
- Check **CloudWatch Logs** if the pipeline fails.

---


