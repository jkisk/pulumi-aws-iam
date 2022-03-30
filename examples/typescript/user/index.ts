import * as pulumi from "@pulumi/pulumi";
import * as iam from "@jkisk/pulumi-aws-iam";

const user = new iam.User("example", {
    createIamAccessKey: true,
    createUserLoginProfile: true,
})

export const iamUser = user.iamUser

