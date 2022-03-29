import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

export interface UserArgs {
  createIamAccessKey: boolean;
  createUserLoginProfile: boolean;
  forceDestroy?: pulumi.Input<boolean>;
  pgpKey?: pulumi.Input<string>;
  passwordLength?: pulumi.Input<number>;
  passwordResetRequired?: pulumi.Input<boolean>;
  permissionsBoundary?: pulumi.Input<string>;
  path?: pulumi.Input<string>;
  sshKeyEncoding?: pulumi.Input<string>;
  sshPublicKey?: pulumi.Input<string>;
  tags?: pulumi.Input<{ [key: string]: pulumi.Input<string> }>;
}

export class User extends pulumi.ComponentResource {
  iamUser: aws.iam.User;
  iamUserLoginProfile?: aws.iam.UserLoginProfile;
  iamAccessKey?: aws.iam.AccessKey;
  iamUserSshKey?: aws.iam.SshKey;

  constructor(
    name: string,
    args: UserArgs,
    opts?: pulumi.ComponentResourceOptions
  ) {
    super("awsIam:index:User", name, opts);

    this.iamUser = new aws.iam.User(
      name,
      {
        path: args.path || "/",
        forceDestroy: args.forceDestroy,
        permissionsBoundary: args.permissionsBoundary,
        tags: args.tags,
      },
      { parent: this }
    );

    if (args.createUserLoginProfile) {
      this.iamUserLoginProfile = new aws.iam.UserLoginProfile(
        name,
        {
          user: this.iamUser.name,
          pgpKey: args.pgpKey,
          passwordLength: args.passwordLength,
          passwordResetRequired: args.passwordResetRequired,
        },
        { parent: this.iamUser }
      );
    }

    let accessKeyArgs: aws.iam.AccessKeyArgs = {
      user: this.iamUser.name,
    };

    if (args.pgpKey != null) {
      accessKeyArgs.pgpKey = args.pgpKey;
    }

    if (args.createIamAccessKey) {
      this.iamAccessKey = new aws.iam.AccessKey(name, accessKeyArgs, {
        parent: this.iamUser,
      });
    }

    if (args.sshPublicKey != null) {
      this.iamUserSshKey = new aws.iam.SshKey(
        name,
        {
          username: this.iamUser.name,
          encoding: args.sshKeyEncoding || "SSH",
          publicKey: args.sshPublicKey!,
        },
        { parent: this.iamUser }
      );
    }
  }
}
