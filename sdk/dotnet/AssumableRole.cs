// *** WARNING: this file was generated by Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsIam
{
    [AwsIamResourceType("awsIam:index:AssumableRole")]
    public partial class AssumableRole : Pulumi.ComponentResource
    {
        /// <summary>
        /// ARN of the IAM role.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("attachedPolicies")]
        public Output<ImmutableArray<Pulumi.Aws.Iam.RolePolicyAttachment>> AttachedPolicies { get; private set; } = null!;

        /// <summary>
        /// Creation date of the IAM role.
        /// </summary>
        [Output("createDate")]
        public Output<string> CreateDate { get; private set; } = null!;

        /// <summary>
        /// The provider-assigned unique ID for this managed resource..
        /// </summary>
        [Output("id")]
        public Output<string> Id { get; private set; } = null!;

        /// <summary>
        /// The IAM role
        /// </summary>
        [Output("role")]
        public Output<Pulumi.Aws.Iam.Role?> Role { get; private set; } = null!;

        /// <summary>
        /// Stable and unique string identifying the role.
        /// </summary>
        [Output("uniqueId")]
        public Output<string> UniqueId { get; private set; } = null!;


        /// <summary>
        /// Create a AssumableRole resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public AssumableRole(string name, AssumableRoleArgs args, ComponentResourceOptions? options = null)
            : base("awsIam:index:AssumableRole", name, args ?? new AssumableRoleArgs(), MakeResourceOptions(options, ""), remote: true)
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

    public sealed class AssumableRoleArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Policy that grants an entity permission to assume the role.
        /// </summary>
        [Input("assumeRolePolicy", required: true)]
        public Input<string> AssumeRolePolicy { get; set; } = null!;

        /// <summary>
        /// Whether to attach a predefined aws admin policy
        /// </summary>
        [Input("attachAdminPolicy")]
        public Input<bool>? AttachAdminPolicy { get; set; }

        /// <summary>
        /// Whether to attach a predefined aws poweruser policy
        /// </summary>
        [Input("attachPowerUserPolicy")]
        public Input<bool>? AttachPowerUserPolicy { get; set; }

        /// <summary>
        /// Whether to attach a predefined aws readonly policy
        /// </summary>
        [Input("attachReadOnlyPolicy")]
        public Input<bool>? AttachReadOnlyPolicy { get; set; }

        public AssumableRoleArgs()
        {
        }
    }
}
