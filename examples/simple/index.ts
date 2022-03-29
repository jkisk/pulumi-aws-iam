import * as iam from "@jkisk/pulumi-aws-iam";

const testRole = new iam.Role("test-role", {
    // indexContent: "<html><body><p>Hello world!</p></body></html>",
});

// export const bucket = page.bucket;
// export const url = page.websiteUrl;
