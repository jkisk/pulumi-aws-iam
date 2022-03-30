// *** WARNING: this file was generated by Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsIam
{
    [AwsIamResourceType("awsIam:index:User")]
    public partial class User : Pulumi.ComponentResource
    {
        /// <summary>
        /// The access key associated with the IAM user
        /// </summary>
        [Output("accessKey")]
        public Output<Pulumi.Aws.Iam.AccessKey?> AccessKey { get; private set; } = null!;

        /// <summary>
        /// The IAM user
        /// </summary>
        [Output("iamUser")]
        public Output<Pulumi.Aws.Iam.User> IamUser { get; private set; } = null!;

        /// <summary>
        /// The SSH key associated with the IAM user
        /// </summary>
        [Output("sshKey")]
        public Output<Pulumi.Aws.Iam.SshKey?> SshKey { get; private set; } = null!;

        /// <summary>
        /// The user login profile associated with the IAM user
        /// </summary>
        [Output("userLoginProfile")]
        public Output<Pulumi.Aws.Iam.UserLoginProfile?> UserLoginProfile { get; private set; } = null!;


        /// <summary>
        /// Create a User resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public User(string name, UserArgs args, ComponentResourceOptions? options = null)
            : base("awsIam:index:User", name, args ?? new UserArgs(), MakeResourceOptions(options, ""), remote: true)
        {
        }

        private static ComponentResourceOptions MakeResourceOptions(ComponentResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new ComponentResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = ComponentResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
    }

    public sealed class UserArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Boolean to determine whether to create an IAM access key
        /// </summary>
        [Input("createIamAccessKey", required: true)]
        public Input<bool> CreateIamAccessKey { get; set; } = null!;

        /// <summary>
        /// Boolean to determine whether to create an IAM user login profile
        /// </summary>
        [Input("createUserLoginProfile", required: true)]
        public Input<bool> CreateUserLoginProfile { get; set; } = null!;

        [Input("forceDestroy")]
        public Input<bool>? ForceDestroy { get; set; }

        [Input("passwordLength")]
        public Input<double>? PasswordLength { get; set; }

        [Input("passwordResetRequired")]
        public Input<bool>? PasswordResetRequired { get; set; }

        [Input("path")]
        public Input<string>? Path { get; set; }

        [Input("permissionsBoundary")]
        public Input<string>? PermissionsBoundary { get; set; }

        [Input("pgpKey")]
        public Input<string>? PgpKey { get; set; }

        [Input("sshKeyEncoding")]
        public Input<string>? SshKeyEncoding { get; set; }

        [Input("sshPublicKey")]
        public Input<string>? SshPublicKey { get; set; }

        [Input("uploadIamUserSshKey")]
        public Input<bool>? UploadIamUserSshKey { get; set; }

        public UserArgs()
        {
        }
    }
}
