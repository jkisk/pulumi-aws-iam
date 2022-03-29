// Copyright 2016-2021, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

import * as pulumi from "@pulumi/pulumi";
import * as provider from "@pulumi/pulumi/provider";

import { AssumableRoleArgs, AssumableRole } from "./assumableRole";

export class Provider implements provider.Provider {
    constructor(readonly version: string, readonly schema: string) { }

    async construct(name: string, type: string, inputs: pulumi.Inputs,
        options: pulumi.ComponentResourceOptions): Promise<provider.ConstructResult> {
        switch (type) {
            case "pulumi-aws-iam:index:IamUser":
                return await constructIamUser(name, inputs, options);
            case "pulumi-aws-iam:index:AssumableRole":
                return await constructAssumableRole(name, inputs, options);
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    }
}

async function constructAssumableRole(name: string, inputs: pulumi.Inputs,
    options: pulumi.ComponentResourceOptions): Promise<provider.ConstructResult> {

    // Create the component resource.
    const role = new AssumableRole(name, inputs as AssumableRoleArgs, options);

    // Return the component resource's URN and outputs as its state.
    return {
        urn: role.urn,
        state: {
            // name: role.arn,
            // path: role.id,
        },
    };
}
