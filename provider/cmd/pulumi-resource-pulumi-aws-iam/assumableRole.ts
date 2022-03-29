import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";


export class AssumableRole extends pulumi.ComponentResource{
    role: aws.iam.Role;

    constructor(
        name: string,
        args: AssumableRoleArgs,
        opts?: pulumi.ComponentResourceOptions) {
        super("pulumi-aws-iam:assumableRole", name, opts);
        

        this.role = new aws.iam.Role(name, {
            assumeRolePolicy: args.assumeRolePolicy
        })
    }
}


export interface AssumableRoleArgs {
    // Policy that grants an entity permission to assume the role (required)
    assumeRolePolicy: pulumi.Input<string> | aws.iam.PolicyDocument,
    // IAM Role description
    description: pulumi.Input<string> | "",
    // Actions of STS
    trustedRoleActions: pulumi.Input<string> | "sts:AssumeRole",
    // ARNs of AWS entities who can assume these roles
    trustedRoleArns: pulumi.Input<Array<string>>,
    // AWS Services that can assume these roles
    trustedRoleServices: pulumi.Input<Array<string>>,
    // Max age of valid MFA (in seconds) for roles which require MFA
    mfa_age: pulumi.Input<number> | 86400,
    // Maximum CLI/API session duration in seconds between 3600 and 43200
    maxSessionDuration: pulumi.Input<number> | 3600,
    //  Whether to create a role
    createRole: pulumi.Input<boolean> | false,
    // Whether to create an instance profile
    createInstanceProfile: pulumi.Input<boolean> | false,
    // IAM role name
    roleName: pulumi.Input<Array<string>>,
    // Path of IAM role
    rolePath: pulumi.Input<Array<string>> | "/",
    // Whether role requires MFA
    roleRequiresMfa: pulumi.Input<boolean> | true,
    // Permissions boundary ARN to use for IAM role"
    rolePermissionsBoundaryArn: pulumi.Input<string> | "",
    // A map of tags to add to IAM role resources
    tags: pulumi.Input<Map<string, string>>,
    // List of ARNs of IAM policies to attach to IAM role
    customRolePolicyArns: pulumi.Input<Array<string>>,
    // A custom role trust policy
    customRoleTrustPolicy: pulumi.Input<Array<string>>,
    // Number of IAM policies to attach to IAM role
    numberOfCustomRolePolicyArns: pulumi.Input<Array<string>> | null,
    // Policy ARN to use for admin role
    adminRolePolicyArn: pulumi.Input<Array<string>> | "arn:aws:iam::aws:policy/AdministratorAccess",
    // Policy ARN to use for poweruser role
    powerUserRolePolicyArn: pulumi.Input<Array<string>> | "arn:aws:iam::aws:policy/PowerUserAccess",
    // Policy ARN to use for readonly role
    readOnlyRolePolicyArn: pulumi.Input<Array<string>> | "arn:aws:iam::aws:policy/ReadOnlyAccess",
    // Whether to attach an admin policy to a role
    attachAdminPolicy: pulumi.Input<boolean> | false,
    // Whether to attach a poweruser policy to a role
    attachPowerUserPolicy: pulumi.Input<boolean> | false,
    // Whether to attach a readonly policy to a role
    attachReadOnlyPolicy: pulumi.Input<boolean> | false,
    // Whether policies should be detached from this role when destroying
    forceDetachPolicies: pulumi.Input<boolean> | false,
    // STS ExternalId condition values to use with a role (when MFA is not required)
    roleStsExternalId: pulumi.Input<Array<string>> | [],
} 
