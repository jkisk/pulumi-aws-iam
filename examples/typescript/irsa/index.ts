import * as pulumi from "@pulumi/pulumi";
import * as iam from "@jkisk/pulumi-aws-iam";

const irsa = new iam.IamRoleForServiceAccount("example", {
    providerArn: "arn:aws:iam::616138583583:oidc-provider/oidc.eks.us-west-2.amazonaws.com/id/F78DEBB138819EE555599A7DB42461D3",
    namespace: "kube-system",
    serviceAccount: "external-dns"
})
