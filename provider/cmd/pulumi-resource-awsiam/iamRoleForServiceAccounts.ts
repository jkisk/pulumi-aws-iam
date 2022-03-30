import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

export interface IamRoleForServiceAccountArgs {
  rolePath?: pulumi.Input<string>;
  namespace: pulumi.Input<string>;
  serviceAccount: pulumi.Input<string>;
  providerArn: pulumi.Input<string>;
}

export class IamRoleForServiceAccount extends pulumi.ComponentResource {
  role: aws.iam.Role;

  constructor(
    name: string,
    args: IamRoleForServiceAccountArgs,
    opts?: pulumi.ComponentResourceOptions
  ) {
    super("awsIam:index:iamRoleForServiceAccount", name, opts);

    let assumeRolePolicy = pulumi
      .all([args.providerArn, args.serviceAccount, args.namespace])
      .apply(([provider, sa, namespace]) =>
        aws.iam.getPolicyDocument({
          statements: [
            {
              actions: ["sts:AssumeRoleWithWebIdentity"],
              conditions: [
                {
                  test: "StringEquals",
                  values: [`system:serviceaccount:${namespace}:${sa}`],
                  variable: `${provider.substring(
                    1,
                    provider.indexOf("/")
                  )}:sub`,
                },
              ],
              effect: "Allow",
              principals: [{ identifiers: [provider], type: "Federated" }],
            },
          ],
        })
      );

    this.role = new aws.iam.Role(name, {
      path: args.rolePath,
      assumeRolePolicy: assumeRolePolicy.json,
    }, { parent: this });

  }
}
