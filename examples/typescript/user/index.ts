import * as pulumi from "@pulumi/pulumi";
import * as iam from "@jkisk/pulumi-aws-iam";

export const user = new iam.User("example", {
    createIamAccessKey: true,
    createUserLoginProfile: true,
    passwordLength: 40,
    sshPublicKey: "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQC7lWCj2Amv0KvFiWH7UwKJQP+4hJulDgqLStMffODIu5wvlUdfqbAOdBm1pbTx05YnpgwTx+FSSKuDzXt12IC3t0sOA/iIs6iU74SV50+UqxwbrzuPTR1nyt3fltI1gyNvosoKGngSTekmNGAPsk09c0D2YFYr4HwhppZUZH4oLf/gyji3UzbxZyz8arCeB3SmmjOoT7b8xOzXdMFgIzmcZw6f37pzNrkWRN/aTnSlApw2LMLWQlsfHmU8XgNRuCoFoCw3LNCP7t0/szziBgFqA/AQu8S314hGhN3kift0wDUrHZviyD4PKP7seVLG30zas07sWNHNxyRp4bjatkd6XIyRzdP4MH2iqTMwz13nZM0icNS4990So3Ewz9tULT+GG+Ax+iAQbf11R1ZYlu8xZPKlH07SikgJrIqK2PP9REi4S+kLlIL6RO1tT1iNT5FtpqWcDpc5MQquI+cqbRJzTO+FmizphoWy0yRa0Zw0N+WkfDcco4isK397Fcv1AXdsUz872HMsJAC6XngAQTJOBmKXlSUop4SyKwWx60Th+5Fad5T9/UU6b9RvrtZHn/gbstY/6Txm7HmxOY1E+svXE5rdfKvvAlkD180Rcp1egFKMwRZHbjXX9uDubpGr9VyoKbXxrPYZG7lHaTliVnRK4JADhjy7TkBJ3XAIJ9fYPQ== lee@leebriggs.co.uk    "
})
