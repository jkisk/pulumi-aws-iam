import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

export class AssumableRole extends pulumi.ComponentResource {
  role: aws.iam.Role;
  policies: aws.iam.RolePolicyAttachment[];

  constructor(
    name: string,
    args: AssumableRoleArgs,
    opts?: pulumi.ComponentResourceOptions
  ) {
    super("awsIam:index:assumableRole", name, opts);

    this.role = new aws.iam.Role(name, args, opts);
    this.policies = [];

    if (args.attachAdminPolicy) {
      let attArgs = {
        role: this.role,
        policyArn: "arn:aws:iam::aws:policy/AdministratorAccess",
      };
      this.policies.push(
        new aws.iam.RolePolicyAttachment(`${name}-admin`, attArgs)
      );
    }
    if (args.attachPowerUserPolicy) {
      let attArgs = {
        role: this.role,
        policyArn: "arn:aws:iam::aws:policy/PowerUserAccess",
      };
      this.policies.push(
        new aws.iam.RolePolicyAttachment(`${name}-power`, attArgs)
      );
    }

    if (args.attachReadOnlyPolicy) {
      let attArgs = {
        role: this.role,
        policyArn: "arn:aws:iam::aws:policy/ReadOnlyAccess",
      };
      this.policies.push(
        new aws.iam.RolePolicyAttachment(`${name}-read`, attArgs)
      );
    }
  }
}

export interface AssumableRoleArgs {
  // Policy that grants an entity permission to assume the role (required)
  assumeRolePolicy: pulumi.Input<string> | aws.iam.PolicyDocument;
  // Actions of STS
  trustedRoleActions: pulumi.Input<string> | "sts:AssumeRole";
  // ARNs of AWS entities who can assume these roles
  trustedRoleArns: pulumi.Input<Array<string>>;
  // AWS Services that can assume these roles
  trustedRoleServices: pulumi.Input<Array<string>>;
  // Max age of valid MFA (in seconds) for roles which require MFA
  mfa_age: pulumi.Input<number> | 86400;
  // Maximum CLI/API session duration in seconds between 3600 and 43200
  maxSessionDuration: pulumi.Input<number> | 3600;
  // Path of IAM role
  rolePath: pulumi.Input<Array<string>> | "/";
  // Whether role requires MFA
  roleRequiresMfa: pulumi.Input<boolean> | true;
  // Permissions boundary ARN to use for IAM role"
  rolePermissionsBoundaryArn: pulumi.Input<string> | "";
  // A map of tags to add to IAM role resources
  tags: pulumi.Input<{ [key: string]: pulumi.Input<string>; }> | undefined;
  // A custom role trust policy
  customRoleTrustPolicy: pulumi.Input<Array<string>>;
  // Whether to attach an admin policy to a role
  attachAdminPolicy: pulumi.Input<boolean> | false;
  // Whether to attach a poweruser policy to a role
  attachPowerUserPolicy: pulumi.Input<boolean> | false;
  // Whether to attach a readonly policy to a role
  attachReadOnlyPolicy: pulumi.Input<boolean> | false;
  // Whether policies should be detached from this role when destroying
  forceDetachPolicies: pulumi.Input<boolean> | false;
  // IAM Role description
  roleDescription: pulumi.Input<string> | "";
}