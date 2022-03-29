import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import { ThingGroupMembership } from "@pulumi/aws/iot";

export interface IamUserArgs {
  createUser: boolean;
  createUserLoginProfile: boolean;
  path: pulumi.Input<string> | "/";
  forceDestroy: pulumi.Input<boolean> | false;
  permissionsBoundary?: pulumi.Input<string> | "";
  pgpKey?: pulumi.Input<string> | "";
  passwordLength?: pulumi.Input<number> | 20;
  passwordResetRequired?: pulumi.Input<boolean> | true;
  tags?: pulumi.Input<{ [key: string]: pulumi.Input<string> }>;
}

export class IamUser extends pulumi.ComponentResource {
  iamUser: aws.iam.User;
  iamUserLoginProfile: aws.iam.UserLoginProfile;

  constructor(
    name: string,
    args: IamUserArgs,
    opts?: pulumi.ComponentResourceOptions
  ) {
    super("pulumi-aws-iam:index:IamUser", name, opts);

    if (args.createUser) {
      this.iamUser = new aws.iam.User(name, {
        path: args.path,
        forceDestroy: args.forceDestroy,
        permissionsBoundary: args.permissionsBoundary,
        tags: args.tags,
      });
    }

    if (args.createUser && args.createUserLoginProfile) {
        this.iamUserLoginProfile = new aws.iam.UserLoginProfile(name, {
            user: this.iamUser.name,
            pgpKey: args.pgpKey,
            passwordLength: args.passwordLength,
            passwordResetRequired: args.passwordResetRequired,
        })
    }

  }
}
