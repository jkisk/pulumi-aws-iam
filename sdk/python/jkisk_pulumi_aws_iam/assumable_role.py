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
                 assume_role_policy: pulumi.Input[str]):
        """
        The set of arguments for constructing a AssumableRole resource.
        :param pulumi.Input[str] assume_role_policy: Policy that grants an entity permission to assume the role.
        """
        pulumi.set(__self__, "assume_role_policy", assume_role_policy)

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


class AssumableRole(pulumi.ComponentResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 assume_role_policy: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a AssumableRole resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] assume_role_policy: Policy that grants an entity permission to assume the role.
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
        super(AssumableRole, __self__).__init__(
            'awsIam:index:AssumableRole',
            resource_name,
            __props__,
            opts,
            remote=True)
