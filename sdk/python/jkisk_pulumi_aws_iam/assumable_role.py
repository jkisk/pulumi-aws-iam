# coding=utf-8
# *** WARNING: this file was generated by Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['AssumableRoleArgs', 'AssumableRole']

@pulumi.input_type
class AssumableRoleArgs:
    def __init__(__self__, *,
                 assume_role_policy: pulumi.Input[str],
                 attach_admin_policy: Optional[pulumi.Input[bool]] = None,
                 attach_power_user_policy: Optional[pulumi.Input[bool]] = None,
                 attach_read_only_policy: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a AssumableRole resource.
        :param pulumi.Input[str] assume_role_policy: Policy that grants an entity permission to assume the role.
        :param pulumi.Input[bool] attach_admin_policy: Whether to attach a predefined aws admin policy
        :param pulumi.Input[bool] attach_power_user_policy: Whether to attach a predefined aws poweruser policy
        :param pulumi.Input[bool] attach_read_only_policy: Whether to attach a predefined aws readonly policy
        """
        pulumi.set(__self__, "assume_role_policy", assume_role_policy)
        if attach_admin_policy is not None:
            pulumi.set(__self__, "attach_admin_policy", attach_admin_policy)
        if attach_power_user_policy is not None:
            pulumi.set(__self__, "attach_power_user_policy", attach_power_user_policy)
        if attach_read_only_policy is not None:
            pulumi.set(__self__, "attach_read_only_policy", attach_read_only_policy)

    @property
    @pulumi.getter(name="assumeRolePolicy")
    def assume_role_policy(self) -> pulumi.Input[str]:
        """
        Policy that grants an entity permission to assume the role.
        """
        return pulumi.get(self, "assume_role_policy")

    @assume_role_policy.setter
    def assume_role_policy(self, value: pulumi.Input[str]):
        pulumi.set(self, "assume_role_policy", value)

    @property
    @pulumi.getter(name="attachAdminPolicy")
    def attach_admin_policy(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to attach a predefined aws admin policy
        """
        return pulumi.get(self, "attach_admin_policy")

    @attach_admin_policy.setter
    def attach_admin_policy(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "attach_admin_policy", value)

    @property
    @pulumi.getter(name="attachPowerUserPolicy")
    def attach_power_user_policy(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to attach a predefined aws poweruser policy
        """
        return pulumi.get(self, "attach_power_user_policy")

    @attach_power_user_policy.setter
    def attach_power_user_policy(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "attach_power_user_policy", value)

    @property
    @pulumi.getter(name="attachReadOnlyPolicy")
    def attach_read_only_policy(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to attach a predefined aws readonly policy
        """
        return pulumi.get(self, "attach_read_only_policy")

    @attach_read_only_policy.setter
    def attach_read_only_policy(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "attach_read_only_policy", value)


class AssumableRole(pulumi.ComponentResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 assume_role_policy: Optional[pulumi.Input[str]] = None,
                 attach_admin_policy: Optional[pulumi.Input[bool]] = None,
                 attach_power_user_policy: Optional[pulumi.Input[bool]] = None,
                 attach_read_only_policy: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        Create a AssumableRole resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] assume_role_policy: Policy that grants an entity permission to assume the role.
        :param pulumi.Input[bool] attach_admin_policy: Whether to attach a predefined aws admin policy
        :param pulumi.Input[bool] attach_power_user_policy: Whether to attach a predefined aws poweruser policy
        :param pulumi.Input[bool] attach_read_only_policy: Whether to attach a predefined aws readonly policy
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AssumableRoleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a AssumableRole resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param AssumableRoleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AssumableRoleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 assume_role_policy: Optional[pulumi.Input[str]] = None,
                 attach_admin_policy: Optional[pulumi.Input[bool]] = None,
                 attach_power_user_policy: Optional[pulumi.Input[bool]] = None,
                 attach_read_only_policy: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is not None:
            raise ValueError('ComponentResource classes do not support opts.id')
        else:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AssumableRoleArgs.__new__(AssumableRoleArgs)

            if assume_role_policy is None and not opts.urn:
                raise TypeError("Missing required property 'assume_role_policy'")
            __props__.__dict__["assume_role_policy"] = assume_role_policy
            __props__.__dict__["attach_admin_policy"] = attach_admin_policy
            __props__.__dict__["attach_power_user_policy"] = attach_power_user_policy
            __props__.__dict__["attach_read_only_policy"] = attach_read_only_policy
            __props__.__dict__["arn"] = None
            __props__.__dict__["create_date"] = None
            __props__.__dict__["id"] = None
            __props__.__dict__["unique_id"] = None
        super(AssumableRole, __self__).__init__(
            'awsIam:index:AssumableRole',
            resource_name,
            __props__,
            opts,
            remote=True)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        Amazon Resource Name (ARN) specifying the role.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="createDate")
    def create_date(self) -> pulumi.Output[str]:
        """
        Creation date of the IAM role.
        """
        return pulumi.get(self, "create_date")

    @property
    @pulumi.getter
    def id(self) -> pulumi.Output[str]:
        """
        The provider-assigned unique ID for this managed resource..
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="uniqueId")
    def unique_id(self) -> pulumi.Output[str]:
        """
        Stable and unique string identifying the role.
        """
        return pulumi.get(self, "unique_id")

