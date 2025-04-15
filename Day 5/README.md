# 🚀 Deploy EC2 Instance Using Terraform

This guide helps you to deploy an AWS EC2 instance using Terraform.

```mermaid 
    sequenceDiagram
    participant User
    participant Terraform
    participant AWS_Console
    participant EC2_Instance

    User->>Terraform: Create `main.tf` configuration file
    User->>Terraform: Run `terraform init` to initialize Terraform
    Terraform->>User: Download AWS provider plugins
    User->>Terraform: Run `terraform plan` to preview deployment
    Terraform->>User: Display execution plan
    User->>Terraform: Run `terraform apply` to deploy EC2 instance
    Terraform->>AWS_Console: Create EC2 instance using configuration
    AWS_Console->>EC2_Instance: Launch EC2 instance
    EC2_Instance->>AWS_Console: EC2 instance is up and running
    AWS_Console->>User: Verify EC2 instance status
    User->>Terraform: Run `terraform destroy` to clean up
    Terraform->>AWS_Console: Terminate EC2 instance
    AWS_Console->>EC2_Instance: EC2 instance is terminated
    Terraform->>User: EC2 instance is destroyed

```

---

## 🧱 Prerequisites

Before you begin, make sure the following tools are installed on your system:

<p align="left">
  <img src="https://img.shields.io/badge/Terraform-7A42BF?style=for-the-badge&logo=terraform&logoColor=white" alt="Terraform"/>
  <img src="https://img.shields.io/badge/AWS%20CLI-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="AWS CLI"/>
</p>

### 📦 Install Terraform

- [Download Terraform](https://www.terraform.io/downloads.html)

### 📦 Install AWS CLI

- [Install AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)

---

## Configure AWS CLI

1. Open your terminal.
2. Run the following command to configure AWS CLI with your AWS credentials:

```bash
aws configure
```

Note: (Sync the time)


## Terraform Commands 
```bash
terraform init
terraform plan
terraform apply
```

![Screenshot 2025-04-14 151651](https://github.com/user-attachments/assets/327d47cc-b97a-4793-a60f-021c334f83c7)
![Screenshot 2025-04-14 151638](https://github.com/user-attachments/assets/cb536458-05b9-4682-a385-d2602e2075c4)



