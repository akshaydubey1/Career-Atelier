# Technology map

Read this before any resume edit that adds, moves or renames a technology. It keeps every edit technically coherent: right ecosystem, right era, right words. It is a starting point, not a complete list; apply the same reasoning to tools not listed here.

## 1. Ecosystems: what naturally goes together

A role's bullets should read like one real stack. Pair tools within the ecosystem the role actually used.

| Ecosystem | Belongs together | Doesn't belong (unless the role truly used both) |
| --- | --- | --- |
| AWS | EKS, EC2, VPC, IAM (roles, policies, IRSA), IAM Identity Center, Organizations/SCPs, CloudFormation/CDK, CodePipeline/CodeBuild, CloudWatch, CloudTrail, Config, Security Hub, Systems Manager, Secrets Manager, ECR, ALB/NLB, Route 53 | AKS, Entra ID, Cloud Build, Stackdriver in the same bullet |
| Azure | AKS, VNets, Entra ID (formerly Azure AD), Azure RBAC, Managed Identities, Key Vault, ARM/Bicep, Azure DevOps Pipelines, Azure Monitor, Defender for Cloud, Azure Policy, ACR, App Gateway, Front Door | IRSA, CloudFormation, GKE Workload Identity |
| GCP | GKE, VPC, Cloud IAM, Workload Identity, Organization Policy, Deployment Manager, Cloud Build, Cloud Monitoring/Logging (formerly Stackdriver), Secret Manager, Artifact Registry, Cloud Load Balancing, Anthos | IRSA, ARM templates, Azure Monitor |
| Red Hat / on-prem | OpenShift, RHEL, Ansible (Tower/AAP), Quay, OpenShift GitOps (Argo CD) | — |
| Kubernetes (any cloud) | Helm, Kustomize, Argo CD/Flux, ingress controllers, cert-manager, HPA/VPA, PDBs, quotas, RBAC, OPA Gatekeeper/Kyverno, Prometheus, Istio/Linkerd | — |
| HashiCorp | Terraform, Vault, Consul, Packer, Nomad, Terraform Cloud/Enterprise, Sentinel | — |
| Java services | Spring Boot, Maven/Gradle, JUnit, Tomcat/JBoss/WebLogic/WebSphere, Nexus/Artifactory | — |

**Rule:** a bullet names tools from one coherent stack. Multi-cloud work is fine when the role really was multi-cloud; say so plainly ("across AWS and Azure") instead of mixing services silently.

## 2. Equivalents: same job, different tool

Use these to **frame transferable experience**, never to claim the other tool. If the posting wants X and the user has an equivalent Y, keep Y in the bullet and describe the shared concept in the posting's language.

| Concept | Equivalent tools |
| --- | --- |
| CI/CD pipelines | Jenkins, GitHub Actions, GitLab CI, Azure DevOps Pipelines, AWS CodePipeline/CodeBuild, Harness, CircleCI, Bamboo, TeamCity, Tekton, Spinnaker |
| GitOps delivery | Argo CD, Flux, OpenShift GitOps, Harness GitOps |
| Infrastructure as code | Terraform/OpenTofu, CloudFormation, CDK, Pulumi, ARM/Bicep, Deployment Manager, Crossplane |
| Configuration management | Ansible, Chef, Puppet, SaltStack |
| Container orchestration | Kubernetes, EKS, AKS, GKE, OpenShift, Rancher (RKE), ECS, Nomad |
| Identity provider / SSO | Okta, Entra ID, Ping, Auth0, Keycloak, Google Workspace |
| Cloud access federation | AWS IAM Identity Center, SAML/OIDC federation to AWS roles, Azure RBAC with Entra ID, GCP Workforce Identity |
| Secrets | Vault, AWS Secrets Manager, SSM Parameter Store, Azure Key Vault, GCP Secret Manager, Sealed Secrets, External Secrets Operator |
| Policy as code | OPA/Gatekeeper, Kyverno, Sentinel, AWS SCPs, Azure Policy, GCP Org Policy |
| Metrics and dashboards | Prometheus, Grafana, Datadog, CloudWatch, Azure Monitor, New Relic, Dynatrace |
| Logs | Splunk, ELK/OpenSearch, Loki, CloudWatch Logs, Datadog Logs |
| Tracing | OpenTelemetry, Jaeger, Zipkin, X-Ray, Datadog APM |
| Code and security scanning | SonarQube, Snyk, Checkmarx, Veracode, Trivy, Prisma Cloud, Wiz, GitHub Advanced Security |
| Artifact repositories | Nexus, Artifactory, ECR, ACR, Artifact Registry, GitHub Packages |
| Hybrid / private cloud platforms | HPE GreenLake, VMware Cloud Foundation, Nutanix, Azure Stack, AWS Outposts, Anthos |

**Framing pattern:** "Built and ran CI/CD pipelines (Jenkins, GitHub Actions) with staged approvals and automated rollback" fits a Harness posting through the shared concept, without claiming Harness.

## 3. Depth signals: what makes a claim believable

Senior readers judge depth by specifics. When a skill is real, surface the specifics that prove it.

| Skill | Shallow | Deep |
| --- | --- | --- |
| AWS IAM | "Managed IAM" | Least-privilege roles and policies, IRSA for EKS, permission boundaries, SCPs, Access Analyzer reviews, Identity Center permission sets |
| Kubernetes | "Worked with Kubernetes" | Cluster upgrades, PDBs, HPA, resource quotas, network policies, RBAC, admission control, multi-cluster |
| Terraform | "Wrote Terraform" | Reusable modules, remote state and locking, drift detection, policy checks, workspace strategy |
| CI/CD | "Built pipelines" | Shared libraries/templates, parallel stages, caching, quality gates, canary/blue-green, rollback |
| Observability | "Set up monitoring" | SLOs/SLIs, error budgets, alert tuning, dashboards tied to incidents, MTTR change |
| Security | "Followed best practices" | SAST/DAST gates, secrets rotation, audit controls, access reviews, CIS benchmarks |

Use only the specifics the user actually did. If a bullet can only be made deep by inventing, keep it shallow and honest.

## 4. Naming: use the current, correct name

- Spell products as the vendor does: `GitHub Actions`, `GitLab CI`, `Argo CD`, `OpenShift`, `PostgreSQL`, `Node.js`, `JavaScript`, `Kubernetes` (K8s in skills is fine).
- Use current names, with the old one in brackets the first time when the posting uses it: `Microsoft Entra ID (Azure AD)`, `AWS IAM Identity Center (AWS SSO)`, `Google Cloud Monitoring (Stackdriver)`, `OpenTofu` only if actually used.
- Mirror the posting's exact phrase once where it matches the user's real work (`HPE GreenLake`, `AWS CodePipeline`), so ATS keyword matching finds it.

## 5. Timeline: the tool must exist when the role used it

Every technology placed in a role must have been publicly available during that role's dates. `tech-timeline.json` lists first public release years; run `scripts/tech_check.py` (see SKILL.md 6d) to check a draft. A tool released after a role ended is an automatic fail. A tool released in the role's final year deserves a second look.

## 6. Seniority language

| Level | Verbs and scope that fit |
| --- | --- |
| Engineer | built, implemented, automated, supported, fixed |
| Senior | designed, owned, improved, standardized, mentored |
| Lead / Staff | led, set direction, defined standards, drove adoption across teams, partnered with leadership |

Use the level the user actually worked at. Don't upgrade "supported" to "led" without proof.
