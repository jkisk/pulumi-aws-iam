import * as iam from "@jkisk/pulumi-aws-iam";

const testRole = new iam.AssumableRole("test-role", {
    assumeRolePolicy: JSON.stringify({
        Version: "2012-10-17",
        Statement: [{
            Action: "sts:AssumeRole",
            Effect: "Allow",
            Sid: "",
            Principal: {
                Service: "ec2.amazonaws.com",
            },
        }],
    }),
    attachReadOnlyPolicy: true
});

export const role = testRole.role;