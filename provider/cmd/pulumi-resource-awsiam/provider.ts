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
import { User, UserArgs} from "./user";
import { IamRoleForServiceAccount, IamRoleForServiceAccountArgs } from "./iamRoleForServiceAccounts";

export class Provider implements provider.Provider {
    constructor(readonly version: string, readonly schema: string) { }

    async construct(name: string, type: string, inputs: pulumi.Inputs,
        options: pulumi.ComponentResourceOptions): Promise<provider.ConstructResult> {
        switch (type) {
            case "awsIam:index:User":
                return await constructUser(name, inputs, options);
            case "awsIam:index:AssumableRole":
                return await constructAssumableRole(name, inputs, options);
            case "awsIam:index:IamRoleForServiceAccount":
                return await constructIamRoleForServiceAccounts(name, inputs, options);
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    }
}

async function constructAssumableRole(name: string, inputs: pulumi.Inputs,
    options: pulumi.ComponentResourceOptions): Promise<provider.ConstructResult> {

    // Create the component resource.
    const component = new AssumableRole(name, inputs as AssumableRoleArgs, options);

    // Return the component resource's URN and outputs as its state.
    return {
        urn: component.urn,
        state: {
            role: component,
            policiesAttached: component.policies,
            createDate: component.role.createDate,
            uniqueId: component.role.uniqueId,
        },
    };
}

async function constructIamRoleForServiceAccounts(name: string, inputs: pulumi.Inputs,
    options: pulumi.ComponentResourceOptions): Promise<provider.ConstructResult> {

    // Create the component resource.
    const irsa = new IamRoleForServiceAccount(name, inputs as IamRoleForServiceAccountArgs, options);

    // Return the component resource's URN and outputs as its state.
    return {
        urn: irsa.urn,
        state: {
            role: irsa.role
        },
    };
}

async function constructUser(name: string, inputs: pulumi.Inputs,
    options: pulumi.ComponentResourceOptions): Promise<provider.ConstructResult> {

    // Create the component resource.
    const user = new User(name, inputs as UserArgs, options);

    // Return the component resource's URN and outputs as its state.
    return {
        urn: user.urn,
        state: {
            iamUser: user.iamUser,
            accessKey: user.iamAccessKey,
            loginProfile: user.iamUserLoginProfile,
            sshKey: user.iamUserSshKey,
        },
    };
}
